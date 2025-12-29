from collections import Counter
from math import factorial

def uniq_count(s):
    text = s.lower() 
    
    counts = Counter(text)
    n = len(text)
    
    numerator = factorial(n)
    
    denominator = 1
    for count in counts.values():
        denominator *= factorial(count)
        
    return numerator // denominator
