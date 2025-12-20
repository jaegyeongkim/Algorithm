// LINK: https://www.acmicpc.net/problem/11723
// NOTE: node.js 로는 풀 수 없음 -> 컨셉 자체는 맞음

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

const S = new Set();
const N = Number(input[0]);
const arr = input.splice(1);
const out = [];

for (let i = 0; i < N; i++) {
  const [str, num] = arr[i].split(" ");

  switch (str) {
    case "add":
      S.add(Number(num));
      break;
    case "remove":
      S.delete(Number(num));
      break;
    case "check":
      S.has(Number(num)) ? out.push(1) : out.push(0);
      break;
    case "toggle":
      S.has(Number(num)) ? S.delete(Number(num)) : S.add(Number(num));
      break;
    case "all":
      S.clear();
      for (let i = 1; i < 21; i++) {
        S.add(i);
      }
      break;
    case "empty":
      S.clear();
      break;
  }
}

console.log(out.join("\n"));
