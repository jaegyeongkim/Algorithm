// LINK: https://www.acmicpc.net/problem/24313

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const a1 = input[0];
const a2 = input[1];
const c = input[2];
const n0 = input[3];

const fn = (n: number) => {
  return a1 * n + a2;
};
const gn = (n: number) => {
  return c * n;
};

let isTrue = 1;
let i = n0;
while (1) {
  if (i > 100) break;

  if (fn(i) > gn(i)) {
    isTrue = 0;
    break;
  }

  i++;
}

console.log(isTrue);
