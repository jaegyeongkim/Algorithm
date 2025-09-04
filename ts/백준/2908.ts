// LINK: https://www.acmicpc.net/problem/2908

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);
// const input = ["734", "893"];
// const input = ["221", "231"];

const str1 = input[0];
const str2 = input[1];

let reverse1 = "";
let reverse2 = "";
for (let i = 2; i >= 0; i--) {
  reverse1 += str1[i];
  reverse2 += str2[i];
}

console.log(Math.max(Number(reverse1), Number(reverse2)));
