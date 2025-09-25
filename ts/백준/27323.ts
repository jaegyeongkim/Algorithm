// https://www.acmicpc.net/problem/27323

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const A = input[0];
const B = input[1];

console.log(A * B);
