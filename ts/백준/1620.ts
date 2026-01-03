// LINK: https://www.acmicpc.net/problem/1620

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

const [N, M] = input[0].split(" ").map(Number);

const arr = input.splice(1, N);
const answer = input.splice(1, M);
const result: (string | number)[] = [];

const map = new Map();

arr.forEach((name, idx) => {
  map.set(idx + 1, name);
  map.set(name, idx + 1);
});

answer.forEach((ans) => {
  if (Number(ans)) {
    result.push(map.get(Number(ans)));
  } else {
    result.push(map.get(ans));
  }
});

console.log(result.join("\n"));
