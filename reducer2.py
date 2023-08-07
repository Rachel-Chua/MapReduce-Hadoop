#!/usr/bin/env python3

import sys

current_key = None
current_count = 0
key = None

# Read key-value pairs from the standard input
for line in sys.stdin:
    line = line.strip()

    # Parse the composite key and value from the input
    key, count = line.split('\t', 1)
    try: 
        count = int(count) 
    except ValueError: 
        continue

    # Check if the composite key is the same as the current one
    if current_key == key:
        current_count += count
    else:
        # If the composite key has changed, print the accumulated count for the previous key
        if current_key is not None:
            print(f"{current_key}\t{current_count}")

        # Reset the current key and count to the new values
        current_key = key
        current_count = count

# Print the last composite key and its accumulated count
if current_key is not None:
    print(f"{current_key}\t{current_count}")
