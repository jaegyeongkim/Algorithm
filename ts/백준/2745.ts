// LINK: https://www.acmicpc.net/problem/2745

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);

const N = input[0];
const B = Number(input[1]);
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

let total = 0;
for (let i = 0; i < N.length; i++) {
  const index = alpha.findIndex((v: (typeof alpha)[number]) => v === N[i]);

  total += index * Math.pow(B, N.length - 1 - i);
}

console.log(total);
