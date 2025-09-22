// LINK: https://www.acmicpc.net/problem/1978


import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = input.splice(1);
let count = 0;

for (let i = 0; i < N; i++) {
  let canDivide = 0;

  for (let j = 1; j < arr[i]; j++) {
    if (arr[i] % j === 0) {
      canDivide++;
    }
    if (canDivide > 2) {
      break;
    }
  }
  if (canDivide === 1) {
    count++;
  }
}

console.log(count);
