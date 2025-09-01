// LINK: https://www.acmicpc.net/problem/2480

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const a = input[0];
const b = input[1];
const c = input[2];

const whatMoney = (a: number, b: number, c: number): void => {
  if (a === b && b === c) {
    console.log(10000 + a * 1000);
  } else if (a === b) {
    console.log(1000 + a * 100);
  } else if (b === c) {
    console.log(1000 + b * 100);
  } else if (c === a) {
    console.log(1000 + c * 100);
  } else {
    const biggest = Math.max(a, b, c);
    console.log(biggest * 100);
  }
};

whatMoney(a, b, c);
