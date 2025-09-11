'''
def analyze_scores():
    user_input = input("Enter a tuple of numbers separated by spaces: ").strip()
    if not user_input:
        print("Not valid input")
        return

    tuples = tuple(map(int, user_input.split()))

    maximum = max(tuples)
    minimum = min(tuples)

    print(f"Max = {maximum}")
    print(f"Least = {minimum}")

analyze_scores()
'''

