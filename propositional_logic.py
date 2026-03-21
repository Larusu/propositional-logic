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

    def mapVariablesToTruthValues(self) -> list:
        atomicVariables = self.atomicVariables
        columnValues = self.binaryRows
        changedVariables = []
        
        # Assignign all the atomicVariables with its truth values equivalence
        # p = 0, q = 0, r = 1
        for row in range(len(columnValues)):
            temp = {}
            for i in range(len(atomicVariables)):
                temp[atomicVariables[i]] = int(columnValues[row][i])
            changedVariables.append(temp)

        return changedVariables


