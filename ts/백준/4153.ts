// LINK: https://www.acmicpc.net/problem/4153
import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let n = 0;
while (1) {
  const a = input[n * 3];
  const b = input[n * 3 + 1];
  const c = input[n * 3 + 2];

  if (a === 0 && b === 0 && c === 0) break;

  if (Math.pow(a, 2) === Math.pow(b, 2) + Math.pow(c, 2)) {
    console.log("right");
  } else if (Math.pow(b, 2) === Math.pow(c, 2) + Math.pow(a, 2)) {
    console.log("right");
  } else if (Math.pow(c, 2) === Math.pow(a, 2) + Math.pow(b, 2)) {
    console.log("right");
  } else {
    console.log("wrong");
  }

  n++;
}
