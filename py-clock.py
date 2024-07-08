#!/usr/bin/python3

# Rather than using a dictionary, we can just use indexing instead
# since it's only digits.
# : can be index 10.
NUMBERS = [number.strip("\n").split("\n") for number in [
"""
██████
██  ██
██  ██
██  ██
██████
""",
"""
    ██
    ██
    ██
    ██
    ██
""",
"""
██████
    ██
██████
██    
██████
""",
"""
██████
    ██
██████
    ██
██████
""",
"""
██  ██
██  ██
██████
    ██
    ██
""",
"""
██████
██    
██████
    ██
██████
""",
"""
██████
██    
██████
██  ██
██████
""",
"""
██████
    ██
    ██
    ██
    ██
""",
"""
██████
██  ██
██████
██  ██
██████
""",
"""
██████
██  ██
██████
    ██
██████
""",
"""
  
██
  
██
  
"""
]]

def get_number(number: int) -> list:
    return NUMBERS[number]

def print_numbers(numbers: list[list[list[str]]]):
    print()
    for line in numbers:
        for section in range(len(line[0])):
            print(" ", "  ".join(num[section] for num in line))
        print()

def translate_time(time: str) -> list[list[list[str]]]:
    chars = [char for char in time]
    numbers = [[]]
    
    for char in chars:
        if char in "0123456789":
            numbers[-1].append(get_number(int(char)))
        elif char == ":":
            numbers[-1].append(get_number(10))
        elif char == "\n":
            numbers.append([])
    
    return numbers

def timer(total_time: int):
    time_left = total_time
    
    while time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        hours, minutes = divmod(minutes, 60)
        
        time_format = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print_numbers(translate_time(time_format))
        time.sleep(1)
        print("\033[7A", end="", flush=True)
        time_left -= 1
    print("\033[0J", end="", flush=True)

def current_time():
    while 1:
        print_numbers(translate_time(datetime.now().strftime("%H:%M:%S")))
        time.sleep(1)
        print("\033[7A\033[0J", end="", flush=True)

if __name__ == "__main__":
    import sys
    import time
    from datetime import datetime

    try:
        if len(sys.argv) > 1:
            timer(int(sys.argv[1]))
        else:
            current_time()
    except KeyboardInterrupt:
        print("\nCancelled.")
