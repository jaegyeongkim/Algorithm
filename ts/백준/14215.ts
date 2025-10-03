// https://www.acmicpc.net/problem/14215

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const a = input[0];
const b = input[1];
const c = input[2];

if (a + b <= c) {
  console.log(a * 2 + b * 2 - 1);
} else if (b + c <= a) {
  console.log(b * 2 + c * 2 - 1);
} else if (c + a <= b) {
  console.log(c * 2 + a * 2 - 1);
} else {
  console.log(a + b + c);
}
