import * as fs from "fs";

const input = Number(fs.readFileSync("/dev/stdin", "utf8").trim());

const dp = new Array(input + 1).fill(0);
dp[1] = 0;

for (let i = 2; i <= input; i++) {
  dp[i] = dp[i - 1] + 1;
  if (i % 2 === 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);
  if (i % 3 === 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);
}

console.log(dp[input]);
