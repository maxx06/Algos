#ACSL2020-2021_Senior3_Contest1
#April 2021
#Max Xiong



def sumOfLastRow(s, d, r):
  d, s = int(str(d), base = 16), int(s, base = 16)
  sum, lastDigits = [], []

  for i in range(r):
    for i in range(i + 1):
      sum.append(hex(s) [2:])
      s = s + d
  
  for i in range(1, r + 1):
    lastDigits.append(sum[-i])

  if(len(lastDigits) > 1):
    for i in range(len(lastDigits)):
      for i in str(lastDigits[i]):
        lastDigits.append(i)

    del lastDigits[0: r]
  
  finalSum = 0
  for i in lastDigits:
      finalSum = finalSum + int(i, base = 16)

  finalSum = hex(finalSum) [2:]
  del lastDigits[:]

  for item in str(finalSum):
      lastDigits.append(i)
 
  print(finalSum)

  sum_of_digits = 0
  for digit in finalSum:
       sum_of_digits += int(digit, base = 16)

  while len(hex(sum_of_digits)):
    if len(hex(sum_of_digits)) != 1:
      sum_of_digits += int(digit, base = 16)
  
  print(sum_of_digits)