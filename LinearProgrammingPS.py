from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  solver = pywraplp.Solver('LinearExample',
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

  x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
  y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')

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

  solver.Solve()
  opt_solution = 6 * x.solution_value() + 8 * y.solution_value()
  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())

  print('Solution:')
  print('x = ', x.solution_value())
  print('y = ', y.solution_value())

  #Best Solution
  print('Optimal objective value =', opt_solution)

  print(('%s: reduced cost = %f' % (x, x.reduced_cost())))
  print(('%s: reduced cost = %f' % (y, y.reduced_cost())))
  print(('%s: Dual Value = %f' % (y, constraint1.dual_value())))
  print(('%s: Dual Value = %f' % (y, constraint2.dual_value())))

if __name__ == '__main__':
  main()