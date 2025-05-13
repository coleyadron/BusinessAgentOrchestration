import csv

def parse_qa_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        if len(rows) < 2:
            raise ValueError("CSV must contain at least two rows (questions and answers).")

        questions = rows[0]
        answers = rows[1]

        if len(questions) != len(answers):
            raise ValueError("Mismatch between number of questions and answers.")

        qa_dict = dict(zip(questions, answers))
        return qa_dict

# Example usage:
if __name__ == "__main__":
    file_path = "drywall_contractor_intake_sample_complete.csv"
    qa = parse_qa_csv(file_path)
    for question, answer in qa.items():
        print(f"{question.strip()}: {answer.strip()}")
