AboutQuiz ={
    'Subject': 'IB DP Business and Management',
    'Class': 'Grade 11 Higher Level',
    'Chapter': '3.1-3.5',
    'Correct': 'One question is awarded one point',
}

print("""
    In this quiz, you will be asked a total of 10 questions that ranges from multiple choice questions, short answer questions and story questions.
    The questions will be from chapters 3.1-3.5, each question having one point.
    It is mandatory to answer the questions in lower case.
""")
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 10

num_correct = 0

QUESTIONS = {
    "What is Depreciation": [
        "a decrease in the value of a currency relative to other currencies", 
        "an increase in the value of an asset over time", 
        "an accounting technique used to spread payments over a set period of time", 
        "ownership of assets that may have debts or other liabilities attached to them."
    ],
    "What does Gross Profit Margin tell us": [
        "What your business made after paying for the direct cost of doing business",
        "Whether the company makes money or not",
        "Company's ability to use its assets and manage its liabilities effectively",
        "Whether a company's current assets are enough to cover their liabilities"
    ],
    "What is the definition of liability": [
        "The amount of money owed by the business",
        "Valuable things that the business owns",
        "The amount of money raised through the sale of shares",
        "An amount of net profit after interest"
    ],
    "What are some two external sources of finance": [
        "Crowdfunding and Overdrafts",
        "Trade Creditors and Retained Profits",
        "Leasing and Sales of Assets",
        "Personal Funds and Microfinance"
    ],
}

for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

QuestionList = {
    "What is one of the formula used to determine the average number of days it takes to collect money from debtors" : "debtor days",  
    "What is one of the formula used to look at the firm’s capital employed that is financed by long term debt" : "gearing ratio", 
}

for num, (questions, CAnswers) in enumerate(QuestionList.items(), start=5):
    print(f"\nQuestion {num}:")
    Answershort = input(f"{questions}\n")

    if Answershort == CAnswers:
        num_correct += 1
        print("Correct!")
    else:
        print(f"The answer is {CAnswers!r}, not {Answershort!r}")

StudyCaseQuestion = {
    "What is the cost to manufacture 20 sofas?" : "19000",  
    "How much revenue is generated from selling 20 sofas at $800 each?" : "16000", 
    "How much profit does the manufacturer gain (or lose) by manufacturing and selling 20 sofas?" : "-3000" ,
    "How many sofas must be sold in order to have a profit of $12,000?" : "70"
}
print("\nThe cost to manufacture a sofa is $700 per sofa plus a fixed setup cost of $5,000. Each sofa sells for $800.")

for num, (question, CorrectAnswers) in enumerate(StudyCaseQuestion.items(), start=7):
    print(f"\nQuestion {num}:")
    Answer = input(f"{question}\n")

    if Answer == CorrectAnswers:
        num_correct += 1
        print("Correct!")
    else:
        print(f"The answer is {CorrectAnswers!r}, not {Answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")

print("\n")
print(f"\t{AboutQuiz}\n")
print(f"\t{QUESTIONS}\n")
print(f"\t{QuestionList}\n")
print(f"\t{StudyCaseQuestion}\n")