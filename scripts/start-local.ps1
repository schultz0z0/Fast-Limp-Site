$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$port = 4173
$existing = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
if ($existing) {
    $ownerProcess = Get-CimInstance Win32_Process -Filter "ProcessId = $($existing[0].OwningProcess)"
    if ($ownerProcess.CommandLine -notlike "*$projectRoot*scripts*dev.mjs*") {
        throw "A porta $port já está ocupada por outro processo."
    }
    Write-Output "Fast Limp já está ativo: http://127.0.0.1:$port"
    exit 0
}
$nodePath = (Get-Command node.exe).Source
$serverPath = Join-Path $projectRoot 'scripts\dev.mjs'
$commandLine = '"' + $nodePath + '" "' + $serverPath + '"'
$startup = New-CimInstance -ClassName Win32_ProcessStartup -ClientOnly -Property @{ ShowWindow = [uint16]0 }
# WMI inicia fora da árvore temporária do terminal do agente. Sem tarefa agendada
# ou execução no login; o servidor continua restrito a 127.0.0.1.
$result = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{
    CommandLine = $commandLine
    CurrentDirectory = $projectRoot
    ProcessStartupInformation = $startup
}
if ($result.ReturnValue -ne 0) { throw "Falha ao iniciar servidor local: $($result.ReturnValue)" }
$serverPid = $result.ProcessId
$deadline = [DateTime]::UtcNow.AddSeconds(15)
do {
    try {
        $response = Invoke-WebRequest "http://127.0.0.1:$port/assets/photos/gallery-03-640.webp" -UseBasicParsing -TimeoutSec 2
        if ($response.StatusCode -eq 200) {
            Write-Output "Fast Limp ativo: http://127.0.0.1:$port (PID $serverPid). Fotos respondendo HTTP 200."
            exit 0
        }
    } catch { Start-Sleep -Milliseconds 200 }
} while ([DateTime]::UtcNow -lt $deadline)
throw "O processo $serverPid iniciou, mas o servidor ainda não respondeu."
