import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [5, 7, 3, 8, 8, 1, 0, 2, 7, 4, 4, 4, 5, 2, 6, 5];

const N = input[0];

const arr = Array.from({ length: N }, () => new Array(N).fill(0));
const dp = Array.from({ length: N }, () => new Array(N).fill(0));

let count = 1;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (j > i) {
      arr[i][j] = 0;
      continue;
    }
    arr[i][j] = input[count];
    count += 1;
  }
}
dp[0][0] = arr[0][0];

for (let i = 1; i < N; i++) {
  for (let j = 0; j <= i; j++) {
    if (j === 0) {
      dp[i][j] = dp[i - 1][j] + arr[i][j];
    } else if (j === i) {
      dp[i][j] = dp[i - 1][j - 1] + arr[i][j];
    } else {
      dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j];
    }
  }
}

console.log(Math.max(...dp[N - 1]));
