// LINK: https://www.acmicpc.net/problem/2475

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let sum = 0;

for (let i = 0; i < input.length; i++) {
  sum += Math.pow(input[i], 2);
}

console.log(sum % 10);
