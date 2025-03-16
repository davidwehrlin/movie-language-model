from dataclasses import dataclass
from typing import List
import os

@dataclass
class DataState:
    RAW: str = "raw"
    PROCESSED: str = "processed"


class ScraperUtils:

    @staticmethod
    def write_list_to_file(script_name: str, script_lines: List[str], data_state: DataState = DataState.RAW):
        directory = f"data/{data_state}"
        
        file_path = os.path.join(directory, f"{script_name}.txt")
        if os.path.exists(file_path) and data_state == DataState.RAW:
            return
        
        with open(file_path, 'w') as file:
            for line in script_lines:
                file.write(line + '\n')
        print(f"File written: {file_path}")