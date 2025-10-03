// https://www.acmicpc.net/problem/24264

import * as fs from "fs";

const n = Number(fs.readFileSync(0, "utf8").trim().split(/\s+/));

console.log(Math.pow(n, 2));
console.log(2);
