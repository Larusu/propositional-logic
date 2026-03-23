class PropositionalLogic:
    OR_SYMBOL = 'v'
    logicalOperators = {
            '^': 'and', 
            'v': 'or', 
            '~': 'not '
        }

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

    def _calculateRowsCount(self): 
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

        return changedVariables # returns a list of dictionary

    # implies == conditional
    def implies(self, p, q):
        return not p or q
    
    def biconditional(self, p, q):
        return p == q
    
    def _findTopLevelOp(self, text, op):
        """Return index of `op` at depth 0, or -1 if not found."""
        depth = 0
        for i in range(len(text) - len(op) + 1):
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1
            elif depth == 0 and text[i:i+len(op)] == op:
                return i
        return -1
 
    def _transformOperators(self, text) -> str:
        """
        Recursively convert -> and <> to Python function calls,
        respecting parenthesis nesting. Logical symbol replacement
        (^, v, ~) is done AFTER this step so they don't interfere.
        """
        text = text.strip()
 
        # Check for top-level <> first (lower precedence than ->)
        idx = self._findTopLevelOp(text, '<>')
        if idx != -1:
            left  = self._transformOperators(text[:idx])
            right = self._transformOperators(text[idx+2:])
            return f"biconditional({left}, {right})"
 
        # Check for top-level ->
        idx = self._findTopLevelOp(text, '->')
        if idx != -1:
            left  = self._transformOperators(text[:idx])
            right = self._transformOperators(text[idx+2:])
            return f"implies({left}, {right})"
 
        # No top-level connective — recurse into the innermost parentheses
        # by rebuilding character by character
        result = []
        i = 0
        while i < len(text):
            if text[i] == '(':
                # Find matching closing paren
                depth = 1
                j = i + 1
                while j < len(text) and depth > 0:
                    if text[j] == '(':
                        depth += 1
                    elif text[j] == ')':
                        depth -= 1
                    j += 1
                inner = text[i+1:j-1]
                result.append('(' + self._transformOperators(inner) + ')')
                i = j
            else:
                result.append(text[i])
                i += 1
        return ''.join(result)

    def _convertExpression(self, rowDict, statement) -> str:
        # 1. Replace atomic variables with bit values
        expr = statement
        for var, bit in rowDict.items():
            expr = expr.replace(var, bit)
 
        # 2. Handle -> and <> with parenthesis-aware transformer
        expr = self._transformOperators(expr)
 
        # 3. Now replace ^, v, ~ (safe to do here — no -> or <> left)
        for operator, equivalence in self.logicalOperators.items():
            expr = expr.replace(operator, equivalence)
 
        return expr

    def evaluateExpression(self, statement = None) -> list:
        statement = statement or self.statement

        # Step 4.3 : Evaluate the resulting strings
        # since statements are converted into statement that python can read 
        # we can now evaluate it using eval()
        evaluated = [] 
        mappedVariables = self._mapVariablesToTruthValues()
        for var in mappedVariables:
            converted = self._convertExpression(var, statement)
            result = eval(converted, {"implies": self.implies, "biconditional": self.biconditional})
            evaluated.append(result)
        
        # Step 4.4 : result is 0 or 1
        return evaluated # return list of compound proposition
    
    def evaluateClassification(self) -> str:
        # Step 4.5 : Evaluate the classification of compound proposition
        evaluated = self.evaluateExpression()
        firstValue = evaluated[0]
        for i in range(1, len(evaluated)):
            if(firstValue != evaluated[i]):
                return "Contingency"

        if(firstValue == 0):
            return "Contradiction"

        return "Tautology"

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
    STEP 5 : GET THE OUTPUT TO PASS SOMEWHERE
    """
    def getTruthTable(self) -> str:
        truthTable = ""
        subexpressionLength = []
        statementLength : int = len(self.statement)
        extractedBits = self._evaluateExtractedExpressions()

        # Header
        for char in self.atomicVariables.strip():
            truthTable += f"{char:^3}|"
        for sentence in self._extractExpressions():
            truthTable += f"({sentence})|"
            subexpressionLength.append(len(sentence))
        truthTable += self.statement + '\n'

        # Body
        for row in range(self.rowsCount):
            for byte in self.binaryRows[row]:
                truthTable += f"{byte:^3}|"
            
            count = 0
            for bits in extractedBits: 
                truthTable += f"{bits[row]:^{subexpressionLength[count]+2}}|"
                
                count += 1

            finalAnswer = self.evaluateExpression()
            truthTable += f"{finalAnswer[row]:^{statementLength+1}}" + '\n'

        return truthTable



