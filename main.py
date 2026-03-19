from propositional_logic import PropositionalLogic

def main():
    logic = PropositionalLogic("(p v q) v (q ^ r)")
    print(logic.variableCount)
    listTo = logic.readThroughParenthesis()
    print(listTo)

if __name__ == "__main__":
    main()