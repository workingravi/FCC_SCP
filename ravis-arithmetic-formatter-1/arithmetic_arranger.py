
def arrange_one(p, solve):
  """
  return the arranged problem or an Error if found
  """
  is_err = False
  s = ""
  opn = p.split()
  opn1 = opn[1]
  if not (opn1 == '+' or opn1 == '-'):
    is_err = True
    s = "Error: Operator must be '+' or '-'."
    return is_err, s  

  op1 = opn[0]
  op2 = opn[2]
  if not op1.isnumeric() or not op2.isnumeric():
    is_err = True
    s = "Error: Numbers must only contain digits."
    return is_err, s

  if len(op1) > 4 or len(op2) > 4:
    is_err = True
    s = "Error: Numbers cannot be more than four digits."
    return is_err, s

  lenp = max(len(op1), len(op2)) + 2
  l1 = op1.rjust(lenp)
  l2 = opn1 + ' ' + (op2.rjust(lenp))[2:]
  s = l1 + '\n' + l2
  dashes = '-'* lenp
  s += '\n' + dashes
    
  if solve:
    op = op1 + opn1 + op2
    ans = eval(op)
    # Width of problem
    s += '\n' + str(ans).rjust(lenp)
    
  return is_err, s

def arithmetic_arranger(problems, solve=False):
    arranged_problems = ""
    arranged_probs = []
    if len(problems) > 5:
      return 'Error: Too many problems.'
    
    for p in problems:
      e, sp = arrange_one(p, solve)
      if e:
        return sp
      else:
        arranged_probs.append(sp)

    split_lines = list(map("    ".join, zip(*[p.split('\n') for p in  arranged_probs])))
    arranged_problems = "\n".join(split_lines)
    # horizontal join
    #res = '\n'.join([x + y for x, y in splt_lines])
  
    
    #arranged_problems = res
    return arranged_problems