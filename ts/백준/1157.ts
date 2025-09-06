// LINK: https://www.acmicpc.net/problem/1157

import * as fs from "fs";

const letter = fs.readFileSync(0, "utf8").trim();
// const letter = "Mississipi";
// const letter = "zZa";
// const letter = "z";
// const letter = "baaa";

const N = letter.length;

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

let maxCount = 0;
let maxLtter = "";

for (let i = 0; i < N; i++) {
  let count = alpha[letter[i].toLocaleLowerCase() as keyof typeof alpha];
  if (count > Math.floor(N / 2)) break;
  count += 1;

  alpha[letter[i].toLocaleLowerCase() as keyof typeof alpha] = count;
  if (maxCount < count) {
    maxLtter = letter[i].toLocaleUpperCase();
    maxCount = count;
  } else if (maxCount === count) {
    maxLtter = "?";
  }
}

console.log(maxLtter);
