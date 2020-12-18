current = int(input())
minimal = current

while current > 0:
    current = int(input())
    if minimal > current >= 0:
        minimal = current

print('Min:', minimal)