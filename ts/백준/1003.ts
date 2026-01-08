// LINK: https://www.acmicpc.net/problem/1003

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(Number);
const arr = input.slice(1);

const dp: Record<number, number[]> = { 0: [1, 0], 1: [0, 1], 2: [1, 1] };

const maxNum = Math.max(...arr);

for (let num = 2; num <= maxNum; num++) {
  if (num !== 0 && num !== 1) {
    dp[num] = [];
    dp[num].push(dp[num - 2][0] + dp[num - 1][0]);
    dp[num].push(dp[num - 2][1] + dp[num - 1][1]);
  }
}

arr.forEach((num) => {
  console.log(dp[num].join(" "));
});
