import random
import streamlit as st

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def nonPair(dice):
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1
    for die, count in counts.items():
        if count == 1:
            return die
    return None

def hasPair(dice):
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1
    return any(count == 2 for count in counts.values())

def validRoll(dice):
    return hasPair(dice) or dice == [1, 2, 3] or len(set(dice)) == 1 or sorted(dice) == [4, 5, 6]

def determine_winner(player_roll, system_roll):
    player_set = sorted(player_roll)
    system_set = sorted(system_roll)

    # Check for automatic win (4-5-6)
    if player_set == [4, 5, 6]:
        st.write("You won automatically; 4-5-6")
        return "You win with 4-5-6 (automatic win)!"
    if system_set == [4, 5, 6]:
        st.write("System won automatically; 4-5-6")
        return "The system wins with 4-5-6 (automatic win)!"

    # Check for triples
    if player_set[0] == player_set[1] == player_set[2]:
        if system_set[0] == system_set[1] == system_set[2]:
            if player_set[0] > system_set[0]:
                st.write("You won with higher triples")
                return "You win with higher triples!"
            elif player_set[0] < system_set[0]:
                st.write("The system wins with higher triples!")
                return "The system wins with higher triples!"
            else:
                return "It's a tie with triples! Roll again."

    # Check for pairs
    player_pair = hasPair(player_set)
    system_pair = hasPair(system_set)

    if player_set == [1, 2, 3]:
        st.write("You lose automatically")
        return "You lose automatically!"
    if system_set == [1, 2, 3]:
        st.write("You lose automatically")
        return "The system loses automatically!"

    if player_pair and system_pair:
        player_nPair = nonPair(player_set)
        system_nPair = nonPair(system_set)

       # if player_nPair is not None and system_nPair is not None:
        if player_nPair > system_nPair:
            st.write(f"The System wins with a higher non-pair {player_nPair}")
            return f"You win with the higher non-pair, {player_nPair}!"
        elif player_nPair < system_nPair:
            st.write(f"The System wins with a higher non-pair {system_nPair}")
            return f"The system wins with the higher non-pair!, {system_nPair}"
            
        else:
            return "Equal pairs, roll again!"

    elif player_pair:
        return "You win with a pair!"
    elif system_pair:
        return "The system wins with a pair!"

    else: return "No pairs, both roll again!"
 
 
 
