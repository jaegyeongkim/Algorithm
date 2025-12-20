// LINK: https://www.acmicpc.net/problem/11399

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = input.splice(1).sort((a, b) => a - b);

let sum = 0;
let beforeWaiting = 0;
arr.forEach((time) => {
  sum += beforeWaiting + time;
  beforeWaiting += time;
});

console.log(sum);
