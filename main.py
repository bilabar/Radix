def superscript(n):
  """
  How do you print superscript in Python?
  https://stackoverflow.com/a/62987096/17063196
  """
  return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)]) 

def radix_explainer(num, radix):
  print(num)
  if int(max(s(num))) > radix:
    return 
  total = 0
  step4 = []
  for n, exp in zip(s(num), range(len(s(num)))[::-1]):
    step1 = n + " x " + s(radix) + ss(exp)
    step2 = n + " x " + s(pow(radix, exp))
    step3 = int(n) * pow(radix, exp)
    if step3:
      step4.append(s(step3))
    total += step3
    print(step1,'=', step2, '=', step3)
  
  print()
  print(" + ".join(step4), '=', total)
  return total

s = str
ss = superscript

number = 101010
assert int(s(number), 2) == radix_explainer(number, 2)
