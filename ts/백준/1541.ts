// LINK: https://www.acmicpc.net/problem/1541

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim();

const arr: (string | number)[] = [];

let str = "";
for (let i = 0; i < input.length; i++) {
  if (input[i] === "-") {
    if (str.length > 0) {
      arr.push(Number(str));
      str = "";
    }
    arr.push("-");
  } else if (input[i] !== "+") {
    str += input[i];
  } else {
    if (str.length > 0) {
      arr.push(Number(str));
      str = "";
    }
    arr.push("+");
  }

  if (i === input.length - 1) {
    arr.push(Number(str));
  }
}

let result = arr[0] as number;
let minusStart = false;
for (let i = 2; i < arr.length; i += 2) {
  if (minusStart === false && arr[i - 1] === "-") {
    minusStart = true;
  }

  if (minusStart) {
    result -= arr[i] as number;
  } else {
    result += arr[i] as number;
  }
}

console.log(result);
