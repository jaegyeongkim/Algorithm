// LINK: https://www.acmicpc.net/problem/10773

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(Number);

const K = input[0];
const arr = input.slice(1);

let sum = 0;
const result = [];
for (let i = 0; i < arr.length; i++) {
  const curNum = arr[i];
  if (curNum === 0) {
    const lastNum = result.pop() as number;
    sum -= lastNum;
  } else {
    result.push(curNum);
    sum += curNum;
  }
}

console.log(sum);
