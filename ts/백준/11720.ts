// LINK: https://www.acmicpc.net/problem/11720

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);
// const input = ["5", "54321"];
// const input = ["25", "7000000000000000000000000"];

const N = Number(input[0]);
const arr = input[1].split("");
let sum = 0;

for (let i = 0; i < N; i++) {
  if (arr[i] !== "0") {
    sum += Number(arr[i]);
  }
}

console.log(sum);
