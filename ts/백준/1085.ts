// LINK: https://www.acmicpc.net/problem/1085

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const [x, y, w, h] = input;

const min = Math.min(
  Math.abs(x - 0),
  Math.abs(y - 0),
  Math.abs(w - x),
  Math.abs(h - y)
);
console.log(min);
