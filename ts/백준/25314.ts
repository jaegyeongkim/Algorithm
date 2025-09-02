// LINK: https://www.acmicpc.net/problem/25314

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];

let long = "";
for (let i = 0; i < N / 4; i++) {
  long += "long ";
}

console.log(long + "int ");
