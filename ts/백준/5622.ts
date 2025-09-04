// LINK: https://www.acmicpc.net/problem/5622

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);
// const input = ["WA"];
// const input = ["UNUCIC"];

const str = input[0];

const phone = {
  A: 2,
  B: 2,
  C: 2,
  D: 3,
  E: 3,
  F: 3,
  G: 4,
  H: 4,
  I: 4,
  J: 5,
  K: 5,
  L: 5,
  M: 6,
  N: 6,
  O: 6,
  P: 7,
  Q: 7,
  R: 7,
  S: 7,
  T: 8,
  U: 8,
  V: 8,
  W: 9,
  X: 9,
  Y: 9,
  Z: 9,
} as const;

let sum = 0;
for (let i = 0; i < str.length; i++) {
  const count = phone[str[i] as keyof typeof phone];
  sum += count + 1;
}

console.log(sum);
