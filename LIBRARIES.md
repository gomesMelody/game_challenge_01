# Python Libraries Guide for Game Challenge 01

This document explains the Python libraries used in this project and how they can help you build your Pokemon or Medicine game.

---

## Required Libraries

### 1. **pandas** ⭐
**Purpose**: Read and manipulate data from CSV files

**Why we use it**:
- Your game uses `pokedex.csv` and `medicine.csv` files in the `database/` folder
- Pandas makes it easy to load these CSV files and extract the data

**How to use it**:
```python
import pandas as pd

# Read a CSV file
pokemon_df = pd.read_csv('database/pokedex.csv')

# Get a list of all Pokemon names
pokemon_names = pokemon_df['name'].tolist()  # Assuming there's a 'name' column

# Get specific rows or columns
print(pokemon_df.head())  # Show first 5 rows
print(pokemon_df.columns)  # Show all column names
```

**Useful methods**:
- `pd.read_csv()` - Load CSV files
- `.head()` - View first few rows
- `.shape` - Get number of rows and columns
- `.columns` - See column names
- `.tolist()` - Convert a column to a Python list
- `.sample()` - Get random rows (useful for your game!)

**Example for your game**:
```python
import pandas as pd
import random

# Load the data
pokemon_df = pd.read_csv('database/pokedex.csv')
medicine_df = pd.read_csv('database/medicine.csv')

pokemon_list = pokemon_df['name'].tolist()
medicine_list = medicine_df['name'].tolist()

# Randomly select one item
random_item = random.choice(pokemon_list + medicine_list)
print(f"Is '{random_item}' a Pokemon or Medicine?")
```

**Learn more**: https://pandas.pydata.org/

---

### 2. **requests** 🌐
**Purpose**: Fetch data from the internet/APIs

**Why we use it**:
- Great for bonus features! You could fetch additional Pokemon info from the PokeAPI
- Get real-time data without hardcoding information

**How to use it**:
```python
import requests

# Fetch data from an API
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
data = response.json()  # Convert to dictionary

print(data['name'])  # Access properties
print(data['height'])
print(data['weight'])
```

**Common methods**:
- `requests.get()` - Fetch data from a URL
- `.json()` - Convert response to Python dictionary
- `.status_code` - Check if request was successful (200 = success)

**Example for your game (Bonus Feature)**:
```python
import requests

def get_pokemon_info(name):
    """Fetch Pokemon info from PokeAPI"""
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

# Use it to show extra details about a Pokemon
pokemon_data = get_pokemon_info('pikachu')
if pokemon_data:
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")
```

**Bonus**: Combine this with your game to show Pokemon details when players guess correctly!

**Learn more**: https://requests.readthedocs.io/

---

### 3. **numpy** 📊
**Purpose**: Numerical computing and array operations

**Why we use it**:
- Fast mathematical operations
- Handle arrays and large datasets efficiently
- Useful for statistics (calculating average scores, etc.)

**How to use it**:
```python
import numpy as np

# Create arrays
scores = np.array([10, 15, 8, 12, 9])

# Useful operations
print(np.mean(scores))    # Average score
print(np.max(scores))     # Highest score
print(np.min(scores))     # Lowest score
print(np.sum(scores))     # Total points
print(np.std(scores))     # Standard deviation (variation)
```

**Useful functions**:
- `np.array()` - Create an array
- `np.mean()` - Calculate average
- `np.max()` / `np.min()` - Find highest/lowest values
- `np.sum()` - Add all values
- `np.random.choice()` - Random selection from array

**Example for your game (Bonus Feature)**:
```python
import numpy as np

# Track player scores across multiple games
scores = np.array([10, 8, 15, 12, 14])

print(f"Average Score: {np.mean(scores):.2f}")
print(f"Best Score: {np.max(scores)}")
print(f"Total Points: {np.sum(scores)}")

# Show statistics
print(f"You've earned {np.sum(scores)} points across {len(scores)} games!")
```

**Learn more**: https://numpy.org/

---

## Standard Library (Already Installed - No pip needed)

### **random** 🎲
**Purpose**: Generate random numbers and selections

**Why we use it**:
- Core to your game - randomly select Pokemon/Medicine names
- Already included with Python, no installation needed!

