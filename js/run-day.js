#!/usr/bin/env node

const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

const [, , dayArg = '01'] = process.argv;
const day = dayArg.padStart(2, '0');
const targetFile = path.join(__dirname, `day${day}.js`);

if (!fs.existsSync(targetFile)) {
  console.error(`No JS solution found for day ${day}. Expected file: ${targetFile}`);
  process.exit(1);
}

const result = spawnSync('node', [targetFile], { stdio: 'inherit' });
process.exit(result.status ?? 1);
