def determine_sequence_type(sequence):
    if len(set(sequence)) == 1:
        return "CONSTANT"
    elif all(sequence[i] < sequence[i + 1] for i in range(len(sequence) - 1)):
        return "ASCENDING"
    elif all(sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1)):
        return "WEAKLY ASCENDING"
    elif all(sequence[i] > sequence[i + 1] for i in range(len(sequence) - 1)):
        return "DESCENDING"
    elif all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1)):
        return "WEAKLY DESCENDING"
    else:
        return "RANDOM"


sequence = []
while True:
    num = int(input())
    if num == -2000000000:
        break
    sequence.append(num)

print(determine_sequence_type(sequence))
