numbers = input().split()
answers = input().split()

print(True if len(set(numbers).symmetric_difference(set(answers))) == 0 else False)
