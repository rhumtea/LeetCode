function countLargestGroup(n: number): number {
    const getSum = (m : number) : number => {
        let sum = 0;
        while (m > 0) {
            sum += m%10;
            m = Math.floor(m/10);   
        }
        return sum;
    }

    const groups = new Map<number, number>();
    let maxCount = 0;
    for (let i = 1; i <= n; i ++) {
        const sum = getSum(i);
        const curCount = (groups.get(sum) || 0) + 1;
        groups.set(sum, curCount);
        if (curCount > maxCount) {
            maxCount = curCount;
        }
    }
    let res = 0;
    for (const count of groups.values()) {
        if (count === maxCount) {
            res++;
        }
    }
    return res;
};