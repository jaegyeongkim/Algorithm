// https://www.acmicpc.net/problem/1018

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

const M = Number(input[0]);
const N = Number(input[1]);

const sample = ["W", "B", "W", "B", "W", "B", "W", "B"];
const sample2 = ["B", "W", "B", "W", "B", "W", "B", "W"];

let minCount = Infinity;

for (let i = 0; i < M - 7; i++) {
  if (minCount === 0) break;
  for (let k = 0; k < N - 7; k++) {
    if (minCount === 0) break;
    let total = 0;
    let total2 = 0;
    for (let j = 0; j < 8; j++) {
      const qwe = input[2 + i + j].split("").slice(k, k + 8);
      let count = 0;
      let count2 = 0;

      for (let m = 0; m < 8; m++) {
        if (j % 2 === 0) {
          if (qwe[m] !== sample[m]) {
            count += 1;
          }
          if (qwe[m] !== sample2[m]) {
            count2 += 1;
          }
        } else {
          if (qwe[m] !== sample2[m]) {
            count += 1;
          }
          if (qwe[m] !== sample[m]) {
            count2 += 1;
          }
        }
      }
      total += count;
      total2 += count2;
    }
    const answer = Math.min(total, total2);
    minCount = Math.min(minCount, answer);
  }
}

console.log(minCount);
