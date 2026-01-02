// LINK: https://www.acmicpc.net/problem/17626

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8"));

const maxNum = Math.floor(Math.sqrt(N));
let minCount = 4;

for (let a = maxNum; a > 0; a--) {
  const A = Math.pow(a, 2);

  if (A === N) {
    minCount = 1;
    break;
  }

  for (let b = a; b > 0; b--) {
    const AB = A + Math.pow(b, 2);

    if (AB === N) {
      minCount = minCount > 2 ? 2 : minCount;
      break;
    } else if (AB > N) {
      continue;
    }

    for (let c = b; c > 0; c--) {
      const ABC = AB + Math.pow(c, 2);

      if (ABC === N) {
        minCount = minCount > 3 ? 3 : minCount;
        break;
      } else if (ABC > N) {
        continue;
      }
    }
  }
}
console.log(minCount);
