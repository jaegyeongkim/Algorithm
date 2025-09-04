// LINK: https://www.acmicpc.net/problem/10809

import * as fs from "fs";

const S = fs.readFileSync(0, "utf8");
// const S = "baekjoon";

const alphabet = {
  a: 0,
  b: 1,
  c: 2,
  d: 3,
  e: 4,
  f: 5,
  g: 6,
  h: 7,
  i: 8,
  j: 9,
  k: 10,
  l: 11,
  m: 12,
  n: 13,
  o: 14,
  p: 15,
  q: 16,
  r: 17,
  s: 18,
  t: 19,
  u: 20,
  v: 21,
  w: 22,
  x: 23,
  y: 24,
  z: 25,
} as const;
const arr = Array(26).fill(-1);

for (let i = 0; i < S.length; i++) {
  if (arr[alphabet[S[i] as keyof typeof alphabet]] === -1) {
    arr[alphabet[S[i] as keyof typeof alphabet]] = i;
  }
}

console.log(arr.join(" "));
