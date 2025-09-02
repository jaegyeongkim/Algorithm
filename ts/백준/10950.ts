// LINK: https://www.acmicpc.net/problem/10950

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const n = input[0];
const arr = input.splice(1);

for (let i = 0; i < n; i++) {
  console.log(arr[i * 2] + arr[i * 2 + 1]);
}
