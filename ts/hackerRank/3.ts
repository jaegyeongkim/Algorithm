const qwe = (userEvent: number[]): number => {
  const N = userEvent.length;
  const maxNum = Math.max(...userEvent);
  const numberCounts = new Array(maxNum + 1).fill(Infinity);

  for (let i = 0; i < N; i++) {
    if (numberCounts[userEvent[i]] === Infinity) {
      numberCounts[userEvent[i]] = 0;
    }
    numberCounts[userEvent[i]] += 1;
  }

  const minCount = Math.min(...numberCounts);

  const countArray = new Array(maxNum + 1).fill(0);
  for (let i = 0; i < N; i++) {
    if (countArray[userEvent[i]] !== minCount) {
      countArray[userEvent[i]] = minCount;
    }
  }

  let maxLength = 0;

  for (let i = 0; i < N; i++) {
    const arr: number[] = [];
    const copyCount = [...countArray];
    for (let j = i; j < N; j++) {
      copyCount[userEvent[j]] -= 1;
      if (copyCount[userEvent[j]] < 0) break;
      arr.push(userEvent[j]);
    }
    maxLength = Math.max(maxLength, arr.length);
  }

  return maxLength;
};

console.log(qwe([9, 8, 5, 9, 2]));
