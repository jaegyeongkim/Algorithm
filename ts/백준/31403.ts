// LINK: https://www.acmicpc.net/problem/31403

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);

const A = input[0];
const B = input[1];
const C = input[2];

console.log(Number(A) + Number(B) - Number(C));
console.log(Number(A + B) - Number(C));
