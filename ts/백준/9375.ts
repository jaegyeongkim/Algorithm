// LINK: https://www.acmicpc.net/problem/9375

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").split("\n");

const N = Number(input[0]);
const arr = input.splice(1);
let n = 0;
let c = 0;

while (c < N) {
  const num = Number(arr[n]);
  const obj: Record<string, string[]> = {};

  for (let i = n + 1; i <= n + num; i++) {
    const [key, value] = arr[i].split(" ");
    if (obj[value]) {
      obj[value].push(key);
    } else {
      obj[value] = [key];
    }
  }
  let result = 1;
  Object.entries(obj).forEach(([key, value]) => {
    result *= value.length + 1;
  });

  c++;
  n += num + 1;
  console.log(result - 1);
}
