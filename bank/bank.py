# Greeting prompt // stripped off spaces // lowercase // first string will be judged only
greeting = input("Greetings: ").strip().lower()
# Check if string starts with hello then output $0
if greeting[0:5] == "hello":
    print("$0")
elif greeting[0] == "h":
    print ("$20")
else:
    print("$100")

