// LINK: https://www.acmicpc.net/problem/11718

import * as fs from "fs";

// const input = `Hello
// Baekjoon
// Online Judge `;

fs.readFileSync(0, "utf8")
  .split(/\n/)
  .map(String)
  .forEach((str: string) => {
    console.log(str);
  });

// input
//   .split(/\n/)
//   .map(String)
//   .forEach((str: string) => {
//     console.log(str);
//   });
