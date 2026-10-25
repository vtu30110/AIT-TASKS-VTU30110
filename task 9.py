
print("College Chatbot")
print("Ask about admissions, fees, or schedules.")
print("Type 'bye' to exit.")

while True:
    question = input("You: ").lower()

    if question == "bye":
        print("Bot: Goodbye!")
        break

    elif "admission" in question:
        print("Bot: Admissions are handled by the college office.")

    elif "fee" in question:
        print("Bot: Please contact the accounts department.")

    elif "schedule" in question or "timetable" in question:
        print("Bot: Check the college academic timetable.")

    else:
        print("Bot: Sorry, I don't understand that question.")
