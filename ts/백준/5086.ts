// LINK: https://www.acmicpc.net/problem/5086

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let i = 0;
while (1) {
  const left = input[i * 2];
  const right = input[i * 2 + 1];
  if (left === 0 && right === 0) break;

  if (left % right === 0) {
    console.log("multiple");
  } else if (right % left === 0) {
    console.log("factor");
  } else {
    console.log("neither");
  }

  i++;
}
