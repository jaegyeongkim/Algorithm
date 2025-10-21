// LINK: https://www.acmicpc.net/problem/8958

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);

const N = Number(input[0]);
const arr = input.splice(1);

for (let i = 0; i < N; i++) {
  let cnt = 0;
  let sum = 0;
  arr[i].split("").forEach((str) => {
    if (str === "O") {
      cnt++;
    } else {
      cnt = 0;
    }
    sum += cnt;
  });

  console.log(sum);
}
