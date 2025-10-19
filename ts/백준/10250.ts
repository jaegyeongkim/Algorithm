// LINK: https://www.acmicpc.net/problem/10250

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const T = input[0];
const arr = input.splice(1);

let count = 0;

while (count < T) {
  const H = arr[count * 3];
  const W = arr[count * 3 + 1];
  const N = arr[count * 3 + 2];

  const q = Math.floor(N / H);
  const rest = N % H;
  const floor = rest === 0 ? H : rest;
  const ho = rest === 0 ? q : q + 1;
  console.log(String(floor) + String(ho).padStart(2, "0"));

  count++;
}
