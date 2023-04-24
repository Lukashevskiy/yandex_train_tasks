from typing import Dict
from collections import Counter

def hist_text(text: str) -> None:
    
    def text_to_counted_dict(text: str) -> Dict[str,int]:
        counted_dict = Counter(text)
        counted_dict.pop(' ', None)
        counted_dict.pop('\n', None)
        
        return dict(sorted(counted_dict.items(), key=lambda x: x[0]))
    
    def get_hist_level(lvl: int, counted_dict: Dict[str,int]) -> str:
        ans_str = ''
        for height in counted_dict.values():
            if lvl <= height:
                ans_str += "#"
            else:
                ans_str += " "

        return ans_str
    
    counted_dict = text_to_counted_dict(text)
    hist_height = max(counted_dict.values())

    while hist_height > 0:
        print(get_hist_level(hist_height, counted_dict))
        hist_height -= 1
    
    print(*counted_dict.keys(), sep='')

with open('input.txt', 'r') as f:
    text = f.read()
    print(text)
    hist_text(text)