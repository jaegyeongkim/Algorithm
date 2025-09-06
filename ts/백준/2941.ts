// LINK: https://www.acmicpc.net/problem/2941

import * as fs from "fs";

const letter = fs.readFileSync(0, "utf8").trim();
// const letter = "ljes=njak";
// const letter = "ddz=z=";
// const letter = "nljj";
// const letter = "c=c=";
// const letter = "dz=ak";

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
  "c=": 0,
  "c-": 0,
  "dz=": 0,
  "d-": 0,
  lj: 0,
  nj: 0,
  "s=": 0,
  "z=": 0,
};

let maxCount = 0;

const counter = (letter: keyof typeof alpha): boolean => {
  const count = alpha[letter];
  if (count !== undefined) {
    maxCount += 1;
    return true;
  } else {
    return false;
  }
};

for (let i = 0; i < letter.length; i++) {
  const three = letter[i] + letter[i + 1] + letter[i + 2];
  const two = letter[i] + letter[i + 1];
  const one = letter[i];

  if (counter(three as keyof typeof alpha)) {
    i += 2;
  } else if (counter(two as keyof typeof alpha)) {
    i += 1;
  } else {
    counter(one as keyof typeof alpha);
  }
}
console.log(maxCount);
