const qwer = [1, 2, 3, 4];
const k = 2;

const N = qwer.length;
const dp = new Array(N).fill(0);

for (let i = 0; i < N; i++) {
  if (i < k) {
    dp[i] = qwer[i];
  } else {
    let minCost = Infinity;
    for (let j = 0; j < k; j++) {
      minCost = Math.min(minCost, dp[i - k + j]);
    }
    dp[i] = minCost + qwer[i];
  }

  console.log("dp", dp);
}

console.log(dp[dp.length - 1]);
