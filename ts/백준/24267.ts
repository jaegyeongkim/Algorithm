// https://www.acmicpc.net/problem/24267

import * as fs from "fs";

const n = BigInt(fs.readFileSync(0, "utf8").trim());

const result = (n * (n - BigInt(1)) * (n - BigInt(2))) / BigInt(6);

console.log(result.toString());
console.log(3);
