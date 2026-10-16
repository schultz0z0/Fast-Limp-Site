import { readFile, writeFile, mkdir } from 'node:fs/promises';
const spec = JSON.parse(await readFile('design-system.json', 'utf8'));
const kebab = value => value.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase();
function resolve(value, seen = []) {
  if (typeof value !== 'string') return value;
  return value.replace(/\{([^}]+)\}/g, (_, path) => {
    if (seen.includes(path)) throw new Error(`Ciclo no token: ${path}`);
    const token = path.split('.').reduce((object, key) => object?.[key], spec.tokens);
    if (!token || !('$value' in token)) throw new Error(`Token ausente: ${path}`);
    return resolve(token.$value, [...seen, path]);
  });
}
const lines = [];
function visit(object, path = []) {
  for (const [key, value] of Object.entries(object)) {
    const next = [...path, kebab(key)];
    if ('$value' in value) {
      if (typeof value.$value === 'object') {
        for (const [prop, item] of Object.entries(value.$value)) lines.push(`  --${next.join('-')}-${kebab(prop)}: ${resolve(item)};`);
      } else lines.push(`  --${next.join('-')}: ${resolve(value.$value)};`);
    } else visit(value, next);
  }
}
visit(spec.tokens);
await mkdir('site/styles', { recursive: true });
await writeFile('site/styles/tokens.css', `/* Gerado de design-system.json. Não editar manualmente. */\n:root {\n${lines.join('\n')}\n}\n`);
console.log(`${lines.length} tokens resolvidos.`);
