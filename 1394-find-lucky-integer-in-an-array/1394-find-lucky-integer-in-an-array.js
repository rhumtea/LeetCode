/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    let freq = new Map();
    let luckyNum = -1;
    for (let x of arr) {
        let curFreq = (freq.get(x) || 0) + 1;
        freq.set(x, curFreq)
    }
    for (let [key, value] of freq) {
        if (key === value) {
            luckyNum = Math.max(luckyNum, key)
        }
    }
    return luckyNum;
};