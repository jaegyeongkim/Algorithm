// LINK: https://www.acmicpc.net/problem/27866

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

// const input = ["Sprout", "3"];

const S = input[0].split("");
const i = Number(input[1]);

console.log(S[i - 1]);
