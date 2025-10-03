// https://www.acmicpc.net/problem/24266

import * as fs from "fs";

const n = BigInt(fs.readFileSync(0, "utf8").trim());

console.log((n * n * n).toString());
console.log(3);
