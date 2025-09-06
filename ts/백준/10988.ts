// LINK: https://www.acmicpc.net/problem/10988

import * as fs from "fs";

const letter = fs.readFileSync(0, "utf8").trim();
// const letter = "level";
// const letter = "baekjoon";

let isTrue = 1;
const N = letter.length;

for (let i = 0; i < Math.floor(N / 2); i++) {
  if (isTrue === 0) break;

  if (letter[i] !== letter[N - 1 - i]) isTrue = 0;
}

console.log(isTrue);
