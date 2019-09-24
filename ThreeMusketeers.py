
def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]
    return board

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    x=[None] * 2
    if s[0]=='A':
        x[0]=0
    elif s[0] == 'B':
        x[0] = 1
    elif s[0] == 'C':
        x[0] = 2
    elif s[0] == 'D':
        x[0]=3
    elif s[0] == 'E':
        x[0] = 4
    for i in s[1]:
        temp=int(i)
        x[1]=temp-1
    x=list(x)
    return x

def location_to_string(location):
    x='**'
    x=list(x)
    if location[0]=='0':
        x[0]='A'
    elif location[0]=='1':
        x[0]='B'
    elif location[0]=='2':
        x[0]='C'
    elif location[0]=='3':
        x[0]='D'
    elif location[0] == '4':
        x[0] = 'E'
    for i in location[1]:
        temp=int(i)+1
        x[1]=str(temp)
    x=''.join(x)
    return x

def all_locations():
    matrix=[[0 for x in range(5)] for y in range(5)]
    for i in range(5):
        for j in range(5):
            matrix[i][j]=i,j

def adjacent_location(location,direction):
    row,col=location
    if(direction=='U'):
        row=row+1
    elif direction=='D':
        row=row-1
    elif direction=='L':
        col=col-1
    elif direction=='R':
        col=col+1
    new_location=[None]*2
    new_location[0]=row
    new_location[1]=col
    return  new_location

def is_legal_move_by_musketeer(location,direction):
    row,col=location
    if(board[row][col]=='M'):
        mrow,mcol=adjacent_location(location,direction)
        if is_legal_location([mrow,mcol]):
            if(board[mrow][mcol]=='R'):
                return True
    return False

def is_legal_move_by_enemy(location,direction):
    row,col=location
    if(board[row][col]=='R'):
        erow,ecol=adjacent_location(location,direction)
        if is_legal_location([erow,ecol]):
            if(board[erow][ecol]=='-'):
                return True
    return False

def has_some_legal_move_somewhere(who):
    if who=='M':
        for i in range(5):
            for j in range(5):
                if board[i][j]=='M':
                    if is_legal_move_by_musketeer([i,j],"U") or is_legal_move_by_musketeer([i,j],"D") or is_legal_move_by_musketeer([i,j],"R") or is_legal_move_by_musketeer([i,j],"L"):
                        return True
    if who=='R':
        for i in range(5):
            for j in range(5):
                if board[i][j]=='R':
                    if is_legal_move_by_enemy([i,j],"U") or is_legal_move_by_enemy([i,j],"D") or is_legal_move_by_enemy([i,j],"R") or is_legal_move_by_enemy([i,j],"L"):
                        return True

def is_legal_location(location):
    row,col=location
    if row>=0 and row<=4 and col>=0 and col<=4:
        return True
    else:
        return False

def possible_moves_from(location):
    moves=[]
    row,col=location
    if board[row][col]!='M' and board[row][col]!='R':
        temp=[[]]
        moves.append(temp)
        return moves
    elif board[row][col]=='M':
        if (is_legal_move_by_musketeer(location,"L")==True):
            temp=(location,"L")
            moves.append(temp)
        if (is_legal_move_by_musketeer(location,"R")==True):
            temp=(location,"R")
            moves.append(temp)
        if (is_legal_move_by_musketeer(location,"U")==True):
            temp=(location,"U")
            moves.append(temp)
        if (is_legal_move_by_musketeer(location,"D")==True):
            temp=(location,"D")
            moves.append(temp)
    elif board[row][col]=='R':
        if (is_legal_move_by_enemy(location,"L")==True):
            temp=(location,"L")
            moves.append(temp)
        if (is_legal_move_by_enemy(location,"R")==True):
            temp=(location,"R")
            moves.append(temp)
        if (is_legal_move_by_enemy(location,"U")==True):
            temp=(location,"U")
            moves.append(temp)
        if (is_legal_move_by_enemy(location,"D")==True):
            temp=(location,"D")
            moves.append(temp)
    return moves

def can_move_piece_at(location):
    x=possible_moves_from(location)
    if len(x)==0:
        return False
    else:
        return True

def is_within_board(location,direction):
    nrow,ncol=adjacent_location(location,direction)
    if is_legal_location([nrow,ncol]):
        return True
    else:
        return False

def is_legal_move(location,direction):
    row,col=location
    if board[row][col]=='M':
        if is_legal_move_by_musketeer([row,col],direction)==True:
            return True
        else:
            return False
    elif board[row][col]=='R':
        if is_legal_move_by_enemy([row,col],direction)==True:
            return True
        else:
            return False
    return False

def all_possible_moves_for(player):
    all_moves=[]
    if player=='M':
        if has_some_legal_move_somewhere('M')==True:
            for i in range(5):
                for j in range(5):
                    if board[i][j]=='M':
                        temp=possible_moves_from([i,j])
                        all_moves.append(temp)
    elif player=='R':
        if has_some_legal_move_somewhere('R')==True:
            for i in range(5):
                for j in range(5):
                    if board[i][j]=='R':
                        temp=possible_moves_from([i,j])
                        all_moves.append(temp)
    return all_moves

def make_move(location,direction):
    row,col=location
    if board[row][col]=='M':
        if is_legal_move_by_musketeer(location,direction):
            mrow,mcol=adjacent_location(location,direction)
            board[row][col]='-'
            board[mrow][mcol]='M'
    elif board[row][col]=='R':
        if is_legal_move_by_enemy(location,direction):
            mrow,mcol=adjacent_location(location,direction)
            board[row][col]='-'
            board[mrow][mcol]='R'

def choose_computer_move(who):
    a=all_possible_moves_for(who)
    x=next(i for i, j in enumerate(a) if j)
    temp1=list(a[x][0])
    loc=temp1[0]
    dir=temp1[1]
    return (loc,dir)

def is_enemy_win():
    loc=[]
    for i in range(5):
        for j in range(5):
            if board[i][j]=='M':
                loc.extend([i,j])
    if (loc[0]==loc[2]==loc[4]) or (loc[1]==loc[3]==loc[5]):
         return True
    else:
        return False

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|",end=" ")
        for j in range(0, 5):
            print(board[i][j] + " ", end= " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        temp=''.join(move[0:2])
        location = string_to_location(move[0:2])
        if is_legal_move(location, move[2]):
            return (location, move[2])
    print("Illegal move--'" + move + "'")
    return get_users_move()

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    location=list(location)
    new_location = adjacent_location(location, direction)
    new_location=list(new_location)
    s = [str(i) for i in location]
    s2=[str(i) for i in new_location]
    temp1=''.join(s)
    temp2=''.join(s2)
    print(who, 'moves', direction, 'from',\
          location_to_string(temp1), 'to',\
          location_to_string(temp2) + ".\n")

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        row,col=location
        if board[row][col] == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)

def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        row,col=location
        if board[row][col] == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break

start()

