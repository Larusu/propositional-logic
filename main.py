from propositional_logic import PropositionalLogic

def main():
    logic = PropositionalLogic("~(~p v q) v (q ^ r)")
    logic.printTruthTable()
    logic1 = PropositionalLogic("(p v q) ^ (q ^ r) v (p v 0)")
    logic1.printTruthTable()
    logic3 = PropositionalLogic("(~p ^ 1) v 0")
    logic3.printTruthTable()
if __name__ == "__main__":
    main()
