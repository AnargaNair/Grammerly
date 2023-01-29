from textblob import TextBlob

a = TextBlob("Campk12 is gooodd coompny anr alwys valulues thier emplyees.")

a= a.correct()

print(a)