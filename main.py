# Command Line Tool for quick a quick solver.

import argparse
from sympy import *
from sympy.abc import *
from sympy.plotting import plot
from sympy.parsing.sympy_parser import parse_expr, \
    implicit_multiplication, \
    standard_transformations, \
    implicit_multiplication_application, \
    _token_splittable
transformations = (standard_transformations + (implicit_multiplication_application,))


parser = argparse.ArgumentParser(description='Simple Command Line Algebra Solver with Sympy')
parser.add_argument('--expression', '-e', type=str, default='x = 0')
parser.add_argument('--variables', '-v', type=str, default='x')
parser.add_argument('--solve_for', '-s', type=str, default='x')
parser.add_argument('--graph', '-g', action='store_true', default=False)




if __name__ == "__main__":
    args = parser.parse_args()

    # for a solver to work... well, it has to be more than just an expression
    if "=" not in args.expression:
        raise Exception('You need an equals sign in the expression.')

    # now we need to get the variables we want to use
    left, right = args.expression.split("=")

    # now we need to parse the Latex (if it was LaTex) that was passed
    tgt = {s: Symbol(s) for s in args.variables.split(" ")}

    # now run the solver over it and spit out the output
    left = parse_expr(left, transformations=transformations, local_dict=tgt)
    right = parse_expr(right, transformations=transformations,  local_dict=tgt)
    equality = Eq(left, right)
    solutions = solve(equality, tgt)

    for solution in solutions:
        for variable in solution:
            expr = solution[variable]
            print(variable, "=", expr)

    # if it's been asked for, graph it

    if args.graph:
        pl = plot(expr)