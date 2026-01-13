// LINK: https://www.acmicpc.net/problem/2630

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n");

let N = Number(input[0]);
const origin = input.slice(1).map((str) => str.split(" ").map(Number));

let whiteCount = 0;
let blueCount = 0;

let seperates: number[][][] = [origin];

while (1) {
  if (N === 1) break;
  const n = N / 2;

  const part: number[][][] = [];

  seperates.forEach((seperate) => {
    for (let i = 0; i < N; i += n) {
      for (let j = 0; j < N; j += n) {
        const abc: number[][] = [];
        let isSame = 1;
        const firstNum = seperate[i][j];

        for (let r = i; r < i + n; r++) {
          const row = [];
          for (let c = j; c < j + n; c++) {
            if (firstNum !== seperate[r][c]) {
              isSame = 0;
            }
            row.push(seperate[r][c]);
          }
          abc.push(row);
        }

        if (isSame) {
          if (firstNum === 0) {
            whiteCount++;
          } else {
            blueCount++;
          }
        } else {
          part.push(abc);
        }
      }
    }
  });

  seperates = part;

  N = n;
}

console.log(whiteCount, blueCount);
