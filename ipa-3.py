'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_graphF = social_graph[from_member]["following"]
    social_graphT = social_graph[to_member]["following"]
    if to_member in social_graphF and from_member in social_graphT:
        return "friends"
    elif to_member in social_graphF:
        return "follower"
    elif from_member in social_graphT:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    secCOM = list ()
    ROWcounter = 0
    while ROWcounter < len(board):
        WORKin = "C" + str(ROWcounter)
        WORKin = list()
        INDIcount = 0
        while INDIcount < len(board):
            WORKin.append(board[INDIcount][ROWcounter])
            INDIcount = INDIcount + 1
        ROWcounter = ROWcounter +1
        secCOM.append(WORKin)
    diaCOM1 = list()
    dCOUNTER = 0
    while dCOUNTER < len(board):
        diaCOM1.append(board[dCOUNTER][dCOUNTER])
        dCOUNTER = dCOUNTER + 1
    diaCOM2 = list()
    dCOUNTER2 = 0
    dCOUNTER3 = -1
    while dCOUNTER2 < len(board):
        diaCOM2.append(board[dCOUNTER2][dCOUNTER3])
        dCOUNTER2 = dCOUNTER2 + 1
        dCOUNTER3 = dCOUNTER3 - 1
    board = board + secCOM
    board.append(diaCOM1)
    board.append(diaCOM2)
    OPTs = ["X","O"]
    CHECK = list()
    for i in OPTs:
        checker = 0
        while checker < len(board):
            CHECK.append((i,(board[checker].count(i))))
            checker = checker + 1
    originaLEN = (len(board)-2)/2
    if ("X",originaLEN) in CHECK:
        return "X"
    elif ("O",originaLEN) in CHECK:
        return "O"
    else:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    TUP = (first_stop,second_stop)
    if TUP in route_map:
        return route_map[TUP]["travel_time_mins"]
    else:
        pure = list(route_map)
        for i in pure:
            if i[0] == first_stop:
                firstPAIR = i[1]
        FIRin = pure.index((first_stop,firstPAIR))
        for i in pure:
            if i[1] == second_stop:
                secondPAIR = i[0]
        SECin = pure.index((secondPAIR,second_stop))
        if FIRin < SECin:
            TOTmin = 0
            while FIRin < SECin + 1:
                TOTmin = TOTmin + route_map[pure[FIRin]]["travel_time_mins"]
                FIRin = FIRin + 1
            return TOTmin
        elif SECin < FIRin:
            TOTmin = 0
            while FIRin < len(pure):
                TOTmin = TOTmin + route_map[pure[FIRin]]["travel_time_mins"]
                FIRin = FIRin + 1
            INDICOUNT = 0
            while INDICOUNT < SECin + 1:
                TOTmin = TOTmin + route_map[pure[INDICOUNT]]["travel_time_mins"]
                INDICOUNT = INDICOUNT + 1
            return TOTmin
