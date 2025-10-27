// LINK: https://www.acmicpc.net/problem/2775

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const T = input[0];
const arr = input.splice(1);

for (let i = 0; i < arr.length; i += 2) {
  const a = arr[i];
  const b = arr[i + 1];

  const result = Array.from({ length: a + 1 }, () =>
    Array.from({ length: b + 1 }, (_, j) => j)
  );

  for (let j = 1; j < a + 1; j++) {
    for (let k = 1; k <= b; k++) {
      result[j][k] = result[j - 1][k] + result[j][k - 1];
    }
  }
  console.log(result[a][b]);
}
