// LINK: https://www.acmicpc.net/problem/24265

import * as fs from "fs";

const n = Number(fs.readFileSync(0, "utf8").trim().split(/\s+/));

let sum = 0;
for (let i = 1; i < n; i++) {
  sum += i;
}
console.log(sum);
console.log(2);
