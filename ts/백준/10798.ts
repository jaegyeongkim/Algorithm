// LINK: https://www.acmicpc.net/problem/10798

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

let maxLength = 0;
for (let i = 0; i < input.length; i++) {
  maxLength = Math.max(maxLength, input[i].length);
}

let letter = "";
for (let i = 0; i < maxLength; i++) {
  for (let j = 0; j < input.length; j++) {
    if (input[j][i]) {
      letter += input[j][i];
    }
  }
}
console.log(letter);
