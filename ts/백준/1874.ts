// LINK: https://www.acmicpc.net/problem/1874

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(Number);

const n = input[0];
const arr = input.splice(1);

const stack: number[] = [];

const result: string[] = [];

let cnt = 0;
for (let i = 1; i <= n; i++) {
  stack.push(i);
  result.push("+");

  while (1) {
    if (arr[cnt] === stack[stack.length - 1]) {
      stack.pop();
      result.push("-");
      cnt++;
    } else {
      break;
    }
    if (stack.length === 0) break;
  }
}

if (stack.length) {
  console.log("NO");
} else {
  console.log(result.join("\n"));
}
