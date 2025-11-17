// LINK: https://www.acmicpc.net/problem/4949

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

for (let i = 0; i < input.length; i++) {
  if (input[i][0] === ".") break;

  const arr: string[] = [];
  for (let j = 0; j < input[i].length; j++) {
    if (input[i][j] === "(" || input[i][j] === "[") {
      arr.push(input[i][j]);
    } else if (input[i][j] === ")" || input[i][j] === "]") {
      if (
        (arr[arr.length - 1] === "(" && input[i][j] === ")") ||
        (arr[arr.length - 1] === "[" && input[i][j] === "]")
      ) {
        arr.pop();
      } else {
        arr.push(input[i][j]);
      }
    }
  }
  console.log(arr.length ? "no" : "yes");
}
