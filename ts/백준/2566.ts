// LINK: https://www.acmicpc.net/problem/2566

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
// const input = [
//   3, 23, 85, 34, 17, 74, 25, 52, 65, 10, 7, 39, 42, 88, 52, 14, 72, 63, 87, 42,
//   18, 78, 53, 45, 18, 84, 53, 34, 28, 64, 85, 12, 16, 75, 36, 55, 21, 77, 45,
//   35, 28, 75, 90, 76, 1, 25, 87, 65, 15, 28, 11, 37, 28, 74, 65, 27, 75, 41, 7,
//   89, 78, 64, 39, 47, 47, 70, 45, 23, 65, 3, 41, 44, 87, 13, 82, 38, 31, 12, 29,
//   29, 80,
// ];

let max = -Infinity;
const arr = [0, 0];
for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (max < input[i * 9 + j]) {
      max = input[i * 9 + j];
      arr[0] = i + 1;
      arr[1] = j + 1;
    }
  }
}

console.log(max);
console.log(arr.join(" "));
