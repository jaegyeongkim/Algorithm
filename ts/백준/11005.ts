// LINK: https://www.acmicpc.net/problem/11005

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
// const input = [60466175, 36];
// const input = [9, 2];
// const input = [8, 2];
// const input = [0, 2];

let N = input[0];
const B = input[1];
const alpha = [
  "0",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
] as const;

let maxNum = 1;

while (1) {
  const num = Math.pow(B, maxNum);

  if (N < num) break;

  maxNum++;
}

const letter: string[] = [];

for (let i = maxNum - 1; i >= 0; i--) {
  const num = Math.pow(B, i);
  const count = Math.floor(N / num);

  N -= count * num;
  letter.push(alpha[count]);
}

console.log(letter.join(""));
