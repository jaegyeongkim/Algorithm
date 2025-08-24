import * as fs from "fs";

const input = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n")
  .map(Number);

// const input = [3, 4, 7, 10];

const N = input[0];
const dp = new Array(10 + 1).fill(0);
dp[0] = 0;
dp[1] = 1;
dp[2] = 2;
dp[3] = 4;
dp[4] = 7;
dp[5] = 13;

for (let i = 6; i <= 10; i++) {
  dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
}

for (let i = 1; i <= N; i++) {
  console.log(dp[input[i]]);
}
