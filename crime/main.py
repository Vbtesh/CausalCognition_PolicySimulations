from scripts.neighbourhood import Neighbourhood
from scripts.cmdLineUtils import allocateResources

gameTest = Neighbourhood()

turn = 1
while True:
    print(f"\nTurn {turn}")
    gameTest.printState()
    print("")

    repress, surveil, support = allocateResources()

    print("\nApplying resources...")
    gameTest.calcNewState(repress, surveil, support)
    gameTest.printState()

    print("\nApplying rates...")
    gameTest.applyRates()

    turn += 1

pass