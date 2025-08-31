const test = (pnl: number[], k: number): number => {
  const N = pnl.length;

  let maxSum = 0;
  let cur = 0;
  const dp = Array.from({ length: N }, () => new Array(N).fill(0));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < i + 1; j++) {
      dp[i][j] = "1";
    }
  }

  return maxSum;
};

// console.log(test([4, 3, -2, 9, -4, 2, 7], 6));
// console.log(test([-7, -5, -8, -6, -7], 3));
console.log(test([1, 2, 3], 1));
