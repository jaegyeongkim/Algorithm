// LINK: https://www.acmicpc.net/problem/11650

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const [arr1, arr2] = [...input].splice(1).reduce<number[][]>(
  (acc, cur, idx) => {
    if (idx % 2) {
      acc[1].push(cur);
      return acc;
    } else {
      acc[0].push(cur);

      return acc;
    }
  },
  [[], []]
);

arr1.sort((a, b) => a - b);
arr2.sort((a, b) => a - b);

for (let i = 0; i < N; i++) {
  console.log(arr1[i], arr2[i]);
}
