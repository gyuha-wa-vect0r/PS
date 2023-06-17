sentence = list(input())
howlong = len(sentence)

if sentence[0] == " " and sentence[howlong - 1] == " ":
  print(sentence.count(" ") - 1)
elif sentence[0] == " " or sentence[howlong - 1] == " ":
  print(sentence.count(" "))
else:
  print(sentence.count(" ") + 1)