from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or a knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # If AKnight then sentence is true, else if AKnave then sentence is false
    Or(
        And(AKnight, And(AKnight, AKnave)),
        And(AKnave, Not(And(AKnight, AKnave)))
    )
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a knight or a knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # B is either a knight or a knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # If AKnight then both A and B are knave, else false
    Or(
        And(AKnight, And(AKnave, BKnave)),
        And(AKnave, Not(And(AKnave, BKnave)))
    )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either a knight or a knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # B is either a knight or a knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # if AKnight then both A and B are same, else A and B are different
    Or(
        And(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
        And(AKnave, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
    ),

    # if BKnight then A and B are different, else A and B are same
    Or(
        And(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
        And(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave)))
    )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is either a knight or a knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # B is either a knight or a knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # C is either a knight or a knave, but not both
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),

    Or(
        # if a said "Im a knight"
        Or(
            And(AKnight, AKnight),
            And(AKnave, AKnave)
        ),
        # if a said "Im a knave"
        Or(
            And(AKnight, AKnave),  # contradiction
            And(AKnave, AKnight)  # contradiction
        )
    ),

    Or(
        # if BKnight, then A said "Im a knave"
        And(BKnight, Or(
            And(AKnight, AKnave),
            And(AKnave, AKnight)
        )),
        # if BKnave, then A said "Im a knight"
        And(BKnave, Or(
            And(AKnight, AKnight),
            And(AKnave, AKnave)
        ))
    ),

    Or(
        # if BKnight, then C is a knave
        And(BKnight, CKnave),
        # if BKnave, then C is a knight
        And(BKnave, CKnight)
    ),

    Or(
        # if CKnight, then A is a knight
        And(CKnight, AKnight),
        # if CKnave, then A is a knave
        And(CKnave, AKnave)
    )
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
