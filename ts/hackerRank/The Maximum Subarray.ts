function maxSubarray(arr: number[]): number[] {
  const N = arr.length;
  const dp = new Array(N).fill(0);

  dp[0] = arr[0];
  let maxSum = arr[0];
  let highSum = arr[0];

  for (let i = 1; i < N; i++) {
    if (dp[i - 1] + arr[i] > arr[i]) {
      dp[i] = dp[i - 1] + arr[i];
    } else {
      dp[i] = arr[i];
    }

    if (highSum < 0) {
      highSum = Math.max(highSum, arr[i]);
    } else {
      if (arr[i] > 0) {
        highSum += arr[i];
      }
    }

    maxSum = Math.max(maxSum, dp[i]);
  }

  return [maxSum, highSum];
}

console.log(maxSubarray([1, 2, 3, 4]));
console.log(maxSubarray([2, -1, 2, 3, 4, -5]));
console.log(maxSubarray([2, -1, -1, -2, 3]));
console.log(maxSubarray([-2, -3, -1, -4, -6]));
console.log(maxSubarray([1]));
console.log(maxSubarray([-1, -2, -3, -4, -5, -6]));
console.log(maxSubarray([1, -2]));
console.log(maxSubarray([1, 2, 3]));
console.log(maxSubarray([-10]));
console.log(maxSubarray([1, -1, -1, -1, -1, 5]));