**How to use it**:
```python
import random

# Random selection
item = random.choice(['pikachu', 'aspirin', 'charmander'])

# Random number
num = random.randint(1, 5)  # Random integer between 1-5

# Shuffle a list
names = ['pikachu', 'aspirin', 'charmander']
random.shuffle(names)  # Shuffles in place
```

**Useful functions**:
- `random.choice()` - Pick one random item from a list ⭐ (main use for your game)
- `random.randint(a, b)` - Random integer between a and b
- `random.shuffle()` - Randomly reorder a list
- `random.sample()` - Pick multiple random items without repeating

**Example for your game**:
```python
import random

def randomize(pokemon_list, medicine_list):
    """Return a random Pokemon or Medicine name"""
    all_items = pokemon_list + medicine_list
    return random.choice(all_items)

# Test it
pokemon = ['pikachu', 'charmander', 'squirtle']
medicine = ['aspirin', 'ibuprofen', 'acetaminophen']
selected = randomize(pokemon, medicine)
print(f"Is '{selected}' a Pokemon or Medicine?")
```

**Learn more**: https://docs.python.org/3/library/random.html

---

## CSV (Standard Library) 📄
**Purpose**: Read/write CSV files without pandas (if you prefer simpler approach)

**How to use it**:
```python
import csv

# Read a CSV file
with open('database/pokedex.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        pokemon_name = row[0]  # First column
        print(pokemon_name)
```

**Note**: For this project, **pandas is recommended** because it's more powerful and easier to use with CSV files.

---

## Installation & Setup

All required libraries will be installed automatically when you run the setup script:

```bash
setup.bat          # For Command Prompt
.\setup.ps1        # For PowerShell
```

Or manually install them:
```bash
pip install -r requirements.txt
```

---

## Which Libraries Should I Use?

### For Basic Game (Mandatory Features)
- `random` - Select random Pokemon/Medicine ✅
- `csv` (standard library) - Read CSV files

### For Better Game (Using Pandas)
- `pandas` - Cleaner way to read and handle CSV data
- `random` - Select random items

### For Advanced Features (Bonus Tasks)
- `pandas` - Manage player rankings/scores
- `requests` - Fetch additional Pokemon info from PokeAPI
- `numpy` - Calculate statistics for leaderboards

---

## Quick Start Example

Here's a complete example combining these libraries:

```python
import pandas as pd
import random
import numpy as np
from datetime import datetime

# Load data
pokemon_df = pd.read_csv('database/pokedex.csv')
medicine_df = pd.read_csv('database/medicine.csv')

pokemon_list = pokemon_df['name'].tolist()
medicine_list = medicine_df['name'].tolist()

def play_game(num_questions=5):
    """Play one round of the game"""
    scores = []
    
    for i in range(num_questions):
        # Select random item
        item = random.choice(pokemon_list + medicine_list)
        
        # Get user answer
        answer = input(f"Is '{item}' a Pokemon or Medicine? (p/m): ").lower()
        
        # Check answer
        is_correct = (item in pokemon_list and answer == 'p') or \
                     (item in medicine_list and answer == 'm')
        
        if is_correct:
            scores.append(1)
            print("Correct! ✓")
        else:
            print("Wrong! ✗")
    
    # Show statistics
    print(f"\nYour Score: {np.sum(scores)}/{num_questions}")
    print(f"Accuracy: {(np.mean(scores)*100):.1f}%")

# Run the game
if __name__ == "__main__":
    play_game()
```

---

## Troubleshooting

**"ModuleNotFoundError: No module named 'pandas'"**
- Run: `pip install -r requirements.txt`
- Or: `pip install pandas requests numpy`

**Installation slow or failing?**
- Make sure your internet connection is working
- Try: `pip install --upgrade pip`
- Then retry: `pip install -r requirements.txt`

---

## Resources & Documentation

- **Pandas**: https://pandas.pydata.org/docs/
- **Requests**: https://requests.readthedocs.io/
- **NumPy**: https://numpy.org/doc/
- **Python Random**: https://docs.python.org/3/library/random.html
- **PokeAPI** (for bonus features): https://pokeapi.co/

---

Happy coding! 🐍✨
