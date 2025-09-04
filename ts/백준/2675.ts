// LINK: https://www.acmicpc.net/problem/2675

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);

// const input = ["2", "3", "ABC", "5", "/HTP"];

const T = Number(input[0]);

for (let i = 1; i < T + 1; i++) {
  const R = Number(input[i * 2 - 1]);
  const S = input[i * 2];

  let str = "";

  for (let j = 0; j < S.length; j++) {
    for (let k = 0; k < R; k++) {
      str += S[j];
    }
  }
  console.log(str);
}
