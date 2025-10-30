// LINK: https://www.acmicpc.net/problem/2751

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = input.splice(1).sort((a, b) => a - b);

process.stdout.write(arr.join("\n"));
