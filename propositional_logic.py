class PropositionalLogic:
    OR_SYMBOL = 'v'

    def __init__(self, statement: str):
        self.statement = statement.strip()                # the question itself
        self.atomicVariables = self._setAtomicVariables() # representation of statement (p, q)
        self.variableCount = self._countVariable()        # atomic variable count
        self.rowsCount = self._calculateRowsCount()       # number of rows
        self.binaryRows = self.generateBinaryRows()       # generate bits

    """
    STEP 1 : IDENTIFY ALL THE UNIQUE ATOMIC VARIABLE
    """

    def _setAtomicVariables(self) -> str:
        atomicVariables = set() # automatically ignores duplicates
        for char in self.statement:
            if char.isalpha() and char != self.OR_SYMBOL:
                atomicVariables.add(char)

        return "".join(sorted(atomicVariables)) # return sorted variables

    def _countVariable(self) -> int:
        return len(self.atomicVariables)

    """
    STEP 2 : DETERMINE THE NUMBER OF ROWS
    """
<<<<<<< HEAD

=======
<<<<<<< Updated upstream
>>>>>>> a85ab6f (diverged conflict)
    def _numberOfRows(self): 
=======

    def _calculateRowsCount(self): 
>>>>>>> Stashed changes
        return 2 ** self.variableCount

    """
    STEP 3 : FILL ALL THE COLUMN WITH VALUES (0, 1)
    """

    def generateBinaryRows(self):
        binaryStrings = []
        binaryRows = []

        # assigning binaries on the binaryStrings array 
        # ['00', '01', '10' '11']
        for i in range(self.rowsCount):
            binaryStrings.append(f"{i:0{self.variableCount}b}")

        # converting binary strings into lists of individual bits
        # [['0', '0'], ['0', '1'], ['1', '0'], ['1', '1']]
        for binary in binaryStrings:
            rowValues = []
            for bits in binary:
                rowValues.append(bits)    
            binaryRows.append(rowValues)

        return binaryRows

    """
    STEP 4 : CHANGE ALL VALUES INTO SOMETHING PYTHON CAN READ
    """
    # Step 4.0 : a function to convert variables to truth values
    def _mapVariablesToTruthValues(self) -> list:
        atomicVariables = self.atomicVariables
        columnValues = self.binaryRows
        changedVariables = []
        
        # Assignign all the atomicVariables with its truth values equivalence
        # p = 0, q = 0, r = 1
        for row in range(self.rowsCount):
            temp = {}
            for i in range(len(atomicVariables)):
                temp[atomicVariables[i]] = (columnValues[row][i])
            changedVariables.append(temp)

<<<<<<< HEAD
=======
<<<<<<< Updated upstream
        return changedVariables
=======
>>>>>>> a85ab6f (diverged conflict)
        return changedVariables # returns a list of dictionary
    
    def _convertExpression(self, rowDict, statement) -> str:
        # Step 4.1 : Replace each variable with its value 
<<<<<<< HEAD
        # convert atomic variables(p, q) into binary
        translationTable = str.maketrans(rowDict)
        replacedText = statement.translate(translationTable)
         
        # Step 4.2 : replace logical operators  
        # convert logical operators into python equivalence
        logicalOperators = {'^': 'and', 'v': 'or', '~': 'not'}
=======
        # convert atomic variables(p, q) into bits (0, 1)
        replacedText = statement
        for atomicVariable, bits in rowDict.items():
            replacedText = replacedText.replace(atomicVariable, bits)
         
        # Step 4.2 : replace logical operators  
        # convert propositional logical symbols into python boolean syntax
        logicalOperators = {'^': 'and', 'v': 'or', '~': 'not '}
>>>>>>> a85ab6f (diverged conflict)
        for operator, equivalence in logicalOperators.items():
            replacedText = replacedText.replace(operator, equivalence)
        
        return replacedText # (p v q) convert into (0 or 1) 

    def evaluateExpression(self, statement = None) -> list:
        statement = statement or self.statement

        # Step 4.3 : Evaluate the resulting strings
        # since statements are converted into statement that python can read 
        # we can now evaluate it using eval()
        evaluated = [] 
        mappedVariables = self._mapVariablesToTruthValues()
        for var in mappedVariables:
            evaluated.append(eval(self._convertExpression(var, statement)))
        
        # Step 4.4 : result is 0 or 1
        return evaluated # return list of evaluation
    
<<<<<<< HEAD
    """
    STEP 5 : PRINT THE OUTPUTS
    """
    def readThroughParenthesis(self) -> list:
        question = self.statement
        firstIndex = lastIndex = 0
        textArray = []
        text = ""

        for i in range(len(question)):
            match question[i]:
                case '(':
                    firstIndex = i + 1
                    continue
                case ')':
                    lastIndex = i

            if(firstIndex > 0 and lastIndex > 0):
                text = question[firstIndex:lastIndex]
                textArray.append(text)
                firstIndex = 0
                lastIndex = 0
                text = ""

        return textArray

    def printTruthTable(self):
        # Header
        sentenceLength : int = 0
        for char in self.atomicVariables.strip():
            print(f"{char:^3}", end="")
        for sentence in self.readThroughParenthesis():
            print(f"({sentence})", end=" ")
            sentenceLength = max(len(sentence), sentenceLength)
        print()
        
=======
    def _extractExpressions(self) -> list:
        statement = self.statement
        firstIndex = 0
        subexpressions = []
        extracted = ""

        for i in range(len(statement)):
            if statement[i] == '(':
                firstIndex = i + 1
                continue

            if statement[i] == ')':
                extracted = statement[firstIndex:i]
                subexpressions.append(extracted)
        
        return subexpressions

    def _evaluateExtractedExpressions(self) -> list:
        bits = []        
        for expression in self._extractExpressions():
            bits.append(self.evaluateExpression(expression))

        return bits

    """
    STEP 5 : PRINT THE OUTPUTS
    """
    def printTruthTable(self):
        subexpressionLength = []
        statementLength : int = len(self.statement)
        extractedBits = self._evaluateExtractedExpressions()

        # Header
        for char in self.atomicVariables.strip():
            print(f"{char:^3}", end="")
        for sentence in self._extractExpressions():
            print(f"({sentence})", end=" ")
            subexpressionLength.append(len(sentence))
        print(self.statement)

>>>>>>> a85ab6f (diverged conflict)
        # Body
        for row in range(self.rowsCount):
            for byte in self.binaryRows[row]:
                print(f"{byte:^3}", end="")

<<<<<<< HEAD
            destructure = self.readThroughParenthesis()
            for chunk in destructure:
                chunkEvaluate = [c for c in self.evaluateExpression(chunk)]
                print(f"{chunkEvaluate[row]:^{sentenceLength+3}}", end="")
             
            print()
        
        print()
    
=======
            count = 0 
            for bits in extractedBits: 
                print(f"{bits[row]:^{subexpressionLength[count]+3}}", end="")
                count += 1

            finalAnswer = self.evaluateExpression()
            print(f"{finalAnswer[row]:^{statementLength+1}}")

        print()
    
>>>>>>> Stashed changes
>>>>>>> a85ab6f (diverged conflict)


