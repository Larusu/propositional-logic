from propositional_logic import PropositionalLogic

def main():
    logic = PropositionalLogic("(p v q) v (q ^ r)")
    print(logic.variableCount)
    idontknow = logic.mapVariablesToTruthValues()
    print(f"ito na yung change: {idontknow}")

if __name__ == "__main__":
    main()
