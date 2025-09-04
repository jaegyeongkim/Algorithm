// LINK: https://www.acmicpc.net/problem/3003

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
// const input = [0, 1, 2, 2, 2, 7];

const arr = [1, 1, 2, 2, 2, 8];
const answer: number[] = [];

for (let i = 0; i < input.length; i++) {
  answer[i] = arr[i] - input[i];
}

console.log(answer.join(" "));
