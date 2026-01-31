# Setup Instructions for Game Challenge 01

## For Students - First Time Setup

Follow these steps to set up your development environment:

### Option 1: Using Command Prompt (Recommended for Windows)

1. **Download and Install Python** (if you don't have it):
   - Go to https://www.python.org/downloads/
   - Download the latest Python version
   - **IMPORTANT**: During installation, check the box that says "Add Python to PATH"

2. **Open Command Prompt** in the game_challenge_01 folder:
   - Open File Explorer
   - Navigate to the game_challenge_01 folder
   - Right-click in the empty space
   - Click "Open in Terminal" (or "Open Command Window here")

3. **Run the setup script**:
   ```
   setup.bat
   ```

4. The script will:
   - Check if Python is installed
   - Create a virtual environment
   - Activate it automatically
   - Display setup completion message

---

### Option 2: Using PowerShell

1. **Download and Install Python** (if you don't have it):
   - Go to https://www.python.org/downloads/
   - Download the latest Python version
   - **IMPORTANT**: During installation, check the box that says "Add Python to PATH"

2. **Open PowerShell** in the game_challenge_01 folder:
   - Open File Explorer
   - Navigate to the game_challenge_01 folder
   - Right-click in the empty space
   - Click "Open in Terminal" (or use Ctrl+Shift+`)

3. **Allow script execution** (first time only):
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   Type `Y` and press Enter

4. **Run the setup script**:
   ```powershell
   .\setup.ps1
   ```

5. The script will:
   - Check if Python is installed
   - Create a virtual environment
   - Activate it automatically
   - Display setup completion message

---

## After Setup

### Configure VSCode

1. **Open the project folder in VSCode**
2. Press `Ctrl+Shift+P` to open the Command Palette
3. Search for and select: **Python: Select Interpreter**
4. Choose the interpreter that shows `(venv)` - this uses your virtual environment
5. VSCode will now use the correct Python environment for your project

### Running Your Code

Once setup is complete and VSCode is configured:

**Option 1 - Using VSCode (Easiest)**:
- Create or open your Python file (e.g., `game.py` or `main.py`)
- Click the "Run" button in the top right, or press `Ctrl+F5`

**Option 2 - Using Terminal**:
- Open a terminal in VSCode (Ctrl+`)
- The virtual environment should activate automatically
- Run: `python your_script.py`

---

## Validating Your Code

### Running the Code Validator

The `validate_code.py` script checks if your game implementation includes all mandatory features, optional features, and bonus tasks.

**How to run it**:

**Option 1 - Using VSCode**:
- Open the integrated terminal (Ctrl+`)
- Make sure your virtual environment is activated
- Run: `python validate_code.py`

**Option 2 - Using Command Prompt**:
```
venv\Scripts\activate.bat
python validate_code.py
```

**Option 3 - Using PowerShell**:
```powershell
.\venv\Scripts\Activate.ps1
python validate_code.py
```

### What the Validator Checks

The script will analyze your code and provide feedback on:

✅ **Mandatory Features**:
- Reading Pokemon and Medicine CSV files
- Storing data in lists
- Creating game state variables (score, number of questions)
- Implementing the `randomize()` function
- Creating player dialogue/menu system
- Implementing game logic and score tracking

🎯 **Optional Features**:
- Player can choose number of questions
- Player can enter their name
- Score resets between rounds

🏆 **Bonus Features**:
- Score saving/leaderboard system
- Showing Pokemon/Medicine information
- Multi-language support (Portuguese/English)

### Understanding the Output

When you run the validator, you'll see a report like:

```
MANDATORY FEATURES: 5/6 ✓
OPTIONAL FEATURES: 2/3 ✓
BONUS FEATURES: 1/3 ✓

Missing features:
- [ ] randomize() function not properly implemented
```

Use this feedback to identify what features you still need to implement!

---

## Troubleshooting

### "Python is not installed or not in PATH"
- Reinstall Python from https://www.python.org/downloads/
- **Make sure to check "Add Python to PATH"** during installation
- Restart Command Prompt/PowerShell after installing Python

### "Permission denied" in PowerShell
- Run PowerShell as Administrator
- Then run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Type `Y` and press Enter

### Virtual environment won't activate
- Make sure you're in the correct folder (game_challenge_01)
- Try manually activating it:
  - **Command Prompt**: `venv\Scripts\activate.bat`
  - **PowerShell**: `.\venv\Scripts\Activate.ps1`

### "pip is not available"
- You may need to reinstall Python with pip selected
- Or try: `python -m pip --version`

---

## Project Resources

- **Game Challenge Rules**: See README.md for complete game rules
- **Data Files**: 
  - `database/pokedex.csv` - List of Pokemon names
  - `database/medicine.csv` - List of medicine names

---

## Need Help?

If you encounter any issues:
1. Check the troubleshooting section above
2. Make sure Python is installed and added to PATH
3. Try running the setup script again
4. Ask your instructor for help
