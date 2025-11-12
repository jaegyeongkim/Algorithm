// LINK: https://www.acmicpc.net/problem/11650

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = input.splice(1);
const result: number[][] = [];

for (let i = 0; i < N * 2; i += 2) {
  result.push([arr[i], arr[i + 1]]);
}

result.sort((a, b) => {
  if (a[0] - b[0] === 0) {
    return a[1] - b[1];
  } else {
    return a[0] - b[0];
  }
});
result.forEach((a) => {
  console.log(a[0], a[1]);
});
