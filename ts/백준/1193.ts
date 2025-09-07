// LINK: https://www.acmicpc.net/problem/1193

import * as fs from "fs";

const X = Number(fs.readFileSync(0, "utf8"));
// const X = 14;

let beforeCount = 0;

let i = 1;
while (1) {
  beforeCount += i;
  if (X <= beforeCount) {
    beforeCount -= i;
    break;
  }
  i++;
}
if (i % 2) {
  console.log(`${i + 1 - X + beforeCount}/${X - beforeCount}`);
} else {
  console.log(`${X - beforeCount}/${i + 1 - X + beforeCount}`);
}
