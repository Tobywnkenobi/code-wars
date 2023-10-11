function countBits(n: number): number {
    return n.toString(2).split('').reduce((count, bit) => count + (bit === '1' ? 1 : 0), 0);
}

console.log(countBits(1234));