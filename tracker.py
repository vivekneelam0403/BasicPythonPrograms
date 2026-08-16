
def calculate_status(score):
    if score >= 60:
        return "pass"
    else: 
        return "fail"

def process_scores():
    total = 0 
    count = 0 

    with open("scores.txt", "r") as file:
        lines = file.readlines()

    with open("report.txt", "w") as report:
        for line in lines: 
            student, score = line.strip().split(",")
            score = int(score)

            status = calculate_status(score)

            report.write(f"{student}: {score} - {status}\n")

            total += score
            count += 1

    average = total / count
    return average

average = process_scores()
print("Average score:", average)


with open("scores.txt", "r") as file:
    for line in file: 
        student, score = line.strip().split(",")
        score = int(score)

        print(student, calculate_status(score))




        

