// LINK: https://www.acmicpc.net/problem/3009

import * as fs from "fs";

const xArr: Record<string, number> = {};
const yArr: Record<string, number> = {};

fs.readFileSync(0, "utf8")
  .trim()
  .split(/\s+/)
  .forEach((num: string, i) => {
    if (i % 2 === 0) {
      xArr[num] = (xArr[Number(num)] || 0) + 1;
    } else {
      yArr[num] = (yArr[Number(num)] || 0) + 1;
    }
  });

const answer: string[] = [];

Object.entries(xArr).forEach(([key, value]) => {
  if (value === 1) answer.push(key);
});
Object.entries(yArr).forEach(([key, value]) => {
  if (value === 1) answer.push(key);
});

console.log(answer.join(" "));
