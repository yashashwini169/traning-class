from ollama import chat

sys_msg="you are a friendly tutor.Answer in piratespeak.Answer in one question"

history=[ {"role":"system","content":sys_msg}]

while True:
    question = input("You:")
    if question == "":
        print("Anushka : please type somthing.")
        continue
    if question.lower().strip() == "/history":
        print("------ Your conversation so far -------")
        if len(history) < 2:
            print("NOthing here sa far!")
        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "Anushka"
            print(f"{speaker}: {msg.content}")
        print("----------------------------------")
        print()
        continue

    if question.lower().strip() =="/clear":
        history = [{"role": "system","content" : system_msg}]
        print("your history is cleared.start a fresh conversation.")
        print()
        continue
    
    if question.lower().strip() =="/help":
        print("------Avaliable commands------")
        print("/history - display conversation history")
        print("/clear - clears chat history")
        print("/help - display this list")
        print("exit - quits the chatbot")
        print("-----------------------------")
        print()
        continue

    if question.lower().strip() == "exit":
        print("Anuksha : Goodbye user. Please come back soon!")
        print(f"You asked {question_counter} question today. Good job!")
        break

    hisyory.append({"role" : "user", "content": question})
    question_counter += 1
    try:
        response = chat(
                model="llama3.2",
                messages = history
            )
        reply = response.message.content
        history.append({"role" : "assistant", "content": reply})
        print(f"anushka : {reply}")
        print()
    except Exception as e:
        print("unknown issue.Is ollama running?")


 