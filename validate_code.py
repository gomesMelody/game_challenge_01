import os
import re
from pathlib import Path

# ============================================
# VALIDATION SCRIPT FOR GAME CHALLENGE
# ============================================

class CodeValidator:
    def __init__(self, project_path='.'):
        self.project_path = project_path
        self.python_files = self.find_python_files()
        self.all_code = self.read_all_code()
        
        # Tracking results
        self.mandatory_features = {}
        self.optional_features = {}
        self.bonus_features = {}
        
    def find_python_files(self):
        """Find all Python files in the project"""
        python_files = []
        for root, dirs, files in os.walk(self.project_path):
            # Skip common directories
            dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'venv', 'env']]
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files
    
    def read_all_code(self):
        """Read all Python files and combine their contents"""
        all_code = ""
        for file_path in self.python_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    all_code += f"\n\n# FILE: {file_path}\n"
                    all_code += f.read()
            except Exception as e:
                print(f"Warning: Could not read {file_path}: {e}")
        return all_code
    
    def check_pattern(self, pattern, flags=re.IGNORECASE):
        """Check if a pattern exists in the code"""
        return bool(re.search(pattern, self.all_code, flags))
    
    def check_function_exists(self, function_name):
        """Check if a function is defined"""
        pattern = rf'def\s+{function_name}\s*\('
        return self.check_pattern(pattern)
    
    def check_class_exists(self, class_name):
        """Check if a class is defined"""
        pattern = rf'class\s+{class_name}\s*[:\(]'
        return self.check_pattern(pattern)
    
    def check_variable_exists(self, var_name):
        """Check if a variable is created/used"""
        pattern = rf'{var_name}\s*='
        return self.check_pattern(pattern)
    
    def check_file_reading(self):
        """Check if CSV files are being read"""
        patterns = [
            r'read_csv|pd\.read_csv|open.*csv|csv\.reader',
            r'pokedex|pokemon.*csv',
            r'medicine|medicin.*csv|remedi.*csv'
        ]
        csv_patterns_found = 0
        for pattern in patterns:
            if self.check_pattern(pattern):
                csv_patterns_found += 1
        return csv_patterns_found >= 2
    
    def check_list_storage(self):
        """Check if data is stored in lists"""
        patterns = [
            r'pokemons?\s*=\s*\[',
            r'pokemon.*list|pokemon.*\[\]',
            r'medicines?\s*=\s*\[',
            r'medicine.*list|medicine.*\[\]',
            r'\.append\(',
            r'\.tolist\('
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 3
    
    def check_variables_for_game_state(self):
        """Check if score and questions variables exist"""
        patterns = [
            r'score\s*=',
            r'point',
            r'question.*=\s*[0-9]|num.*question|num.*asked',
            r'round',
            r'player.*name|player.*score'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 3
    
    def check_randomize_function(self):
        """Check if randomize/random selection function exists"""
        patterns = [
            r'def\s+random\w*\(',
            r'random\.choice',
            r'random\.sample',
            r'random\.randint',
            r'choice.*pokemon|choice.*medicine'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 2
    
    def check_game_dialogue(self):
        """Check if there's user interaction/dialogue"""
        patterns = [
            r'input\s*\(',
            r'print\s*\(',
            r'question|guess|answer',
            r'correct|wrong|invalid'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 4
    
    def check_points_system(self):
        """Check if points system exists"""
        patterns = [
            r'score\s*\+=|score\s*=\s*score\s*\+',
            r'point.*\+=|point.*=.*point.*\+',
            r'accumulate|gain.*point',
            r'correct.*point|point.*correct'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 2
    
    def check_round_system(self):
        """Check if round system is implemented"""
        patterns = [
            r'for.*in.*range|while.*<|while.*>',
            r'round|iteration|question.*\d+',
            r'reset.*score|score.*=\s*0'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 2
    
    def check_display_score(self):
        """Check if final score is displayed"""
        patterns = [
            r'print.*score|display.*score|show.*score',
            r'print.*point|final.*score',
            r'print.*player.*score'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 1
    
    # ============= OPTIONAL FEATURES =============
    
    def check_custom_questions(self):
        """Check if player can choose number of questions"""
        patterns = [
            r'input.*question|input.*round|how.*many.*question',
            r'custom.*question|choose.*question|set.*question'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 1
    
    def check_player_name(self):
        """Check if player can enter their name"""
        patterns = [
            r'input.*name|enter.*name|player.*name',
            r'player.*=.*input|name.*=.*input'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 1
    
    def check_language_support(self):
        """Check if Portuguese/English support exists"""
        patterns = [
            r'pt|português|portuguese',
            r'en|english|inglês',
            r'language|idioma|lang.*choice|select.*language'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 2
    
    # ============= BONUS FEATURES =============
    
    def check_score_saving(self):
        """Check if scores are saved to file"""
        patterns = [
            r'write|save.*score|export',
            r'csv|json|database|file.*write',
            r'scores\.csv|ranking|leaderboard'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 2
    
    def check_ranking_display(self):
        """Check if ranking/leaderboard is displayed"""
        patterns = [
            r'ranking|leaderboard|top.*player|best.*player',
            r'sort.*score|display.*ranking|show.*ranking',
            r'ranking.*menu|view.*ranking'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 2
    
    def check_pokemon_info(self):
        """Check if Pokemon information feature exists"""
        patterns = [
            r'pokemon.*info|pokemon.*detail|pokemon.*search',
            r'search.*pokemon|display.*pokemon|show.*pokemon',
            r'pokemon.*menu|pokemon.*information'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 1
    
    def check_medicine_info(self):
        """Check if Medicine information feature exists"""
        patterns = [
            r'medicine.*info|medicine.*detail|medicine.*search|remedi.*search',
            r'search.*medicine|display.*medicine|show.*medicine|remedi',
            r'medicine.*menu|medicine.*information'
        ]
        found = sum(1 for pattern in patterns if self.check_pattern(pattern))
        return found >= 1
    
    def validate_all(self):
        """Run all validations"""
        print("\n" + "="*70)
        print("            GAME CHALLENGE VALIDATION REPORT")
        print("="*70)
        
        # ============= MANDATORY FEATURES =============
        print("\n📋 MANDATORY FEATURES:")
        print("-" * 70)
        
        self.mandatory_features['Load CSV files'] = self.check_file_reading()
        self.mandatory_features['Store data in lists'] = self.check_list_storage()
        self.mandatory_features['Game state variables'] = self.check_variables_for_game_state()
        self.mandatory_features['Randomize function'] = self.check_randomize_function()
        self.mandatory_features['Game dialogue/interaction'] = self.check_game_dialogue()
        self.mandatory_features['Points system'] = self.check_points_system()
        self.mandatory_features['Round system'] = self.check_round_system()
        self.mandatory_features['Display final score'] = self.check_display_score()
        
        passed = 0
        failed = 0
        for feature, status in self.mandatory_features.items():
            status_text = "✓ PASS" if status else "✗ FAIL"
            print(f"  {status_text} | {feature}")
            if status:
                passed += 1
            else:
                failed += 1
        
        mandatory_status = passed == len(self.mandatory_features)
        
        print("\n" + "-" * 70)
        if mandatory_status:
            print(f"✓ ALL MANDATORY FEATURES PASSED ({passed}/{len(self.mandatory_features)})")
        else:
            print(f"✗ MANDATORY FEATURES FAILED ({failed} missing)")
        
        # ============= OPTIONAL FEATURES =============
        print("\n🎯 OPTIONAL FEATURES:")
        print("-" * 70)
        
        self.optional_features['Custom question count'] = self.check_custom_questions()
        self.optional_features['Player name entry'] = self.check_player_name()
        self.optional_features['Portuguese/English support'] = self.check_language_support()
        
        optional_passed = 0
        for feature, status in self.optional_features.items():
            status_text = "✓ DONE" if status else "✗ NOT DONE"
            print(f"  {status_text} | {feature}")
            if status:
                optional_passed += 1
        
        print(f"\nOptional features: {optional_passed}/{len(self.optional_features)} implemented")
        
        # ============= BONUS FEATURES =============
        print("\n🏆 BONUS FEATURES:")
        print("-" * 70)
        
        self.bonus_features['Save scores to file'] = self.check_score_saving()
        self.bonus_features['Display ranking'] = self.check_ranking_display()
        self.bonus_features['Pokemon information viewer'] = self.check_pokemon_info()
        self.bonus_features['Medicine information viewer'] = self.check_medicine_info()
        
        bonus_passed = 0
        for feature, status in self.bonus_features.items():
            status_text = "✓ DONE" if status else "✗ NOT DONE"
            print(f"  {status_text} | {feature}")
            if status:
                bonus_passed += 1
        
        print(f"\nBonus features: {bonus_passed}/{len(self.bonus_features)} implemented")
        
        # ============= FINAL REPORT =============
        print("\n" + "="*70)
        print("                         FINAL REPORT")
        print("="*70)
        
        if mandatory_status:
            print("✓ STATUS: PASSED")
            print("\nYour implementation successfully covers all mandatory features!")
            print(f"\nOptional features completed: {optional_passed}/{len(self.optional_features)}")
            print(f"Bonus features completed: {bonus_passed}/{len(self.bonus_features)}")
        else:
            print("✗ STATUS: FAILED")
            print("\nThe following mandatory features are missing:")
            for feature, status in self.mandatory_features.items():
                if not status:
                    print(f"  • {feature}")
            print("\nPlease implement these features to pass the challenge.")
        
        print("\n" + "="*70 + "\n")
        
        return mandatory_status

if __name__ == '__main__':
    # Get project path
    import sys
    project_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    # Run validation
    validator = CodeValidator(project_path)
    result = validator.validate_all()
    
    # Exit with appropriate code
    sys.exit(0 if result else 1)