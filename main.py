from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # Will this be working?
    lines = open(path, 'r').read().split('\n')
    return lines
