// LINK: https://www.acmicpc.net/problem/2581

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const M = input[0];
const N = input[1];

let minNum = 0;
let sum = 0;
for (let i = M; i <= N; i++) {
  let is소수 = true;
  if (i === 1) continue;
  for (let j = 2; j < i; j++) {
    if (i % j === 0) {
      is소수 = false;
      break;
    }
  }
  if (is소수) {
    if (!minNum) {
      minNum = i;
    }
    sum += i;
  }
}

if (sum) {
  console.log(sum);
  console.log(minNum);
} else {
  console.log(-1);
}
