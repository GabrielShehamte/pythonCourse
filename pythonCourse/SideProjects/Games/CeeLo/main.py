import random
import streamlit as st
from setupGame import roll_dice, nonPair, hasPair, validRoll, determine_winner


def main():
    play = input("Do you want to play Cee-lo? (yes/y or no/n): ").strip().lower()

    if play in ["yes", "y"]:
        while True:
            player_roll = roll_dice()
            print("You rolled:", player_roll)
            st.write(f"Your Roll: {player_roll}")
            
            while not validRoll(player_roll):
                print("Your roll is not valid, rolling again...")
                player_roll = roll_dice()
                print("You rolled: ", player_roll)
                st.write(f"Your Roll: {player_roll}")

            # Roll until the system has a valid hand
            system_roll = []
            while True:
                system_roll = roll_dice()
                if validRoll(system_roll):
                    print("The system rolled:", system_roll)
                    st.write(f"System roll: {system_roll}")
                    break
            
            # Determine the winner after both have valid rolls
            result = determine_winner(player_roll, system_roll)
            print(result)

            # If the result indicates to roll again, loop back; otherwise, exit
            if "roll again" not in result.lower():
                break
    else:
        print("Maybe next time!")

if __name__ == "__main__":
    main()

st.title("Dice Game")
if st.button("Play"):
    main()
    
    # st.write(f"Your Roll: {player_roll}")
    # st.write(f"System Roll: {system_roll}")
    # st.write(f"Result: {result}")
 










