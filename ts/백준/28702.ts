// LINK: https://www.acmicpc.net/problem/28702

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);

const a = input[0];
const b = input[1];
const c = input[2];

let num = 0;

if (`${Number(a)}` !== "NaN") {
  num = Number(a) + 3;
} else if (`${Number(b)}` !== "NaN") {
  num = Number(b) + 2;
} else if (`${Number(c)}` !== "NaN") {
  num = Number(c) + 1;
}

if (num % 5 === 0 && num % 3 === 0) {
  console.log("FizzBuzz");
} else if (num % 3 === 0) {
  console.log("Fizz");
} else if (num % 5 === 0) {
  console.log("Buzz");
} else {
  console.log(num);
}
