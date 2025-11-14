// LINK: https://www.acmicpc.net/problem/2164

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8"));

let arr = new Array(N).fill(0).map((_, idx) => idx + 1);

let cnt = 0;
while (arr.length > 1) {
  let newArr: number[] = [];
  for (let i = 0; i < arr.length; i++) {
    if (cnt % 2 === 0) {
      if (i % 2 === 1) {
        newArr.push(arr[i]);
      }
    } else {
      if (i % 2 === 0) {
        newArr.push(arr[i]);
      }
    }
  }
  cnt += arr.length;
  arr = newArr;
}
console.log(arr[0]);
