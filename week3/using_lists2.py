states = ["Washington", "Oregon", "California"]

'''
for state in states:
    state = state.lower()
    print(state)
'''
'''
print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)
'''
states2 = ["Nevada", "Ohio", "New York"]
best_states = states + states2

print(best_states)
print(best_states[1:3])
print(best_states[:3])
print(best_states[4:])