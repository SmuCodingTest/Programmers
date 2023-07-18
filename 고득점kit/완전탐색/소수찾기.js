function solution() {

function isPrime(num) {
    if (num < 2) {
      return false;
    }
  
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
  
    return true;
  }
  
  function findPrimePermutations(nums) {
    const result = [];
  
    function backtrack(nums, current) {
      if (current.length > 0 && isPrime(Number(current.join('')))) {
        result.push(Number(current.join('')));
      }
  
      for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
          continue; // 중복된 숫자는 건너뜁니다.
        }
        current.push(nums[i]);
        backtrack(nums, current);
        current.pop();
      }
    }
  
    nums.sort((a, b) => a - b); // 숫자 배열을 정렬합니다.
    backtrack(nums, []);
  
    return result;
  }
  
  // 예제 #1
  const nums1 = [1, 7];
  const primePermutations1 = findPrimePermutations(nums1);
  console.log(`예제 #1: ${primePermutations1}`);
  
  // 예제 #2
  const nums2 = [0, 1, 1];
  const primePermutations2 = findPrimePermutations(nums2);
  console.log(`예제 #2: ${primePermutations2}`);

}