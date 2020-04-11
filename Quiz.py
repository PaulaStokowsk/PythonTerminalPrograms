def calculateAnswer(lhs, rhs, operator):
   if(operator not in "/*-+"):
      raise Exception("unknown operator")
   return eval("{0}{1}{2}".format(lhs,operator,rhs))


from random import randint
def generateQuestion():
   ops="/*-+"
   opIndex= randint(1,len(ops)-1)
   operator=ops[opIndex]
   lhs=randint(0,10)
   rhs=randint(0,10)
   while(rhs==0 and operator == "/"):
      rhs=randint(0,10)
   return lhs,rhs,operator

correct = 0
totalQuestions = 3
for i in range(totalQuestions):
   question = generateQuestion()
   correctAnswer = calculateAnswer(question[0],question[1],question[2])
   playerAnswer = input("{0} {2} {1} = ".format(question[0],question[1],question[2]))
   if(correctAnswer == playerAnswer):
      print("Correct!")
      correct += 1
   else:
      print("Wrong. Correct answer = " + str(correctAnswer))

print("You got {0} correct out of {1}. Or {2}% correct.".format(correct, totalQuestions, correct/totalQuestions*100))