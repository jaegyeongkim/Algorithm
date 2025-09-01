// LINK: https://www.acmicpc.net/problem/2588

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

const a = Number(input[0]);
const b = String(input[1]);
const b1 = Number(b[2]);
const b2 = Number(b[1]);
const b3 = Number(b[0]);

console.log(a * b1);
console.log(a * b2);
console.log(a * b3);
console.log(a * Number(b));
