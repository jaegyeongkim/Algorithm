// LINK: https://www.acmicpc.net/problem/2720

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const T = input[0];
const coins = [25, 10, 5, 1];

for (let i = 1; i < T + 1; i++) {
  const answer = [0, 0, 0, 0];

  let num = input[i];
  let j = 0;

  while (num > 0) {
    if (num < coins[j]) {
      j++;
      continue;
    }
    num -= coins[j];
    answer[j]++;
  }
  console.log(answer.join(" "));
}
