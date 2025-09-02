// LINK: https://www.acmicpc.net/problem/10871

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [10, 5, 1, 10, 4, 9, 2, 3, 8, 5, 7, 6];

const N = input[0];
const X = input[1];
const arr = input.splice(2);
let numbers = "";
for (let i = 0; i < N; i++) {
  if (arr[i] < X) {
    if (numbers.length > 0) {
      numbers += " ";
    }
    numbers += arr[i];
  }
}

console.log(numbers);
