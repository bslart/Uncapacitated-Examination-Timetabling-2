from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  solver = pywraplp.Solver('SolveIntegerProblem',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

  x = solver.IntVar(0.0, solver.infinity(), 'x')
  y = solver.IntVar(0.0, solver.infinity(), 'y')

  # 30 x1 + 20 x2 <= 300 
  constraint1 = solver.Constraint(-solver.infinity(), 300)
  constraint1.SetCoefficient(x, 30)
  constraint1.SetCoefficient(y, 20)

  # 5 x1 + 10 x2 <= 110 
  constraint2 = solver.Constraint(-solver.infinity(), 110)
  constraint2.SetCoefficient(x, 5)
  constraint2.SetCoefficient(y, 10)

  # max 6 x + 8 y.
  objective = solver.Objective()
  objective.SetCoefficient(x, 6)
  objective.SetCoefficient(y, 8)
  objective.SetMaximization()

  result_status = solver.Solve()
  
  #Best Solution
  assert result_status == pywraplp.Solver.OPTIMAL

  assert solver.VerifySolution(1e-7, True)

  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())

  print('Optimal objective value = %d' % solver.Objective().Value())
  print()
  
  variable_list = [x, y]

  for variable in variable_list:
    print('%s = %d' % (variable.name(), variable.solution_value()))

if __name__ == '__main__':
  main()