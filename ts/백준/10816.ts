// LINK: https://www.acmicpc.net/problem/10816

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);
const numbers = input[3].split(" ").map(String);

const obj = new Map();

input[1].split(" ").forEach((num) => {
  const cur = obj.get(num);
  if (!obj.get(num)) {
    obj.set(num, 1);
  } else {
    obj.set(num, cur + 1);
  }
});

let output = "";
numbers.forEach((num, idx) => {
  output += obj.get(num) ? obj.get(num) : 0;
  if (numbers.length - 1 !== idx) {
    output += " ";
  }
});

console.log(output);
