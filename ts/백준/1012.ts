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
          const [n, m] = bfs.pop() as number[];

          if (m > M - 1 || m < 0 || n > N - 1 || n < 0) continue;

          if (map[n][m] === 1 && searched[n][m] === 0) {
            searched[n][m] = 1;
            bfs.push([n + 1, m]);
            bfs.push([n - 1, m]);
            bfs.push([n, m + 1]);
            bfs.push([n, m - 1]);
          }
        }
      }
    }
  }

  console.log(bugCount);
}
