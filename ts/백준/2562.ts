// LINK: https://www.acmicpc.net/problem/2562

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [3, 29, 38, 12, 57, 74, 40, 85, 61];

let max = -Infinity;
let index = 0;

for (let i = 0; i < 9; i++) {
  if (max < input[i]) {
    max = input[i];
    index = i + 1;
  }
}
console.log(max, `\n${index}`);
