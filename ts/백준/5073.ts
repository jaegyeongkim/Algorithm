// https://www.acmicpc.net/problem/5073

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

for (let i = 0; i < input.length; i += 3) {
  const a1 = input[i];
  const a2 = input[i + 1];
  const a3 = input[i + 2];

  if (a1 === 0 && a2 === 0 && a3 === 0) {
    continue;
  } else if (a1 + a2 <= a3 || a2 + a3 <= a1 || a3 + a1 <= a2) {
    console.log("Invalid");
  } else if (a1 === a2 && a2 === a3 && a3 === a1) {
    console.log("Equilateral");
  } else if (a1 === a2 || a2 === a3 || a3 === a1) {
    console.log("Isosceles");
  } else {
    console.log("Scalene");
  }
}
