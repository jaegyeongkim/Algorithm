// LINK: https://www.acmicpc.net/problem/2292

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8"));
// const N = 8;

let num = 1;
let i = 1;
while (1) {
  if (N <= num) break;
  num += 6 * i;
  i++;
}

console.log(i);
