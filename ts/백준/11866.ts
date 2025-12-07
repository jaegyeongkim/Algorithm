// LINK: https://www.acmicpc.net/problem/11866

import * as fs from "fs";

const [N, K] = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
const arr = new Array(N).fill(0).map((_, idx) => idx + 1);
const result = [];
let beforeIdx = 0;

while (result.length < N) {
  let count = 0;

  while (1) {
    if (arr[beforeIdx] !== 0) {
      count += 1;
    }

    if (count >= K) break;

    beforeIdx += 1;
    if (beforeIdx >= N) {
      beforeIdx -= N;
    }
  }

  result.push(arr[beforeIdx]);
  arr[beforeIdx] = 0;
}

console.log(`<${result.join(", ")}>`);
