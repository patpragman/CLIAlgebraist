# Command Line Tool for quick a quick solver.

from sys import argv
from sympy import *
from sympy.abc import *
from sympy.plotting import plot
from sympy.parsing.sympy_parser import parse_expr, \
    standard_transformations, \
    implicit_multiplication_application
transformations = (standard_transformations + (implicit_multiplication_application,))



if __name__ == "__main__":
    args = " ".join(argv[1:])
    statement, equation = args.split(":")
    equation.replace(" ", "")

    # now we need to parse the Latex (if it was LaTex) that was passed

    command, category, variable_name = statement.split(" ")

    if command.upper() == "SOLVE":
        # for a solver to work... well, it has to be more than just an expression
        if "=" not in equation:
            raise Exception('You need an equals sign in the expression.')

        # now we need to get the variables we want to use
        left, right = equation.split("=")

        # now run the solver over it and spit out the output
        left = parse_expr(left, transformations=transformations)
        right = parse_expr(right, transformations=transformations)
        equality = Eq(left, right)
        solve_for = Symbol(variable_name)
        solutions = solveset(equality, solve_for)

        print(f'Solutions for {variable_name}:')
        for solution in solutions:
            print(solve_for, "=", solution)

    elif command.upper() == "INTEGRATE":
        # for a solver to work... well, it has to be more than just an expression
        if "=" in equation:
            raise Exception('Unexpected equals sign.')

        equation = parse_expr(equation, transformations=transformations)
        print(f"The integral of {equation} with respect to {variable_name} is:")
        print(integrate(equation, Symbol(variable_name)))
    elif command.upper() == "DERIVATIVE":
        # for a solver to work... well, it has to be more than just an expression
        if "=" in equation:
            raise Exception('Unexpected equals sign.')

        equation = parse_expr(equation, transformations=transformations)
        print(f"The derivative of {equation} with respect to {variable_name} is:")
        print(diff(equation, variable_name))
    elif command.upper() == "PLOT":
        # plot 2d graph
        x = Symbol(category)
        y = Symbol(variable_name)

        # now we need to get the variables we want to use
        left, right = equation.split("=")

        # now run the solver over it and spit out the output
        left = parse_expr(left, transformations=transformations)
        right = parse_expr(right, transformations=transformations)
        equation = Eq(left, right)
        solutions = solveset(equation, y)

        print(solutions)
        if solutions is not None:
            sol_list = list(solutions)
            p = plot(sol_list.pop(), show=False)
            for solution in sol_list:
                p.append(plot(solution, show=False)[0])

            p.show()
    elif command.upper() == "INSTALL":
        print('Installed OK!')
    else:
        print(f'Command "{command}" not understood in statement "{" ".join([statement, equation])}."')
