from Game import Game
from Colors import Colors

def main():
    statement = [
            "(p v q) ^ (~q ^ r)", 
            "(~q ^ ~p) -> (~p v q) v r",
            "(~q ^ p) v r",
            "(p ^ q) ^ r",
            "~(q ^ p) v (q v r)",
            "(p ^ q) v ~(q v r)",
            "(q v p) ^ (~p v r)",
            "(p -> q) ^ (q -> r)",
            "(~q -> p) v ~r",
            "(p ^ r) -> (~q v r)"]

    g = Game()
    print(g.run())

if __name__ == "__main__":
    main()
