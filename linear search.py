arr = [10, 20, 30, 40, 50]
target = 30
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Found it! {target} is at index {i}.")
        found = True
        break

if not found:
    print(f"Sorry, {target} is not in the list.")

