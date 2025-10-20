// LINK: https://www.acmicpc.net/problem/2577

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const A = input[0];
const B = input[1];
const C = input[2];

const result = String(A * B * C).split("");
const arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

result.forEach((str) => {
  arr[Number(str)]++;
});

arr.forEach((str) => {
  console.log(str);
});
