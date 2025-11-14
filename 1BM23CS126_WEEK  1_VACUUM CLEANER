a=input("Enter state of room A")
b=input("Enter state of room B")
state = {"A": "Dirty","B": "Dirty"}
current_room = input("Enter current room")
print("Initial State:")
print(state)
print()
while state["A"] == "Dirty" or state["B"] == "Dirty":
    print(f"Vacuum is in Room {current_room}")
    
    if state[current_room] == "Dirty":
        print(f"Cleaning Room {current_room}...")
        state[current_room] = "Clean"
    else:
        print(f"Room {current_room} is already clean.")

    current_room = "B" if current_room == "A" else "A"
    print(f"Moving to Room {current_room}...\n")
print("Final State:")
print(state)
print("Both rooms are clean. Vacuum stopped.")
