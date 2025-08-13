from textblob import TextBlob

print("Hi students, Welcome to the Sentimental Analysis \n")
user_name = input("What is your name\n")
print(f"Good to know your {user_name} Lets being with the Sentimental Analysis\n")
print("Type exit to quit \n")

while True:
    sentence = input("Enter the Sentence for Sentimental Analysis \n")
    if sentence.lower() == "exit":
     print(f"Good Bye {user_name} for the Day")
     break
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment>0:
      print("Positive Emotion \n")
    elif sentiment<0:
      print("Negative Emotion \n ")
    else:
      print("Neutral \n")
     
       
