class PropositionalLogic:
    OR_SYMBOL = 'v'

    def __init__(self, statement: str):
        self.statement = statement.strip()                # the question itself
        self.atomicVariables = self._setAtomicVariables() # representation of statement (p, q)
        self.variableCount = self._countVariable()        # atomic variable count
        self.rowsCount = self._numberOfRows()             # number of rows
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

    def _numberOfRows(self): 
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
            for index in range(self.variableCount):
                bit = binary[index]
                rowValues.append(bit)    
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

        return changedVariables # returns a list of dictionary
    
    def _convertExpression(self, rowDict, statement) -> str:
        # Step 4.1 : Replace each variable with its value 
        # convert atomic variables(p, q) into binary
        translationTable = str.maketrans(rowDict)
        replacedText = statement.translate(translationTable)
         
        # Step 4.2 : replace logical operators  
        # convert logical operators into python equivalence
        logicalOperators = {'^': 'and', 'v': 'or', '~': 'not'}
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
        
        # Body
        for row in range(self.rowsCount):
            for byte in self.binaryRows[row]:
                print(f"{byte:^3}", end="")

            destructure = self.readThroughParenthesis()
            for chunk in destructure:
                chunkEvaluate = [c for c in self.evaluateExpression(chunk)]
                print(f"{chunkEvaluate[row]:^{sentenceLength+3}}", end="")
             
            print()
        
        print()
    


