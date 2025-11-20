// LINK: https://www.acmicpc.net/problem/10828

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

const N = Number(input[0]);
const stack: string[] = [];
const result: any[] = [];

for (let i = 1; i < N + 1; i++) {
  switch (input[i]) {
    case "pop":
      if (stack.length) {
        result.push(stack.pop());
      } else {
        result.push("-1");
      }
      break;
    case "size":
      result.push(stack.length);
      break;
    case "empty":
      result.push(stack.length ? 0 : 1);
      break;
    case "top":
      if (stack.length) {
        result.push(stack[stack.length - 1]);
      } else {
        result.push("-1");
      }
      break;
    default: // "push"
      const [_, X] = input[i].split(" ");
      stack.push(X);
      break;
  }
}

process.stdout.write(result.join("\n").replace(/,/g, " "));
