// LINK: https://www.acmicpc.net/problem/9012

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

const N = Number(input[0]);
const arr = input.splice(1);

for (let i = 0; i < N; i++) {
  const cur = arr[i];
  const list: string[] = [];
  let result = true;

  for (let j = 0; j < cur.length; j++) {
    if (result === false) break;

    if (cur[j] === "(") {
      list.push(cur[j]);
    } else {
      if (list[list.length - 1] === "(") {
        list.pop();
      } else if (list.length === 0) {
        result = false;
      }
    }
  }

  if (result === false || list.length) {
    console.log("NO");
  } else {
    console.log("YES");
  }
}
