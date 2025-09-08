// LINK: https://www.acmicpc.net/problem/2869

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
// const input = [2, 1, 5];
// const input = [5, 1, 6];
// const input = [100, 99, 1000000000];

const A = input[0];
const B = input[1];
const V = input[2];

console.log(Math.ceil((V - A) / (A - B)) + 1);
