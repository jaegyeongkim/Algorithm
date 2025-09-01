// LINK: https://www.acmicpc.net/problem/11382

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const a = input[0];
const b = input[1];
const c = input[2];

console.log(a + b + c);
