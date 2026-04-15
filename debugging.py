#fix one: Loop backwards to safely remove odd numbers

def clean_database(record_ids):
    # Fix 1: Loop backwards to safely remove odd numbers
    for i in range(len(record_ids) - 1, -1, -1):
        if record_ids[i] % 2 != 0:
            record_ids.remove(record_ids[i])
    return record_ids

#fix two: Create a new list with only even numbers

def clean_database(record_ids):
    # Fix 2: Create a new list with only even numbers
    return [record_id for record_id in record_ids if record_id % 2 == 0]


"""
TASK 1:
I used the VS Code debugger and added a breakpoint where the program removes items from the list.
When I ran it, I noticed that when the loop removes the first odd number (1), the next number (3) shifts into its place.
 But the loop moves to the next index, so it skips 3. 
 This is why some odd numbers are not removed.
TASK 2:
Why this happens:
When you remove an item from a list while looping forward, the remaining items shift left. The loop then moves to the next index and skips the item that just moved into the current position.
Fix:
Fix 1: Iterate through the list backwards so shifting doesn’t affect what you check.
Fix 2: Create a new list that only includes even numbers.
"""