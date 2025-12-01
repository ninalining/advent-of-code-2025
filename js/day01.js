#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const inputFilePath = path.join(__dirname, '..', 'inputs', 'day01.txt');

const lines = fs
    .readFileSync(inputFilePath, 'utf-8')
    .trim()
    .split('\n')
    .filter(Boolean);

let position = 50;
let count = 0;

for (const line of lines) {
    const direction = line[0];
    const amount = parseInt(line.slice(1), 10);

    if (direction === 'L') {
        position = (position - amount + 100) % 100;

    } else if (direction === 'R') {
        position = (position + amount) % 100;
    }
    if (position === 0) {
        count += 1;
    }
}

console.log(`Password: ${count}`);