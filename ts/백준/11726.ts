// LINK: https://www.acmicpc.net/problem/11726

import * as fs from "fs";

const N = Number(fs.readFileSync(0, "utf8"));

const arr = [0, 1, 2];

if (N > 2) {
  for (let n = 3; n <= N; n++) {
    const result = (arr[n - 2] + arr[n - 1]) % 10007;
    arr.push(result);
  }
}

console.log(arr[N]);
