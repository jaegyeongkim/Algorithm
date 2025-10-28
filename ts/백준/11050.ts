// LINK: https://www.acmicpc.net/problem/11050

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const K = input[1];
const arr = [1];

const facotiral = (n: number) => {
  let result = 1;
  for (let i = 1; i < n + 1; i++) {
    result *= i;
    arr.push(result);
  }
  return result;
};

console.log(facotiral(N) / arr[N - K] / arr[K]);
