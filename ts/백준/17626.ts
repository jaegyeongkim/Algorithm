// LINK: https://www.acmicpc.net/problem/17626

import * as fs from "fs";

let N = Number(fs.readFileSync(0, "utf8"));

let n = N;
let cnt = 0;
let arr: number[] = [];

while (n > 0) {
  const result = Math.floor(Math.sqrt(n));

  n -= Math.pow(result, 2);
  cnt += 1;
  arr.push(result);
  if (cnt > 4) {
    n = N;
    arr = [arr[0] - 1];
    n -= Math.pow(arr[0], 2);
    cnt = 1;
  }
}

console.log(cnt);
