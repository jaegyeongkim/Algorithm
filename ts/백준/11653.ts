// LINK: https://www.acmicpc.net/problem/11653

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8").trim().split(/\s+/));

if (N !== 1) {
  let number = N;
  let i = 2;

  while (number > 1) {
    if (number % i === 0) {
      number = number / i;
      console.log(i);
      i = 2;
    } else {
      i++;
    }
  }
}

