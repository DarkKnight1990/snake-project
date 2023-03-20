SNAKE = r""" \
    \    __
    \   {00}
        (__)\
          ^ \\
            _\\__
           (______)_
          (________)Oo 
"""


def bubble(message):
    bubble_length = len(message) + 2
    return f"""
    {"_" * bubble_length}
    ({message})
    {"_" * bubble_length}
    """

def say(message):
    print(bubble(message))
    print(SNAKE)
