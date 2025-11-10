// LINK: https://www.acmicpc.net/problem/10814

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);

const N = Number(input[0]);

const arr = [...input].splice(1).reduce<string[][]>((acc, cur, idx) => {
  if (idx % 2 === 1) return acc;

  acc.push([cur, input[idx + 2]]);
  return acc;
}, []);

arr.sort((a, b) => Number(a[0]) - Number(b[0]));

process.stdout.write(arr.join("\n").replace(/,/g, " "));
