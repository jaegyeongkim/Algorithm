// LINK: https://www.acmicpc.net/problem/2609

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let a = input[0];
let b = input[1];
let divider = 2;
let biggestDivider = 1;

while (1) {
  if (a === 1 || b === 1) break;

  if (a % divider === 0 && b % divider === 0) {
    a = a / divider;
    b = b / divider;
    biggestDivider *= divider;
    divider = 2;
  } else if (a / divider === 1 || b / divider === 1) break;
  else {
    divider += 1;
  }
}

console.log(biggestDivider);
console.log((input[0] * input[1]) / biggestDivider);
