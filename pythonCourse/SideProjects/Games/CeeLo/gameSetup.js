export function rollDice() {
    return [Math.floor(Math.random() * 6) + 1, 
            Math.floor(Math.random() * 6) + 1, 
            Math.floor(Math.random() * 6) + 1];
}

export function evaluateHand(dice) {
    const sortedDice = [...dice].sort();
    
    if (sortedDice.toString() === [4, 5, 6].toString()) {
        return '4-5-6 (automatic win)';
    } else if (sortedDice.toString() === [1, 2, 3].toString()) {
        return '1-2-3 (automatic loss)';
    } else if (new Set(dice).size === 1) {
        return `Triple ${dice[0]}`;
    } else {
        return `High ${Math.max(...dice)}`;
    }
}
