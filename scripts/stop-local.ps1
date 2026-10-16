$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$listeners = Get-NetTCPConnection -LocalPort 4173 -State Listen -ErrorAction SilentlyContinue
foreach ($listener in $listeners) {
    $ownerProcess = Get-CimInstance Win32_Process -Filter "ProcessId = $($listener.OwningProcess)"
    if ($ownerProcess.CommandLine -notlike "*$projectRoot*scripts*dev.mjs*") {
        throw 'O processo na porta 4173 não é o servidor deste projeto.'
    }
    Stop-Process -Id $listener.OwningProcess
    Write-Output 'Servidor Fast Limp encerrado.'
}
