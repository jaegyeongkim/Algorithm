// LINK: https://www.acmicpc.net/problem/2579

import * as fs from "fs";

const input = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n")
  .map(Number);

const N = input[0];
const dp = new Array(N + 1);

dp[1] = input[1];
dp[2] = input[1] + input[2];
dp[3] = Math.max(input[1], input[2]) + input[3];

for (let i = 4; i <= N; i++) {
  dp[i] = Math.max(dp[i - 3] + input[i - 1], dp[i - 2]) + input[i];
}

console.log(dp[N]);
