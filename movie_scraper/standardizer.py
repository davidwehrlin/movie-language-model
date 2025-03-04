import re
import string
from typing import List





class Standardizer:
    """
    Standardizes movie data to a consistent format.
    """
    @staticmethod
    def standardize_movie_script( lines: List[str]) -> List[str]:
        processed_lines = []
        for i in range(len(lines)):
            lines[i] = lines[i].strip()

            prev_line = lines[i - 1] if i > 0 else ""
            current_line = lines[i]
            next_line = lines[i + 1].strip() if i < len(lines) - 1 else ""

            if Standardizer.has_invalid_character(current_line):
                raise ValueError(f"Invalid character in script")
            
            current_line = Standardizer.remove_page_numbers(current_line)
            current_line = Standardizer.remove_special_script_strings(current_line)
            current_line = Standardizer.remove_line_with_only_special_chars(current_line)
            current_line = Standardizer.remove_empty_parentheses(current_line)

            if prev_line == "" and current_line == "" and next_line == "":
                continue
            lines[i] = current_line.strip()
        return processed_lines

    @staticmethod
    def has_invalid_character(line: str) -> bool:
        pattern = re.compile(r'[^a-zA-Z0-9`!@#$%^&*()_+|\-=\\{}\[\]:"";\'<>?,./]')
        if pattern.search(line):
            return True
        return False
    
    
    @staticmethod
    def has_some_lowercase(line: str) -> bool:
        lowercase_count = sum(1 for char in line if char.islower())
        return lowercase_count >= 3
    
    @staticmethod
    def has_mostly_lowercase(line: str) -> bool:
        uppercase_count = 0
        lowercase_count = 0
        for char in line:
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
        # Check if lowercase characters are more than twice the uppercase characters
        return lowercase_count > uppercase_count * 2
    
    @staticmethod
    def has_only_uppercase_and_special(line: str) -> bool:
        special_chars = string.punctuation + string.whitespace
        return all(c.isupper() or c in special_chars for c in s)
    
    @staticmethod
    def remove_page_numbers(line: str) -> str:
        # Remove page numbers from the beginning and end of the line
        line = re.sub(r'^(Page \d+ of \d+|\(?\d+[A-Z]?\)?\.?-?\)?\.?)\s*', '', line)  # Remove leading page numbers
        line = re.sub(r'\s*(Page \d+ of \d+|\(?\d+[A-Z]?\)?\.?-?\)?\.?)$', '', line)  # Remove trailing page numbers
        return line

    @staticmethod
    def remove_special_script_strings(line: str) -> str:
        special_strings = [
            "CONTINUED", "CONT'D", "cont'd", "CONTINUING", "CUT TO", "FADE IN", "CONTINUOUS", "MORE", "CUT TO’s",
            "DISSOLVE", "DISSOLVE OUT", "DISSOLVE IN", "FADE TO BLACK", "FADE FROM BLACK", "FADE OUT", "INSERT CUT",
            "INSERT SHOT", "MONTAGE"
        ]
        for special_string in special_strings:
            line = re.sub(re.escape(special_string) + r'[:\-]?', '', line, flags=re.IGNORECASE)
        return line.strip()
    
    @staticmethod
    def remove_line_with_only_special_chars(line: str) -> str:
        pattern = re.compile(r'^[\-_=@#\s]+$')
        return line if not pattern.match(line) else ""
    
    @staticmethod
    def remove_empty_parentheses(s):
        return re.sub(r"\(\s*\)", "", s)