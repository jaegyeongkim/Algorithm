// LINK: https://www.acmicpc.net/problem/2501

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const K = input[1];

let count = 0;
let number = 0;
for (let i = 1; i <= N; i++) {
  if (N % i === 0) {
    count += 1;
  }
  if (count === K) {
    number = i;
    break;
  }
}

console.log(number);
