// LINK: https://www.acmicpc.net/problem/2439

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [5];

const N = input[0];

for (let i = 0; i < N; i++) {
  let str = "";
  for (let j = N - 1; j >= 0; j--) {
    if (j <= i) {
      str += "*";
    } else {
      str += " ";
    }
  }
  console.log(str);
}
