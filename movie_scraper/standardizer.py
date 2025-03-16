import re
import string
from typing import List





class Standardizer:
    """
    Standardizes movie data to a consistent format.
    """
    @staticmethod
    def standardize_movie_script(lines: List[str]) -> List[str]:
        for i in range(len(lines)):
            current_line = lines[i]
            maybe_invalid_char = Standardizer.has_invalid_character(current_line)
            if maybe_invalid_char != None:
                raise ValueError(f"Invalid character in script: {ord(maybe_invalid_char)}")
            current_line = Standardizer.remove_special_script_strings(current_line)
            current_line = Standardizer.remove_revision_lines(current_line)
            current_line = Standardizer.remove_dates(current_line)
            current_line = Standardizer.remove_page_numbers(current_line)
            current_line = Standardizer.remove_line_with_only_special_chars(current_line)
            current_line = Standardizer.remove_empty_parentheses(current_line)
            current_line = current_line.strip()

            lines[i] = current_line

        lines = Standardizer.remove_start_and_end_empty_lines(lines)
        return Standardizer.manage_empty_lines(lines)

    @staticmethod
    def has_invalid_character(line: str) -> bool:
        for char in line:
            if char not in ''.join(chr(i) for i in range(256)):
                return char
        return None
    
    
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
        if line == "":
            return False
        special_chars = string.punctuation + string.whitespace
        return all(c.isupper() or c in special_chars for c in line)
    
    @staticmethod
    def remove_page_numbers(line: str) -> str:
        # Remove page numbers from the beginning and end of the line
        isMostlyLower = Standardizer.has_mostly_lowercase(line)
        charIntPattern = r'(([A-Z]{1,2}\d+)|(\d+(?!ST|ND|RD|TH|AM|PM)[A-Z]{1,2}))'
        complexPattern = Standardizer.build_regex_pattern(charIntPattern, isMostlyLower)
        simplePattern = Standardizer.build_regex_pattern(r'\d+', isMostlyLower)
        line = re.sub(r"^([Pp]age [A-Z]*\d+[A-Z]*\.? of [A-Z]*\d+[A-Z]*\.?|[A-Z]*\d+[A-Z]*\.? [Tt]hrough [A-Z]*\d+[A-Z]*\.?)", '', line)
        line = re.sub(complexPattern, '', line)  # Remove leading page numbers
        line = re.sub(simplePattern, '', line)  # Remove trailing page numbers
        return line
    
    @staticmethod
    def build_regex_pattern(innerPattern: str, isMostlyLower: bool) -> str:
        # Covers case where inner pattern is surrounded by () has - or .
        pattern = fr'(\(?{innerPattern}\)?\.?-?)'
        if isMostlyLower:
            pattern = r'[^\s{2,}\t+]' + pattern + r'(\s{2,}|\t+|$)'
        else:
            pattern = r'(^|\s+|\t+)' + pattern + r'(\s+|\t+|$)'
        return pattern

    @staticmethod
    def remove_special_script_strings(line: str) -> str:
        special_strings = [
            "BACK TO SCRIPT", "BACK TO SCREEN", "BACK TO STORY", "BACK TO SCENE", "BACK TO FILM", "BACK TO MOVIE",
            "BACK TO PICTURE", "TITLE SEQUENCE", "OPENING CREDITS", "END CREDITS", "CREDIT SEQUENCE", "CREDIT ROLL",
            "PULL BACK WIDER", "FADE FROM BLACK", "DISSOLVE OUT", "DISSOLVE IN", "DISSOLVE TO", "FADE TO BLACK", 
            "CUT TO BLACK", "CUT FROM BLACK", "BLACK SCREEN", "INSERT SHOT", "INSERT CUT", "INTO FRAME", "ANGLE ON", 
            "CUT BACK AND FORTH", "CUT BACK TO", "CUT TO’s", "CUT TO", "FADE IN", "FADE OUT", "SUPERIMPOSED", 
            "SUPERIMPOSE", "SUPER", "CONTINUING", "CONTINUOUS", "CONTINUED", "CONT'D", "cont'd", "DISSOLVE", 
            "MONTAGE", "UNTITLED", "OMITTED", "RESUMING", "RESUMES", "RESUME", "OMITTING", "OMITS", "(OMIT)", 
            "OMIT", "THEN", "MORE", "TITLE CARD", "TITLES", "TITLE", "DELETED", "(Deleted)", "STUDIO"
        ]
        for special_string in special_strings:
            line = re.sub(fr"\(?{special_string}\)?[:\-]?", '', line)
        line = re.sub(r'CONTINUED:?\s*\(\d+\)', ' ', line) # Remove CONTINUED with page numbers
        return line.strip()
    
    @staticmethod
    def remove_revision_lines(line: str) -> str:
        revision_strings = [
            r"REVISION", r"Revisions", r"Revision", r"Revised", r'((Rev\.|REV\.)(\s*\(?\d+))'
        ]
        pattern = re.compile(r'|'.join(revision_strings))
        return line if not pattern.match(line) else ""

    @staticmethod
    def remove_line_with_only_special_chars(line: str) -> str:
        pattern = re.compile(r'^[\-_=@#\s/\(\)]+$')
        return line if not pattern.match(line) else ""
    
    @staticmethod
    def remove_empty_parentheses(line:str) -> str:
        return re.sub(r"\(\s*\)", "", line)
    
    @staticmethod
    def remove_dates(line: str) -> str:
        # Define regex patterns for different date formats
        date_patterns = [
            r'([01]?[0-9])[/\.-]([0-3]?[0-9])[/\.-]([0-9]{2})',  # mm dd yy
            r'([01]?[0-9])[/\.-]([0-3]?[0-9])[/\.-]([0-9]{4})',  # mm dd yyyy
            r'([0-3]?[0-9])[/\.-]([01]?[0-9])[/\.-]([0-9]{2})',  # dd mm yy
            r'([0-3]?[0-9])[/\.-]([01]?[0-9])[/\.-]([0-9]{4})',  # dd mm yyyy
        ]
        
        # Remove dates from the beginning of the line
        for pattern in date_patterns:
            line = re.sub(r'(^|\s)(\(?' + pattern + r'\)?)(\s|$)', '', line)

        line

        return line
    
    @staticmethod
    def remove_start_and_end_empty_lines(lines: List[str]) -> List[str]:
        start, end = 0, 0
        for i in range(len(lines)):
            if lines[i] != "":
                start = i
                break
        for i in reversed(range(len(lines))):
            if lines[i] != "":
                end = i
                break
        return lines[start:end + 1]
    
    @staticmethod
    def manage_empty_lines(lines: List[str]) -> List[str]:
        correct_lines = []
        for i in range(len(lines)):
            previous_line = lines[i - 1] if i > 0 else ""
            current_line = lines[i]
            next_line = lines[i + 1] if i < len(lines) - 1 else ""
            if previous_line == "" and current_line == "" and next_line == "":
                continue
            if Standardizer.has_mostly_lowercase(previous_line) and Standardizer.has_only_uppercase_and_special(current_line):
                correct_lines.append("")
            correct_lines.append(current_line)
        return correct_lines