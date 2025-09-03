// LINK: https://www.acmicpc.net/problem/5597

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [
//   3, 1, 4, 5, 7, 9, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
//   24, 25, 26, 27, 28, 29, 30,
// ];

const N = input.length;
const arr: number[] = Array.from({ length: 31 }, (_: unknown, i: number) => i);

for (let i = 0; i < N; i++) {
  const index = arr.findIndex((value: number) => value === input[i]);

  if (index) {
    arr.splice(index, 1);
  }
}

console.log(arr[1]);
console.log(arr[2]);
