def allocateResources():

    repress = input("Repress: ")
    if repress == "":
        repress = 0
    else:
        repress = int(repress)

    surveil = input("Surveil: ")
    if surveil == "":
        surveil = 0
    else:
        surveil = int(surveil)

    support = input("Support: ")
    if support == "":
        support = 0
    else:
        support = int(support)

    return repress, surveil, support