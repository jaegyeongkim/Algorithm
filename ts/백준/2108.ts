// LINK: https://www.acmicpc.net/problem/2108
import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = input.splice(1).sort((a, b) => a - b);

let total = 0;
const obj: Record<number, number> = {};
const half = Math.floor(N / 2);

for (let i = 0; i < N; i++) {
  total += arr[i];
  if (obj[arr[i]]) {
    obj[arr[i]] += 1;
  } else {
    obj[arr[i]] = 1;
  }
}

const sorted = Object.entries(obj).sort((a, b) => {
  if (b[1] === a[1]) {
    return Number(a[0]) - Number(b[0]);
  }
  return b[1] - a[1];
});

console.log(Math.round(total / N) === -0 ? 0 : Math.round(total / N));
console.log(arr[half]);
if (sorted.length > 1 && sorted[0][1] === sorted[1][1]) {
  console.log(sorted[1][0]);
} else {
  console.log(sorted[0][0]);
}
console.log(arr[N - 1] - arr[0]);
