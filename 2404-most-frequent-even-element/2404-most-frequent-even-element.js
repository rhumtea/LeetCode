/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function(nums) {
    let freq = new Map();
    let res = -1;
    let maxFreq = 0;
    for (let num of nums) {
        if (num%2 === 0) {
            let curFreq = (freq.get(num) || 0) + 1;
            freq.set(num, curFreq);
            if (curFreq > maxFreq || (curFreq === maxFreq && num < res)) {
                maxFreq = curFreq;
                res = num;
            }
        }
    }
    return res;
};