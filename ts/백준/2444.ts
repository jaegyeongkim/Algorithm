// LINK: https://www.acmicpc.net/problem/2444

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8"));
// const N = 5;
const arr: string[] = [];
for (let i = 0; i < N * 2 - 1; i++) {
  let stars = "";
  if (i < N) {
    for (let j = 0; j < N + i; j++) {
      if (j < N - i - 1) {
        stars += " ";
      } else {
        stars += "*";
      }
    }
    console.log(stars);
    arr.push(stars);
  } else {
    console.log(arr[2 * N - 2 - i]);
  }
}
