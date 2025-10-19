// LINK: https://www.acmicpc.net/problem/2741

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8").trim().split(/\s+/));

for (let i = 1; i < N + 1; i++) {
  console.log(i);
}
