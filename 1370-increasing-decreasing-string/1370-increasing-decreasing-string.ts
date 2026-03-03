function sortString(s: string): string {
    const counts: number[] = new Array(26).fill(0);
    const res: string[] = [];
    const charCodeA = 'a'.charCodeAt(0);

    for (let i = 0; i <= s.length; i++) {
        counts[s.charCodeAt(i) - charCodeA]++;
    }

    while (res.length < s.length) {
        for (let i = 0; i < 26; i++) {
            if (counts[i] > 0) {
            res.push(String.fromCharCode(i + charCodeA));
            counts[i]--;
            }
        }

        for (let i = 25; i >= 0; i--) {
            if (counts[i] > 0) {
                res.push(String.fromCharCode(i + charCodeA));
                counts[i]--;
            }
        }
    }
    return res.join('');
};