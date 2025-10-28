// LINK: https://www.acmicpc.net/problem/14626

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("");

let sum = 0;
let mul = 1;
input.forEach((str, idx) => {
  if (idx % 2 === 0) {
    if (str === "*") {
      mul = 1;
    } else {
      sum += Number(str);
    }
  } else {
    if (str === "*") {
      mul = 3;
    } else {
      sum += 3 * Number(str);
    }
  }
});

let x = 0;
while (1) {
  if ((sum + mul * x) % 10 === 0) {
    console.log(x);
    break;
  }
  x++;
}
