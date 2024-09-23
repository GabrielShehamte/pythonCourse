import {rollDice, evaluateHand} from './gameSetup.js'


function playCeeLo() {
    let player1Dice, player2Dice, player1Hand, player2Hand;
    
    while (true) {
        player1Dice = rollDice();
        player2Dice = rollDice();

        console.log("Player 1 Dice:", player1Dice)
        
        player1Hand = evaluateHand(player1Dice);
        player2Hand = evaluateHand(player2Dice);

        const result = document.getElementById("result");
        result.innerHTML = `
            Player 1 rolled: ${player1Dice.join(', ')} -> ${player1Hand}<br>
            Player 2 rolled: ${player2Dice.join(', ')} -> ${player2Hand}<br>
        `;

        // Determine the winner
        if (player1Hand === '4-5-6 (automatic win)') {
            return result.innerHTML += `Player 1 wins automatically with a hand of ${player1Hand}!`;
            break;
        } else if (player2Hand === '4-5-6 (automatic win)') {
            return result.innerHTML += `Player 2 wins automatically with a hand of ${player2Hand}!`;
            break;
        } else if (player1Hand === '1-2-3 (automatic loss)') {
            return result.innerHTML += `Player 2 wins with a hand of ${player2Hand}!`;
            break;
        } else if (player2Hand === '1-2-3 (automatic loss)') {
            return result.innerHTML += `Player 1 wins with a hand of ${player1Hand}!`;
            break;
        } else {
            if (player1Hand.includes('Triple') && player2Hand.includes('Triple')) {
                if (player1Dice[0] > player2Dice[0]) {
                    result.innerHTML += `Player 1 wins with a higher triple: ${player1Hand}!`;
                    break;
                } else if (player1Dice[0] < player2Dice[0]) {
                    result.innerHTML += `Player 2 wins with a higher triple: ${player2Hand}!`;
                    break;
                } else {
                    result.innerHTML += "It's a tie! Rolling again...";
                }
            } else {
                const player1High = parseInt(player1Hand.split(' ').pop());
                const player2High = parseInt(player2Hand.split(' ').pop());
                if (player1High > player2High) {
                    result.innerHTML += `Player 1 wins with a higher hand: ${player1Hand}!`;
                    break;
                } else if (player1High < player2High) {
                    result.innerHTML += `Player 2 wins with a higher hand: ${player2Hand}!`;
                    break;
                } else {
                    result.innerHTML += "It's a tie! Rolling again...";
                }
            }
        }
    }
}

document.getElementById("rollButton").addEventListener("click", playCeeLo);
