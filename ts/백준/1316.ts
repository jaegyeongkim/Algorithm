// LINK: https://www.acmicpc.net/problem/1316

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);
// const input = ["3", "happy", "new", "year"];
// const input = ["4", "aba", "abab", "abcabc", "a"];
// const input = ["5", "ab", "aa", "aca", "ba", "bb"];
// const input = ["2", "yzyzy", "zyzyz"];
// const input = ["1", "z"];
// const input = [
//   "9",
//   "aaa",
//   "aaazbz",
//   "babb",
//   "aazz",
//   "azbz",
//   "aabbaa",
//   "abacc",
//   "aba",
//   "zzaz",
// ];

const N = Number(input[0]);
let count = 0;

for (let i = 1; i < N + 1; i++) {
  const letter = input[i];
  const alpha = {
    a: 0,
    b: 0,
    c: 0,
    d: 0,
    e: 0,
    f: 0,
    g: 0,
    h: 0,
    i: 0,
    j: 0,
    k: 0,
    l: 0,
    m: 0,
    n: 0,
    o: 0,
    p: 0,
    q: 0,
    r: 0,
    s: 0,
    t: 0,
    u: 0,
    v: 0,
    w: 0,
    x: 0,
    y: 0,
    z: 0,
  };

  let beforeStr = letter[0] as keyof typeof alpha;
  let isContinue = true;

  for (let j = 1; j < letter.length; j++) {
    if (!isContinue) break;

    const str = letter[j] as keyof typeof alpha;
    if (alpha[str] === 1) {
      isContinue = false;
      break;
    }

    if (beforeStr !== str) {
      if (alpha[beforeStr] === 0) {
        alpha[beforeStr] = 1;
      } else {
        isContinue = false;
      }
      beforeStr = str;
    }
  }

  if (isContinue) count += 1;
}

console.log(count);
