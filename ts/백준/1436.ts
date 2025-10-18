// LINK: https://www.acmicpc.net/problem/1436https://www.acmicpc.net/problem/1436

import * as fs from "fs";

const input = Number(fs.readFileSync(0, "utf8").trim().split(/\s+/));

let count = 0;
let num = 666;

while (1) {
  if (String(num).includes("666")) {
    count++;
  }

  if (count === input) break;
  num++;
}

console.log(num);
