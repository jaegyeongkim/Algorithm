// LINK: https://www.acmicpc.net/problem/10813

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = Number(input[0]);
const arr = input.splice(1);

arr.sort((a, b) => {
  return a < b;
});
