// LINK: https://www.acmicpc.net/problem/11047

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const arr = input.splice(1).map(Number);

let rest = K;
let idx = arr.length - 1;
let coinCount = 0;

while (rest > 0) {
  if (Math.floor(rest / arr[idx])) {
    coinCount++;
    rest -= arr[idx];
  } else {
    idx--;
  }
}

console.log(coinCount);
