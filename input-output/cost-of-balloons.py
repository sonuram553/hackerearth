T = int(input())
result = []

for t in range(T):
  green_price, purple_price = [int(n) for n in input().split()]
  participants = int(input())
  
  first_problem_solve_counts = 0
  sec_problem_solve_counts = 0
  total_price = 0

  for p in range(participants):
    first_problem_status, sec_problem_status = [int(n) for n in input().split()]

    if first_problem_status:
      first_problem_solve_counts += 1
    if sec_problem_status:
      sec_problem_solve_counts += 1

  if green_price > purple_price:
    if first_problem_solve_counts < sec_problem_solve_counts:
      total_price = green_price * first_problem_solve_counts + purple_price * sec_problem_solve_counts
    else:
      total_price = green_price * sec_problem_solve_counts + purple_price * first_problem_solve_counts
  else:
    if first_problem_solve_counts < sec_problem_solve_counts:
      total_price = purple_price * first_problem_solve_counts + green_price * sec_problem_solve_counts
    else:
      total_price = purple_price * sec_problem_solve_counts + green_price * first_problem_solve_counts

  result.append(total_price)

for value in result:
  print(value)
