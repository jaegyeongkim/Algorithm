// LINK: https://www.acmicpc.net/problem/9086

import * as fs from "fs";

const input = fs.readFileSync(0, "utf-8").trim().split(/\s+/).map(String);
// const input = ["3", "ACDKJFOWIEGHE", "O", "AB"];

const T = Number(input[0]);

for (let i = 1; i < T + 1; i++) {
  const N = input[i].length;
  console.log(`${input[i][0]}${input[i][N - 1]}`);
}
