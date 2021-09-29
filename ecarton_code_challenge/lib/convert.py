import pandas as pd

from typing import List

def convert_chars(input: List[str]) -> List[str]:
    """
    Convert a list of characters
    for characters < (h, H): return ord(c) * 10
    otherwise: return 0

    This implies:
        numeric characters are converted to 0
        null values are converted to 0

    Note:
    When the item is a multi-character word, this implementation
    considers the first letter of the word. This is not part 
    of the original specification.

    :param List[str] input: list of characters to convert
    :return: the corresponding list of ord(x)
    :rtype: List[int]
    """

    s: pd.Series = pd.Series(input)

    output = s.map(
        lambda x:
            (ord(str(x[0])) * 10 if 
            x and
            str(x)[0].lower() < 'h' and
            str(x)[0].lower() >= 'a'
            else 0))

    return list(output)
