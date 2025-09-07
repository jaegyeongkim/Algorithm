// LINK: https://www.acmicpc.net/problem/2903

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8"));
// const N = 1;
// const N = 2;
// const N = 5;

let length = 2;

for (let i = 0; i < N; i++) {
  length += Math.pow(2, i);
}

console.log(Math.pow(length, 2));
