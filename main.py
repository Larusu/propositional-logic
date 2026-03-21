from propositional_logic import PropositionalLogic

def main():
    logic = PropositionalLogic("(p v q) v (q ^ r)")
    print(logic.printTruthTable())

if __name__ == "__main__":
    main()
