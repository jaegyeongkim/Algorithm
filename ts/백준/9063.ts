// https://www.acmicpc.net/problem/9063
import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = input.splice(1);

let maxX = -Infinity;
let maxY = -Infinity;
let minX = Infinity;
let minY = Infinity;

for (let i = 0; i < N; i++) {
  const x = arr[i * 2];
  const y = arr[i * 2 + 1];

  maxX = Math.max(maxX, x);
  maxY = Math.max(maxY, y);
  minX = Math.min(minX, x);
  minY = Math.min(minY, y);
}

console.log((maxX - minX) * (maxY - minY));
