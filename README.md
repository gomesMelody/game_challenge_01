# GAME CHALLENGE 01

## Objective
Create a simple game to play **Pokemon or Medicine!**

---

## Challenge Rules
- You can use AI to help with development
- All mandatory functions of the game must be implemented

---

## Game Rules
- Each round has **5 questions**
- The player must guess if the displayed name is a **Pokemon** or a **Medicine**
- For each correct answer, the player earns **1 point**
- At the end of the round, the game must display how many points the player accumulated and reset the score

---

## Optional Features
- The player can choose **how many questions** are in the round
- The player can enter their **name** to appear in the final Score

---

## Bonus Tasks
- The Score can be **saved** to display a **Ranking** of players who have played before
- The player can have the option to see more information about **Pokemons** or **Medicines**
- The player can have the option to see the game dialogues in both Portuguese and English (the medicine names are in Portuguese)

---

## Step-by-Step
- Read the source files and store them in lists
- Create variables to store the player's score and the number of questions per round
- Create a `randomize()` function that takes the two lists and returns the name of a Pokemon or a Medicine randomly (you can use a random lib)
- Create a dialogue with the player (the person running your script), using the game instructions
---

## EXAMPLE

With all the optional and Bonus tasks implemented, the Menu should look like this:

```text
============================================================
        WELCOME TO POKÉMON OR MEDICINE GAME!
============================================================
1. Play
2. View Pokemon information
3. View Medicine information
4. View Ranking
5. Change language
6. Exit
```