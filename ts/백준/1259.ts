// LINK: https://www.acmicpc.net/problem/1259

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);

let i = 0;
while (1) {
  if (input[i] === "0") break;

  const str = input[i];
  const n = str.length;
  const half = Math.ceil(n / 2);
  let isTrue = true;

  for (let j = 0; j < half; j++) {
    const front = str[j];
    const back = str[n - j - 1];
    if (front !== back) {
      isTrue = false;
      break;
    }
  }

  console.log(isTrue ? "yes" : "no");

  i++;
}
