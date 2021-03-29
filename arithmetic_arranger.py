def arithmetic_arranger(problems, calculate=False):
    
    # create variables
    topString = ''
    bottomString = ''
    dashesList = list()
    dashesString = ''
    totalsList = list()
    totalsString = ''
    sumValue = ''
    diffValue = ''
    totalValue = ''
    
    # check for correct number of problems
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems

    for sets in problems:
        pieces = sets.split()
        operand1 = pieces[0]
        operator = pieces[1]
        operand2 = pieces[2]

        # check that the problems have the correct operators (+ or -)
        if operator == '*' or operator == '/':
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        
        # check that the problems only contain numeric values
        if operand1.isnumeric() is False or operand2.isnumeric() is False:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems

        # check that numers are not longer than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

        # alignment, processing and calculations
        for align, details in zip('<', problems):

            # compare the length of operand1 and operand2
            # then process a single string of values containing operand1
            # on a new line process a string of values containing the operator and operand2
            # on a new line process dashes that are of equal length to the bottom string
            # on a new line process and include the sum or difference of the problem if the request is True
            if len(operand1) < len(operand2):
                topString += '{0:{align}{width}}'.format(
                    operand1.rjust(2 + len(operand2)), align=align, width=(len(operand2) + 6))
                bottomString += '{0:{align}{width}}'.format(
                    operator.ljust(2) + operand2, align=align, width=(len(operand2) + 6))
                dashesList.append((2 + len(operand2)) * '-')
                if operator == '+':
                    sumValue = str(int(operand1) + int(operand2))
                    totalValue = '{0:{align}{width}}'.format(
                        sumValue.rjust(2 + len(operand2)), align=align, width=(len(operand2) + 6))
                    totalsList.append(totalValue)
                elif operator == '-':
                    diffValue = str(int(operand1) - int(operand2))
                    totalValue = '{0:{align}{width}}'.format(
                        diffValue.rjust(2 + len(operand2)), align=align, width=(len(operand2) + 6))
                    totalsList.append(totalValue)

            if len(operand1) == len(operand2):
                topString += '{0:{align}{width}}'.format(
                    operand1.rjust(2 + len(operand1)), align=align, width=(len(operand1) + 6))
                bottomString += '{0:{align}{width}}'.format(
                    operator.ljust(2) + operand2, align=align, width=(len(operand1) + 6))
                dashesList.append((2 + len(operand2)) * '-')
                if operator == '+':
                    sumValue = str(int(operand1) + int(operand2))
                    totalValue = '{0:{align}{width}}'.format(
                        sumValue.rjust(2 + len(operand1)), align=align, width=(len(operand1) + 6))
                    totalsList.append(totalValue)
                elif operator == '-':
                    diffValue = str(int(operand1) - int(operand2))
                    totalValue = '{0:{align}{width}}'.format(
                        diffValue.rjust(2 + len(operand1)), align=align, width=(len(operand1) + 6))
                    totalsList.append(totalValue)

            if len(operand1) > len(operand2):
                topString += '{0:{align}{width}}'.format(
                    operand1.rjust(2 + len(operand1)), align=align, width=(len(operand1) + 6))
                bottomString += '{0:{align}{width}}'.format(
                    operator.ljust(2) + operand2.rjust(len(operand1)), align=align, width=(len(operand1) + 6))
                dashesList.append((2 + len(operand1)) * '-')
                if operator == '+':
                    sumValue = str(int(operand1) + int(operand2))
                    totalValue = '{0:{align}{width}}'.format(
                        sumValue.rjust(2 + len(operand1)), align=align, width=(len(operand1) + 6))
                    totalsList.append(totalValue)
                elif operator == '-':
                    diffValue = str(int(operand1) - int(operand2))
                    totalValue = '{0:{align}{width}}'.format(
                        diffValue.rjust(2 + len(operand1)), align=align, width=(len(operand1) + 6))
                    totalsList.append(totalValue)

    # process all the values prepared and calculated in the main section
    topString = topString.rstrip()
    topString += topString.join('\n')
    bottomString = bottomString.rstrip()
    bottomString += bottomString.rstrip().join('\n')
    dashesMap = map(lambda dashesString: dashesString.ljust(
        len(dashesString) + 4), dashesList)
    dashesString = ''.join(list(dashesMap))
    dashesString = dashesString.rstrip()
    totalsMap = map(lambda totalsString: str(totalsString), totalsList)
    totalsString = ''.join(list(totalsMap))
    totalsString = totalsString.rstrip()

    # check the calculation flag value and build the required outut of the function
    if calculate is True:
        dashesString += dashesString.join('\n')
        arranged_problems = topString + bottomString + dashesString + totalsString
    else:
        arranged_problems = topString + bottomString + dashesString

    return arranged_problems
