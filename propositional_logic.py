class PropositionalLogic:
    def __init__(self, statement: str):
        self.statement = statement.strip()
        self.variableCount = self._countVariable()
        self.rowsCount = self._numberOfRows()

    # 
    # STEP 1 : IDENTIFY ALL THE UNIQUE ATOMIC VARIABLE
    #
    def _countVariable(self) -> int:
        atomicVariables = set()
        count = 0
        for char in self.statement:
            # checks if char is alphabet, and not letter 'v', and is not in atomicVariables
            if char.isalpha() and char != 'v' and char not in atomicVariables:
                atomicVariables.add(char)
                count += 1
        
        return count

    #
    # STEP 2 : DETERMINE THE NUMBER OF ROWS
    #
    def _numberOfRows(self): return 2 ** self.variableCount

    #
    # STEP 3 : FILL ALL THE COLUMN WITH VALUES (0, 1)
    #
    def generateTruthTable(self):
        binaryHolder = []
        listOfBinary = []

        # assigning binaries on the binaryHolder array 
        # ['00', '01', '10' '11']
        for i in range(self.rowsCount):
            binaryHolder.append(f"{i:0{self.variableCount}b}")

        # destructuring the binaryHolder of every digit 
        # [['0', '0'], ['0', '1'], ['1', '0'], ['1', '1']]
        for digit in range(len(binaryHolder)):
            count = 0
            tempArr = []
            for index in range(self.variableCount):
                temp = binaryHolder[digit][index]
                tempArr.append(temp)
                count += 1

                if count >= self.variableCount:
                    listOfBinary.append(tempArr)

        return listOfBinary

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
                print(text)
                textArray.append(text)
                firstIndex = 0
                lastIndex = 0
                text = ""

        return textArray