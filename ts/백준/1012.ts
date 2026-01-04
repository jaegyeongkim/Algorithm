// LINK: https://www.acmicpc.net/problem/1012

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

const T = Number(input[0]);

let i = 1;
for (let t = 0; t < T; t++) {
  const [M, N, K] = input[i].split(" ").map(Number);
  const arr = input.slice(i + 1, i + 1 + K);
  i += 1 + K;

  const map = Array.from({ length: N }, () => new Array(M).fill(0));
  const searched = Array.from({ length: N }, () => new Array(M).fill(0));
  arr.forEach((spot) => {
    const [x, y] = spot.split(" ").map(Number);
    map[y][x] = 1;
  });

  let bugCount = 0;

  for (let x = 0; x < N; x++) {
    for (let y = 0; y < M; y++) {
      if (map[x][y] === 1 && searched[x][y] === 0) {
        bugCount++;
        searched[x][y] = 1;

        let bfs = [
          [x + 1, y],
          [x - 1, y],
          [x, y + 1],
          [x, y - 1],
        ];

        while (bfs.length) {
          const [m, n] = bfs.pop() as number[];

          if (m > N || m < 0 || n > M || n < 0) continue;

          if (map[m][n] === 1 && searched[m][n] === 0) {
            searched[m][n] = 1;
            bfs.push([m + 1, n]);
            bfs.push([m - 1, n]);
            bfs.push([m, n + 1]);
            bfs.push([m, n - 1]);
          }
        }
      }
    }
  }

  console.log(bugCount);
}
