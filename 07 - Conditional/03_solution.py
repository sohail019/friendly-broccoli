# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = input('Enter Your Score:: ')
score = int(score)

if score > 100 :
  print('Invalid Score')
elif score >= 90:
  print('Grade A')
elif score >= 80:
  print('B Grade')
elif score >= 70:
  print('Grade C')
elif score >= 60:
  print('Grade D')
else:
  print('Fail')