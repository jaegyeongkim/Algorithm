// LINK: https://www.acmicpc.net/problem/1676

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8"));

let cnt = 0;
for (let i = 1; i < N + 1; i++) {
  if (i % 5 === 0) {
    let num = i;
    while (1) {
      if (num % 5 !== 0) {
        break;
      }
      num = num / 5;
      cnt += 1;
    }
  }
}

console.log(cnt);
