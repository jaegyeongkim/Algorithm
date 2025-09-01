// LINK: https://www.acmicpc.net/problem/2525

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const A = input[0];
const B = input[1];
const C = input[2];

const whatTime = (h: number, m: number, spend: number): void => {
  const time = h * 60 + m + spend;

  const hour = Math.floor(time / 60);
  const minute = time % 60;
  console.log(hour >= 24 ? hour - 24 : hour, minute);
};

whatTime(A, B, C);
