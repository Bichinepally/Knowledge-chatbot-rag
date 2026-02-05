from rag_pipeline import rag_answer

# Question → Expected Answer
test_questions = {
    "Who works in IT department?": "Employee",
    "Which employee works in HR?": "Employee",
    "Tell me employees in Finance": "Employee"
}

correct = 0

for question, expected in test_questions.items():
    answer = rag_answer(question)
    print(f"\nQ: {question}")
    print(f"A: {answer}")

    if expected.lower() in answer.lower():
        correct += 1

accuracy = correct / len(test_questions)
print(f"\nRAG Answer Accuracy: {accuracy:.2f}")