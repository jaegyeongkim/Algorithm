// LINK: https://www.hackerrank.com/challenges/stockmax/problem
function stockmax(prices: number[]): number {
  // Write your code here
  const N = prices.length;
  let maxSum = 0;

  for (let i = 0; i < N; i++) {
    let maxDiff = 0;
    for (let j = i + 1; j < N; j++) {
      maxDiff = Math.max(maxDiff, prices[j] - prices[i]);
    }
    maxSum += maxDiff;
  }

  return maxSum;
}

console.log(stockmax([5, 3, 2]));
console.log(stockmax([1, 2, 100]));
console.log(stockmax([1, 3, 1, 2]));
