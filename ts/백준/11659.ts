// LINK: https://www.acmicpc.net/problem/11659

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").split("\n");

const [N, M] = input[0].split(" ").map(Number);

const arr = input[1].split(" ").map(Number);
const cals = input.splice(2, M);

let result: number[] = [];

let sum = 0;
for (let i = 0; i < arr.length; i++) {
  sum += arr[i];
  result.push(sum);
}

for (let cal of cals) {
  const [i, j] = cal.split(" ").map(Number);
  if (i === 1) {
    console.log(result[j - 1]);
  } else {
    console.log(result[j - 1] - result[i - 2]);
  }
}
