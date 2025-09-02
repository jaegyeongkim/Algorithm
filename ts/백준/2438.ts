// LINK: https://www.acmicpc.net/problem/2438

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [5];

const N = input[0];

for (let i = 0; i < N; i++) {
  let star = "";
  for (let j = 0; j < i + 1; j++) {
    star += "*";
  }
  console.log(star);
}
