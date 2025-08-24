// LINK: https://www.acmicpc.net/problem/1912

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [10, 10, -4, 3, 1, 5, 6, -35, 12, 21, -1];
// const input = [10, 2, 1, -4, 3, 4, -4, 6, 5, -5, 1];
// const input = [5, -1, -2, -3, -4, -5];

const N = input[0];
const arr = input.slice(1, 1 + N);

let best = arr[0];
let cur = arr[0];

for (let i = 1; i < N; i++) {
  cur = Math.max(arr[i], cur + arr[i]);

  best = Math.max(best, cur);
}

console.log(best);
