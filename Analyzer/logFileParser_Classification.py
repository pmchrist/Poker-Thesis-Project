
import os
import datetime
import copy
from treys import Card
from treys import Evaluator

# Each game comes with its start date
dateTimeFormat = "%Y-%m-%d %H:%M:%S.%f"
# To decode card ids we need a lookup array
index2card = ['As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks',
            'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh',
            'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd',
            'Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc']

# Starting hand combination quality is predefined, we just have to check 2 cards and get value
def TwoCardHandEval(card1, card2):
    pairQuality = 0.0
    card1Rank = Card.get_rank_int(card1)
    card2Rank = Card.get_rank_int(card2)

    # Swap cards if rank2 is highest
    if (card2Rank > card1Rank):
        cardTempRank = card1Rank
        card1Rank = card2Rank
        card2Rank = cardTempRank

    # Check for each possible card combination
    if (card1Rank == 12):
        if (card2Rank == 12):
            pairQuality = 0.85
        elif (card2Rank == 11):
            pairQuality = 0.65
        elif (card2Rank == 10):
            pairQuality = 0.64
        elif (card2Rank == 9):
            pairQuality = 0.64
        elif (card2Rank == 8):
            pairQuality = 0.63
        elif (card2Rank == 7):
            pairQuality = 0.61
        elif (card2Rank == 6):
            pairQuality = 0.60
        elif (card2Rank == 5):
            pairQuality = 0.59
        elif (card2Rank == 4):
            pairQuality = 0.58
        elif (card2Rank == 3):
            pairQuality = 0.58
        elif (card2Rank == 2):
            pairQuality = 0.56
        elif (card2Rank == 1):
            pairQuality = 0.56
        elif (card2Rank == 0):
            pairQuality = 0.55
    if (card1Rank == 11):
        if (card2Rank == 11):
            pairQuality = 0.82
        elif (card2Rank == 10):
            pairQuality = 0.61
        elif (card2Rank == 9):
            pairQuality = 0.61
        elif (card2Rank == 8):
            pairQuality = 0.60
        elif (card2Rank == 7):
            pairQuality = 0.58
        elif (card2Rank == 6):
            pairQuality = 0.56
        elif (card2Rank == 5):
            pairQuality = 0.55
        elif (card2Rank == 4):
            pairQuality = 0.54
        elif (card2Rank == 3):
            pairQuality = 0.53
        elif (card2Rank == 2):
            pairQuality = 0.52
        elif (card2Rank == 1):
            pairQuality = 0.51
        elif (card2Rank == 0):
            pairQuality = 0.50
    if (card1Rank == 10):
        if (card2Rank == 10):
            pairQuality = 0.80
        elif (card2Rank == 9):
            pairQuality = 0.58
        elif (card2Rank == 8):
            pairQuality = 0.57
        elif (card2Rank == 7):
            pairQuality = 0.56
        elif (card2Rank == 6):
            pairQuality = 0.54
        elif (card2Rank == 5):
            pairQuality = 0.52
        elif (card2Rank == 4):
            pairQuality = 0.51
        elif (card2Rank == 3):
            pairQuality = 0.50
        elif (card2Rank == 2):
            pairQuality = 0.49
        elif (card2Rank == 1):
            pairQuality = 0.48
        elif (card2Rank == 0):
            pairQuality = 0.47
    if (card1Rank == 9):
        if (card2Rank == 9):
            pairQuality = 0.78
        elif (card2Rank == 8):
            pairQuality = 0.55
        elif (card2Rank == 7):
            pairQuality = 0.53
        elif (card2Rank == 6):
            pairQuality = 0.52
        elif (card2Rank == 5):
            pairQuality = 0.50
        elif (card2Rank == 4):
            pairQuality = 0.48
        elif (card2Rank == 3):
            pairQuality = 0.47
        elif (card2Rank == 2):
            pairQuality = 0.46
        elif (card2Rank == 1):
            pairQuality = 0.45
        elif (card2Rank == 0):
            pairQuality = 0.44
    if (card1Rank == 8):
        if (card2Rank == 8):
            pairQuality = 0.75
        elif (card2Rank == 7):
            pairQuality = 0.52
        elif (card2Rank == 6):
            pairQuality = 0.50
        elif (card2Rank == 5):
            pairQuality = 0.48
        elif (card2Rank == 4):
            pairQuality = 0.46
        elif (card2Rank == 3):
            pairQuality = 0.44
        elif (card2Rank == 2):
            pairQuality = 0.43
        elif (card2Rank == 1):
            pairQuality = 0.42
        elif (card2Rank == 0):
            pairQuality = 0.42
    if (card1Rank == 7):
        if (card2Rank == 7):
            pairQuality = 0.72
        elif (card2Rank == 6):
            pairQuality = 0.48
        elif (card2Rank == 5):
            pairQuality = 0.47
        elif (card2Rank == 4):
            pairQuality = 0.45
        elif (card2Rank == 3):
            pairQuality = 0.43
        elif (card2Rank == 2):
            pairQuality = 0.41
        elif (card2Rank == 1):
            pairQuality = 0.40
        elif (card2Rank == 0):
            pairQuality = 0.39
    if (card1Rank == 6):
        if (card2Rank == 6):
            pairQuality = 0.69
        elif (card2Rank == 5):
            pairQuality = 0.46
        elif (card2Rank == 4):
            pairQuality = 0.44
        elif (card2Rank == 3):
            pairQuality = 0.42
        elif (card2Rank == 2):
            pairQuality = 0.40
        elif (card2Rank == 1):
            pairQuality = 0.38
        elif (card2Rank == 0):
            pairQuality = 0.37
    if (card1Rank == 5):
        if (card2Rank == 5):
            pairQuality = 0.66
        elif (card2Rank == 4):
            pairQuality = 0.43
        elif (card2Rank == 3):
            pairQuality = 0.41
        elif (card2Rank == 2):
            pairQuality = 0.38
        elif (card2Rank == 1):
            pairQuality = 0.37
        elif (card2Rank == 0):
            pairQuality = 0.35
    if (card1Rank == 4):
        if (card2Rank == 4):
            pairQuality = 0.63
        elif (card2Rank == 3):
            pairQuality = 0.40
        elif (card2Rank == 2):
            pairQuality = 0.38
        elif (card2Rank == 1):
            pairQuality = 0.36
        elif (card2Rank == 0):
            pairQuality = 0.34
    if (card1Rank == 3):
        if (card2Rank == 3):
            pairQuality = 0.60
        elif (card2Rank == 2):
            pairQuality = 0.38
        elif (card2Rank == 1):
            pairQuality = 0.36
        elif (card2Rank == 0):
            pairQuality = 0.34
    if (card1Rank == 2):
        if (card2Rank == 2):
            pairQuality = 0.57
        elif (card2Rank == 1):
            pairQuality = 0.34
        elif (card2Rank == 0):
            pairQuality = 0.33
    if (card1Rank == 1):
        if (card2Rank == 1):
            pairQuality = 0.54
        elif (card2Rank == 0):
            pairQuality = 0.32
    if (card1Rank == 0):
        if (card2Rank == 0):
            pairQuality = 0.50
    
    return pairQuality

# All information needed to classify a game
class DoyleGame(object):
    nickname = None
    difficulty = None
    
    cardsHand = []
    cardsTable = []
    handQualityStart = 0.5
    handQualityEnd = 0.5

    actions = 0
    fold = 0
    allin = 0
    calls = 0
    callsPercent = 0.0
    raises = 0
    raisesPercent = 0.0

    betted = 0
    pot = 0.0
    chipsCoeff = 0
    payoff = 0

    won = 0

    def findMeta(self):
        # If game was empty, we need to avoid division by zero
        if (self.pot == 0): self.pot = 1
        if (self.actions == 0): self.actions = 1

        # Finding some simple meta values
        if (self.payoff > 0): self.won = 1
        self.chipsCoeff = round(self.betted / self.pot, 3)
        self.callsPercent = round(self.calls / self.actions, 3)
        self.raisesPercent = round(self.raises / self.actions, 3)

        # Analyzing cards that have been delt in game
        hand = []
        for i in range(len(self.cardsHand)):
            hand.append(Card.new(index2card[self.cardsHand[i]]))
        board = []
        for i in range(len(self.cardsTable)):
            board.append(Card.new(index2card[self.cardsTable[i]]))
        # Evaluate Hand at the start and end
        if (len(board) > 2 and len(hand) > 0):
            self.handQualityStart = TwoCardHandEval(hand[0], hand[1])
            evaluator = Evaluator()
            self.handQualityEnd = round(evaluator.evaluate(board, hand) / 7462, 3)
        elif (len(hand) > 0):
            self.handQualityStart = TwoCardHandEval(hand[0], hand[1])
            self.handQualityEnd = 0.0

    def getArrayForPlayer(self):
        tempArray = []
        tempArray.append(self.nickname)
        tempArray.append(self.actions)
        tempArray.append(self.fold)
        tempArray.append(self.allin)
        tempArray.append(self.calls)
        tempArray.append(self.raises)
        tempArray.append(self.betted)
        tempArray.append(self.pot)
        tempArray.append(self.payoff)
        tempArray.append(self.won)
        return(tempArray)

    def getArrayForClustering(self):
        tempArray = []
        tempArray.append(self.nickname)
        tempArray.append(self.difficulty)
        tempArray.append(self.handQualityStart)
        tempArray.append(self.handQualityEnd)
        tempArray.append(self.callsPercent)
        tempArray.append(self.raisesPercent)
        tempArray.append(self.chipsCoeff)
        return(tempArray)

    def getArrayForClassifying(self):
        tempArray = []
        tempArray.append(self.handQualityStart)
        tempArray.append(self.handQualityEnd)
        tempArray.append(self.callsPercent)
        tempArray.append(self.raisesPercent)
        tempArray.append(self.chipsCoeff)
        return(tempArray)

    def __str__(self):
        return("nickname: " + str(self.nickname) +
            "\nhandQualityStart: " + str(self.handQualityStart) +
            "\nhandQualityEnd: " + str(self.handQualityEnd) +
            "\ncallsPercent: " + str(self.callsPercent) +
            "\nraisesPercent: " + str(self.raisesPercent) +
            "\nchipsCoeff: " + str(self.chipsCoeff) + "\n")

# All information needed to classify a player
class PlayerProfile(object):
    nickname = None
    gamesPlayed = 0

    actions = 0
    folds = 0.0
    foldsPercent = 0.0
    allins = 0.0
    allinsPercent = 0.0
    calls = 0.0
    callsPercent = 0.0
    raises = 0.0
    raisesPercent = 0.0

    bettedOverall = 0.0
    potOverall = 0.0
    chipsCoeff = 0.0
    payoffOverall = 0.0
    payoff = 0.0

    wins = 0.0
    winRate = 0.0

    def __init__(self, name):
        self.nickname = name

    def findMeta(self):
        if (self.gamesPlayed == 0): self.gamesPlayed = 1
        if (self.actions == 0): self.actions = 1
        if (self.bettedOverall == 0): self.bettedOverall = 1
        self.foldsPercent = round(self.folds / self.actions, 3)
        self.allinsPercent = round(self.allins / self.actions, 3)
        self.callsPercent = round(self.calls / self.actions, 3)
        self.raisesPercent = round(self.raises / self.actions, 3)
        self.chipsCoeff = round(self.bettedOverall / self.potOverall, 3)
        self.payoff = round(self.payoffOverall / self.potOverall, 3)   # How many chips won proportionally to all pot
        self.winRate = round(self.wins / self.gamesPlayed, 3)   # How many games were won

    def getArrayForClustering(self):
        tempArray = []
        tempArray.append(self.nickname)
        tempArray.append(self.foldsPercent)
        tempArray.append(self.allinsPercent)
        tempArray.append(self.callsPercent)
        tempArray.append(self.raisesPercent)
        tempArray.append(self.chipsCoeff)
        tempArray.append(self.payoff)
        return(tempArray)

    def getArrayForClassifying(self):
        tempArray = []
        tempArray.append(self.foldsPercent)
        tempArray.append(self.allinsPercent)
        tempArray.append(self.callsPercent)
        tempArray.append(self.raisesPercent)
        tempArray.append(self.chipsCoeff)
        tempArray.append(self.payoff)
        return(tempArray)


# Start of analyzer
os.system('cls')
# Reading file
logName = "AllLogs.log"
dirname = os.path.dirname(__file__)
pathlist = os.path.join(dirname, logName)
gamesPlayed = []

# Parse path object to string
# Parse Humans
with open(pathlist) as f:
    logLines = f.readlines()
    # Read first line
    for content in logLines:
        try:
            # Reading date of game
            date = datetime.datetime.strptime(content.rstrip(), dateTimeFormat)
            # If we got no errors it means that line was actually a date.
            # So, next lines are from a new game session.
        except ValueError as err:
            lineContent = content.rstrip().split("|")
            # If Start line
            if (lineContent[0] == "Start"):
                # Declare a new game
                # Reset
                doyleGame = DoyleGame()
                playerBudgetPrevious = 100000
                # Nickname
                nickname = lineContent[1]
                doyleGame.nickname = nickname
                # Difficulty (AI nickname)
                difficulty = lineContent[2]
                doyleGame.difficulty = difficulty
                # GameMode
                gameMode = lineContent[3]
            # If Action line
            elif (lineContent[0] == "PlayerAction"):
                doyleGame.actions += 1
                if (lineContent[1] == "0"):
                    doyleGame.fold = 1
                elif (lineContent[1] == "1" or lineContent[1] == "2"):
                    doyleGame.calls += 1
                elif (lineContent[1] == "3" or lineContent[1] == "4"):
                    doyleGame.raises += 1
                elif (lineContent[1] == "5"):
                    doyleGame.allin = 1
            # If End line
            elif ((lineContent[0] == "RoundOver" and gameMode == "Normal") or (lineContent[0] == "End" and gameMode == "Doyle")):
                # Game ended, lets find metadata and save it
                doyleGame.payoff = int(float(lineContent[1]))
                doyleGame.findMeta()
                # And save it
                gamesPlayed.append(copy.deepcopy(doyleGame))
                # Declare a new game
                doyleGame = DoyleGame()
                playerBudgetPrevious = 100000
                # Nickname
                doyleGame.nickname = nickname
                # Difficulty (AI nickname)
                doyleGame.difficulty = difficulty
            # If just update line
            elif (lineContent[0] == "0" or lineContent[0] == "1" or lineContent[0] == "2" or lineContent[0] == "3"):
                # Save pot and table cards
                if (doyleGame.pot < int(lineContent[1])): doyleGame.pot = int(lineContent[1]) 
                if (lineContent[2] != ""): doyleGame.cardsTable = list(eval(lineContent[2]))
                # Save player pot and budget
                if (int(lineContent[3]) < playerBudgetPrevious):
                    if (playerBudgetPrevious != 100000):
                        doyleGame.betted += (playerBudgetPrevious - int(lineContent[3]))
                    playerBudgetPrevious = int(lineContent[3])
                if (lineContent[4] != ""): doyleGame.cardsHand = list(eval(lineContent[4]))
f.close()
#Parse AIs
with open(pathlist) as f:
    logLines = f.readlines()
    # Read first line
    for content in logLines:
        try:
            # Reading date of game
            date = datetime.datetime.strptime(content.rstrip(), dateTimeFormat)
            # If we got no errors it means that line was actually a date.
            # So, next lines are from a new game session.
        except ValueError as err:
            lineContent = content.rstrip().split("|")
            # If Start line
            if (lineContent[0] == "Start"):
                # Declare a new game
                # Reset
                doyleGame = DoyleGame()
                playerBudgetPrevious = 100000
                # Nickname
                nickname = lineContent[1]
                if ("tightAggressive" in lineContent[1] or "tightPassive" in lineContent[1] or "looseAggressive" in lineContent[1] or "loosePassive" in lineContent[1]):
                    nickname = lineContent[1]
                else:
                    nickname = lineContent[2]
                doyleGame.nickname = nickname
                # Difficulty (AI nickname)
                difficulty = lineContent[2]
                doyleGame.difficulty = difficulty
                # GameMode
                gameMode = lineContent[3]
            # If End line
            elif ((lineContent[0] == "RoundOver" and gameMode == "Normal") or (lineContent[0] == "End" and gameMode == "Doyle")):
                # Game ended, lets find metadata and save it
                doyleGame.payoff = int(float(lineContent[1]))
                doyleGame.findMeta()
                # And save it
                gamesPlayed.append(copy.deepcopy(doyleGame))
                # Declare a new game
                doyleGame = DoyleGame()
                playerBudgetPrevious = 100000
                # Nickname
                doyleGame.nickname = nickname
                # Difficulty (AI nickname)
                doyleGame.difficulty = difficulty
            # If just update line
            elif (lineContent[0] == "0" or lineContent[0] == "1" or lineContent[0] == "2" or lineContent[0] == "3"):
                # Save pot and table cards
                if (doyleGame.pot < int(lineContent[1])): doyleGame.pot = int(lineContent[1]) 
                if (lineContent[2] != ""): doyleGame.cardsTable = list(eval(lineContent[2]))
                # Save player pot and budget
                if (int(lineContent[5]) < playerBudgetPrevious):
                    if (playerBudgetPrevious != 100000):
                        doyleGame.betted += (playerBudgetPrevious - int(lineContent[5]))
                    playerBudgetPrevious = int(lineContent[5])
                if (lineContent[4] != ""): doyleGame.cardsHand = list(eval(lineContent[6]))
                # If line contains AI Action
                if (lineContent[8] == "Enemy"):
                    doyleGame.actions += 1
                    if (lineContent[9] == "0"):
                        doyleGame.fold = 1
                    elif (lineContent[9] == "1" or lineContent[1] == "2"):
                        doyleGame.calls += 1
                    elif (lineContent[9] == "3" or lineContent[1] == "4"):
                        doyleGame.raises += 1
                    elif (lineContent[9] == "5"):
                        doyleGame.allin = 1
f.close()

# Creating Dataframes for Clustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Extract array for classification from all played games
arrayForClustering = []
AIbettedGames = []
AIwinRate = []
for game in gamesPlayed:
    arrayForClustering.append(game.getArrayForClustering())
    AIbettedGames.append(game.pot - game.betted)
    AIwinRate.append(game.payoff * -1)
arrayForClustering = np.array(arrayForClustering)
# And create a dataframe
df_full_games = pd.DataFrame(arrayForClustering, columns = ['nickname', 'difficulty', 'handQualityStart', 'handQualityEnd', 'callsPercent', 'raisesPercent', 'chipsCoeff'])
df_games = df_full_games.drop(columns=['nickname', 'difficulty'])

# Extracting data from games to create player profiles
playerNicknames = df_full_games['nickname'].unique()
arrayForPlayers = []
for game in gamesPlayed:
    arrayForPlayers.append(game.getArrayForPlayer())
# Creating player profiles
arrayOfPlayers = []
for nickname in playerNicknames:
    currentPlayer = PlayerProfile(nickname)
    for gameArray in arrayForPlayers:
        if (gameArray[0] == nickname):
            currentPlayer.gamesPlayed += 1
            currentPlayer.actions += gameArray[1]
            currentPlayer.folds += gameArray[2]
            currentPlayer.allins += gameArray[3]
            currentPlayer.calls += gameArray[4]
            currentPlayer.raises += gameArray[5]
            currentPlayer.bettedOverall += gameArray[6]
            currentPlayer.potOverall += gameArray[7]
            currentPlayer.payoffOverall += gameArray[8]
            currentPlayer.wins += gameArray[9]
    currentPlayer.findMeta()
    arrayOfPlayers.append(copy.deepcopy(currentPlayer))
# Array of players for Classification
arrayOfPlayersForClusterting = []
for player in arrayOfPlayers:
    arrayOfPlayersForClusterting.append(np.array(player.getArrayForClustering()))
# Creating Dataframe of players
df_full_players = pd.DataFrame(arrayOfPlayersForClusterting, columns = ['nickname', 'foldsPercent', 'allinsPercent', 'callsPercent', 'raisesPercent', 'chipsCoeff', 'payoff'])
df_players = df_full_players.drop(columns=['nickname'])

print("Actions Collected:\n")
for player in arrayOfPlayers:
    print(str(player.nickname) + ": " + str(player.actions))
print("\n")

# DECLARE WHOM WE ARE ANALYZING

classificationTarget = "Players"
#classificationTarget = "Games"
class_names_target = ['tightAggressive', 'tightPassive', 'looseAggressive', 'loosePassive']

if (classificationTarget == "Players"):
    # Extract arrays with Test and Train data for classification from all Players
    arrayForClassificationPlayerX = []
    arrayForClassificationPlayerY = []
    for player in arrayOfPlayers:
        if ("tightAggressive" in player.nickname):
            arrayForClassificationPlayerX.append(player.getArrayForClassifying())
            arrayForClassificationPlayerY.append(0)
        if ("tightPassive" in player.nickname):
            arrayForClassificationPlayerX.append(player.getArrayForClassifying())
            arrayForClassificationPlayerY.append(1)
        if ("looseAggressive" in player.nickname):
            arrayForClassificationPlayerX.append(player.getArrayForClassifying())
            arrayForClassificationPlayerY.append(2)
        if ("loosePassive" in player.nickname):
            arrayForClassificationPlayerX.append(player.getArrayForClassifying())
            arrayForClassificationPlayerY.append(3)
    arrayForClassificationPlayerX = np.array(arrayForClassificationPlayerX)
    arrayForClassificationPlayerY = np.array(arrayForClassificationPlayerY)
    # Assigning final values
    X = arrayForClassificationPlayerX
    Y = arrayForClassificationPlayerY
    df_full = df_full_players.copy()
    df = df_players.copy()
    # Declaring features for training and visualization of original data
    feature_names = ['foldsPercent', 'allinsPercent', 'callsPercent', 'raisesPercent', 'chipsCoeff', 'payoff']
    df_train = pd.DataFrame({'foldsPercent': X[:, 0], 'allinsPercent': X[:, 1], 'callsPercent': X[:, 2], 'raisesPercent': X[:, 3], 'chipsCoeff': X[:, 4], 'payoff': X[:, 5]})
    
if (classificationTarget == "Games"):
    # Extract arrays with Test and Train data for classification from all played Games
    arrayForClassificationGameX = []
    arrayForClassificationGameY = []
    for game in gamesPlayed:
        if ("tightAggressive" in game.nickname):
            arrayForClassificationGameX.append(game.getArrayForClassifying())
            arrayForClassificationGameY.append(0)
        if ("tightPassive" in game.nickname):
            arrayForClassificationGameX.append(game.getArrayForClassifying())
            arrayForClassificationGameY.append(1)
        if ("looseAggressive" in game.nickname):
            arrayForClassificationGameX.append(game.getArrayForClassifying())
            arrayForClassificationGameY.append(2)
        if ("loosePassive" in game.nickname):
            arrayForClassificationGameX.append(game.getArrayForClassifying())
            arrayForClassificationGameY.append(3)
    arrayForClassificationGameX = np.array(arrayForClassificationGameX)
    arrayForClassificationGameY = np.array(arrayForClassificationGameY)
    # Assigning final values
    X = arrayForClassificationGameX
    Y = arrayForClassificationGameY
    df_full = df_full_games.copy()
    df = df_games.copy()
    # Declaring features for training and visualization of original data
    feature_names = ['handQualityStart', 'handQualityEnd', 'callsPercent', 'raisesPercent', 'chipsCoeff']
    df_train = pd.DataFrame({'handQualityStart': X[:, 0], 'handQualityEnd': X[:, 1], 'callsPercent': X[:, 2], 'raisesPercent': X[:, 3], 'chipsCoeff': X[:, 4]})


# Explicitly save dataframe values as floats (Otherwise we have a bug)
if (classificationTarget == "Players"):
    df_full.iloc[:, 1] = pd.to_numeric(df_full.iloc[:, 1], downcast="float")
df_full.iloc[:, 2] = pd.to_numeric(df_full.iloc[:, 2], downcast="float")
df_full.iloc[:, 3] = pd.to_numeric(df_full.iloc[:, 3], downcast="float")
df_full.iloc[:, 4] = pd.to_numeric(df_full.iloc[:, 4], downcast="float")
df_full.iloc[:, 5] = pd.to_numeric(df_full.iloc[:, 5], downcast="float")
df_full.iloc[:, 6] = pd.to_numeric(df_full.iloc[:, 6], downcast="float")
df = df.apply(pd.to_numeric, errors='coerce')


#############################################################################################

# CLASSIFICATION

# Creating Train and Test datasets with KFold to check classifier Metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
if (classificationTarget == "Players"):
    splits = 2
if (classificationTarget == "Games"):
    splits = 5
skf = StratifiedKFold(n_splits=splits)
skf.get_n_splits(X,Y)
StratifiedKFold(n_splits=splits, random_state=42, shuffle=True)
for train_index, test_index in skf.split(X,Y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = Y[train_index], Y[test_index]

# Tree Classifier
from sklearn import tree

clf = tree.DecisionTreeClassifier()

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Tree F1: " + str(f1_score(y_test, y_pred, average=None)))
print("Tree Accuracy: " + str(accuracy_score(y_test, y_pred, normalize=True)))

clf = clf.fit(X, Y)
labelTree = clf.predict(df)

# Save Tree
plt.figure(figsize=(120,30))
tree.plot_tree(clf,
                   feature_names=feature_names,  
                   class_names=class_names_target,
                   fontsize=8.5,
                   filled=True)
plt.savefig(os.path.join(dirname, "treeClassifier.png"), bbox_inches='tight')
# Add new labels
df_full["labelTree"] = labelTree.astype(str)


 # SVM classifier

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

# Linear
clf = make_pipeline(StandardScaler(), LinearSVC(random_state=0, tol=1e-5))

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("SVM F1: " + str(f1_score(y_test, y_pred, average=None)))
print("SVM Accuracy: " + str(accuracy_score(y_test, y_pred, normalize=True)))

clf.fit(X, Y)
labelSVClinear = clf.predict(df)
# Add labels
df_full["labelSVClinear"] = labelSVClinear.astype(str)

# RBF kernel
clf = make_pipeline(StandardScaler(), SVC(kernel='rbf', gamma='scale', C=1.0))

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("SVM RBF F1: " + str(f1_score(y_test, y_pred, average=None)))
print("SVM RBF Accuracy: " + str(accuracy_score(y_test, y_pred, normalize=True)))

clf.fit(X, Y)
labelSVC = clf.predict(df)
# Add labels
df_full["labelSVC"] = labelSVC.astype(str)

# Gaussian
# It's a fuzzy classifier, it generates interesting results but to analyze them we need proper visualization
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
kernel = 1.0 * RBF(1.0)
gpc = GaussianProcessClassifier(kernel=kernel, random_state=0).fit(X, Y)
gpc.score(X, Y)
#print(gpc.predict_proba(df))

# Final dataframe
print(df_full)

# Some generic statistics related to games vs AI
if (classificationTarget == "Games"):
    # Adding game results
    df_full["betted"] = AIbettedGames
    df_full["payoff"] = AIwinRate
    # Gathering generic statistics
    gamesVeryHard = 0
    gamesVeryHard_0_betted = 0.0
    gamesVeryHard_0_payoff = 0.0
    gamesVeryHard_1_betted = 0.0
    gamesVeryHard_1_payoff = 0.0
    gamesVeryHard_2_betted = 0.0
    gamesVeryHard_2_payoff = 0.0
    gamesVeryHard_3_betted = 0.0
    gamesVeryHard_3_payoff = 0.0
    for index, row in df_full.iterrows():
        if (row['nickname'] != "Easy" and row['nickname'] != "Medium" and row['nickname'] != "Hard" and row['nickname'] != "Very Hard" and
        not("tightAggressive" in row['nickname']) and not("tightPassive" in row['nickname']) and not("looseAggressive" in row['nickname']) and not("loosePassive" in row['nickname'])):
            if (row['difficulty'] == "Very Hard"):
                gamesVeryHard += 1
                # If Player is tightAggressive
                if(row['labelTree'] == "0"):
                    gamesVeryHard_0_betted += row['betted']
                    gamesVeryHard_0_payoff += row['payoff']
                if(row['labelTree'] == "1"):
                    gamesVeryHard_1_betted += row['betted']
                    gamesVeryHard_1_payoff += row['payoff']
                if(row['labelTree'] == "2"):
                    gamesVeryHard_2_betted += row['betted']
                    gamesVeryHard_2_payoff += row['payoff']
                if(row['labelTree'] == "3"):
                    gamesVeryHard_3_betted += row['betted']
                    gamesVeryHard_3_payoff += row['payoff']
    print("\n")
    print("Games played vs CFR: " + str(gamesVeryHard))
    print("CFR winnings/betted vs tightAggressive: " + str(gamesVeryHard_0_betted/gamesVeryHard_0_payoff))
    print("CFR winnings/betted vs tightPassive: " + str(gamesVeryHard_1_betted/gamesVeryHard_1_payoff))
    print("CFR winnings/betted vs looseAggressive: " + str(gamesVeryHard_2_betted/gamesVeryHard_2_payoff))
    print("CFR winnings/betted vs loosePassive: " + str(gamesVeryHard_3_betted/gamesVeryHard_3_payoff))

    # Gathering generic statistics
    gamesHard = 0
    gamesHard_0_betted = 0.0
    gamesHard_0_payoff = 0.0
    gamesHard_1_betted = 0.0
    gamesHard_1_payoff = 0.0
    gamesHard_2_betted = 0.0
    gamesHard_2_payoff = 0.0
    gamesHard_3_betted = 0.0
    gamesHard_3_payoff = 0.0
    for index, row in df_full.iterrows():
        if (row['nickname'] != "Easy" and row['nickname'] != "Medium" and row['nickname'] != "Hard" and row['nickname'] != "Very Hard" and
        not("tightAggressive" in row['nickname']) and not("tightPassive" in row['nickname']) and not("looseAggressive" in row['nickname']) and not("loosePassive" in row['nickname'])):
            if (row['difficulty'] == "Hard"):
                gamesHard += 1
                # If Player is tightAggressive
                if(row['labelTree'] == "0"):
                    gamesHard_0_betted += row['betted']
                    gamesHard_0_payoff += row['payoff']
                if(row['labelTree'] == "1"):
                    gamesHard_1_betted += row['betted']
                    gamesHard_1_payoff += row['payoff']
                if(row['labelTree'] == "2"):
                    gamesHard_2_betted += row['betted']
                    gamesHard_2_payoff += row['payoff']
                if(row['labelTree'] == "3"):
                    gamesHard_3_betted += row['betted']
                    gamesHard_3_payoff += row['payoff']
    print("\n")
    print("Games played vs NFSP: " + str(gamesHard))
    print("NFSP winnings/betted vs tightAggressive: " + str(gamesHard_0_betted/gamesHard_0_payoff))
    print("NFSP winnings/betted vs tightPassive: " + str(gamesHard_1_betted/gamesHard_1_payoff))
    print("NFSP winnings/betted vs looseAggressive: " + str(gamesHard_2_betted/gamesHard_2_payoff))
    print("NFSP winnings/betted vs loosePassive: " + str(gamesHard_3_betted/gamesHard_3_payoff))

    # Gathering generic statistics
    gamesMedium = 0
    gamesMedium_0_betted = 0.0
    gamesMedium_0_payoff = 0.0
    gamesMedium_1_betted = 0.0
    gamesMedium_1_payoff = 0.0
    gamesMedium_2_betted = 0.0
    gamesMedium_2_payoff = 0.0
    gamesMedium_3_betted = 0.0
    gamesMedium_3_payoff = 0.0
    for index, row in df_full.iterrows():
        if (row['nickname'] != "Easy" and row['nickname'] != "Medium" and row['nickname'] != "Hard" and row['nickname'] != "Very Hard" and
        not("tightAggressive" in row['nickname']) and not("tightPassive" in row['nickname']) and not("looseAggressive" in row['nickname']) and not("loosePassive" in row['nickname'])):
            if (row['difficulty'] == "Medium"):
                gamesMedium += 1
                # If Player is tightAggressive
                if(row['labelTree'] == "0"):
                    gamesMedium_0_betted += row['betted']
                    gamesMedium_0_payoff += row['payoff']
                if(row['labelTree'] == "1"):
                    gamesMedium_1_betted += row['betted']
                    gamesMedium_1_payoff += row['payoff']
                if(row['labelTree'] == "2"):
                    gamesMedium_2_betted += row['betted']
                    gamesMedium_2_payoff += row['payoff']
                if(row['labelTree'] == "3"):
                    gamesMedium_3_betted += row['betted']
                    gamesMedium_3_payoff += row['payoff']
    print("\n")
    print("Games played vs Random: " + str(gamesMedium))
    print("Random winnings/betted vs tightAggressive: " + str(gamesMedium_0_betted/gamesMedium_0_payoff))
    print("Random winnings/betted vs tightPassive: " + str(gamesMedium_1_betted/gamesMedium_1_payoff))
    print("Random winnings/betted vs looseAggressive: " + str(gamesMedium_2_betted/gamesMedium_2_payoff))
    print("Random winnings/betted vs loosePassive: " + str(gamesMedium_3_betted/gamesMedium_3_payoff))

    # Gathering generic statistics
    gamesEZ = 0
    gamesEZ_0_betted = 0.0
    gamesEZ_0_payoff = 0.0
    gamesEZ_1_betted = 0.0
    gamesEZ_1_payoff = 0.0
    gamesEZ_2_betted = 0.0
    gamesEZ_2_payoff = 0.0
    gamesEZ_3_betted = 0.0
    gamesEZ_3_payoff = 0.0
    for index, row in df_full.iterrows():
        if (row['nickname'] != "Easy" and row['nickname'] != "Medium" and row['nickname'] != "Hard" and row['nickname'] != "Very Hard" and
        not("tightAggressive" in row['nickname']) and not("tightPassive" in row['nickname']) and not("looseAggressive" in row['nickname']) and not("loosePassive" in row['nickname'])):
            if (row['difficulty'] == "Easy"):
                gamesEZ += 1
                # If Player is tightAggressive
                if(row['labelTree'] == "0"):
                    gamesEZ_0_betted += row['betted']
                    gamesEZ_0_payoff += row['payoff']
                if(row['labelTree'] == "1"):
                    gamesEZ_1_betted += row['betted']
                    gamesEZ_1_payoff += row['payoff']
                if(row['labelTree'] == "2"):
                    gamesEZ_2_betted += row['betted']
                    gamesEZ_2_payoff += row['payoff']
                if(row['labelTree'] == "3"):
                    gamesEZ_3_betted += row['betted']
                    gamesEZ_3_payoff += row['payoff']
    print("\n")
    print("Games played vs Fish: " + str(gamesEZ))
    print("Fish winnings/betted vs tightAggressive: " + str(gamesEZ_0_betted/gamesEZ_0_payoff))
    print("Fish winnings/betted vs tightPassive: " + str(gamesEZ_1_betted/gamesEZ_1_payoff))
    print("Fish winnings/betted vs looseAggressive: " + str(gamesEZ_2_betted/gamesEZ_2_payoff))
    print("Fish winnings/betted vs loosePassive: " + str(gamesEZ_3_betted/gamesEZ_3_payoff))


# VISUALISATION SCATTER
import plotly.express as px

# Visualize original Train Dataset
df_train["label"] = Y.astype(str)
df_train = df_train.sort_values(by=['label'])
# Visualize Tree in 3D with PCA
fig = px.scatter_matrix(df_train,
    dimensions=feature_names,
    color="label",
    title="Scatter Matrix of Train Data")
fig.show()

if (classificationTarget == "Players"):
    # Visualize clusters of Players
    # To show all
    df_visible = df_full.drop(columns=['nickname'])
if (classificationTarget == "Games"):
    # Visualize clusters of Games
    # To show all
    df_visible = df_full.drop(columns=['nickname', 'difficulty'])
    # To show only AI played Games
    #df_visible = df_full.loc[df_full['difficulty'] == "Easy"]
    #df_visible = df_full.drop(columns=['nickname', 'difficulty'])

# Visualize Tree cluster wise
df_visible = df_visible.sort_values(by=['labelTree'])
fig = px.scatter_matrix(df_visible,
    dimensions=feature_names,
    color="labelTree",
    title="Scatter Matrix Based on Tree Classifier Labels")
fig.show()

# Visualize SVC cluster wise
df_visible = df_visible.sort_values(by=['labelSVClinear'])
fig = px.scatter_matrix(df_visible,
    dimensions=feature_names,
    color="labelSVClinear",
    title="Scatter Matrix Based on Linear SVM Classifier Labels")
fig.show()

# Visualize SVC cluster wise
df_visible = df_visible.sort_values(by=['labelSVC'])
fig = px.scatter_matrix(df_visible,
    dimensions=feature_names,
    color="labelSVC",
    title="Scatter Matrix Based on RBF SVM Classifier Labels")
fig.show()

print("\n")
##################################################################################

# PCA on Train Data for Visualization

# PCA

# Clustering players
if (classificationTarget == "Players"):
    df_full = df_full_players.copy()
    df = df_players.copy()
    df_for_pca = df_full.drop(columns=['nickname'])
# Clustering games
if (classificationTarget == "Games"):
    df_full = df_full_games.copy()
    df = df_games.copy()
    df_for_pca = df_full.drop(columns=['nickname', 'difficulty'])

# Explicitly save dataframe values as floats (Otherwise we have a bug)
df_full = df_full.apply(pd.to_numeric, errors='coerce')
df = df.apply(pd.to_numeric, errors='coerce')

# Creating array with PCA
from sklearn.decomposition import PCA
# Start
pca = PCA(n_components=3)
pca.fit(df_for_pca)
transformPCA = pca.transform(df_for_pca)
print("Kept data amount with PCA ", np.sum(pca.explained_variance_ratio_))
# Creating new dataframe with PCA values
if (classificationTarget == "Games"):
    df_pca_full = df_full.drop(columns=['handQualityStart', 'handQualityEnd', 'callsPercent', 'raisesPercent', 'chipsCoeff'])
if (classificationTarget == "Players"):
    df_pca_full = df_full.drop(columns=['foldsPercent', 'allinsPercent', 'callsPercent', 'raisesPercent', 'chipsCoeff', 'payoff'])
# Adding PCA values
df_pca_full['pcaX'] = transformPCA[:,0]
df_pca_full['pcaY'] = transformPCA[:,1]
df_pca_full['pcaZ'] = transformPCA[:,2]
# Creating dataframe only with PCA results for Clustering
if (classificationTarget == "Games"):
    df_pca = df_pca_full.drop(columns=['nickname', 'difficulty'])
if (classificationTarget == "Players"):
    df_pca = df_pca_full.drop(columns=['nickname'])

# Creating target Data and Labels arrays
if (classificationTarget == "Players"):
    # Extract arrays with Test and Train data for classification from all Players
    arrayForClassificationPlayerX = []
    arrayForClassificationPlayerY = []
    playerID = -1
    for player in arrayOfPlayers:
        playerID += 1
        if ("tightAggressive" in player.nickname):
            arrayForClassificationPlayerX.append(df_pca.iloc[playerID].to_numpy() )
            arrayForClassificationPlayerY.append(0)
        if ("tightPassive" in player.nickname):
            arrayForClassificationPlayerX.append(df_pca.iloc[playerID].to_numpy() )
            arrayForClassificationPlayerY.append(1)
        if ("looseAggressive" in player.nickname):
            arrayForClassificationPlayerX.append(df_pca.iloc[playerID].to_numpy() )
            arrayForClassificationPlayerY.append(2)
        if ("loosePassive" in player.nickname):
            arrayForClassificationPlayerX.append(df_pca.iloc[playerID].to_numpy() )
            arrayForClassificationPlayerY.append(3)
    arrayForClassificationPlayerX = np.array(arrayForClassificationPlayerX)
    arrayForClassificationPlayerY = np.array(arrayForClassificationPlayerY)
    X = arrayForClassificationPlayerX
    Y = arrayForClassificationPlayerY

if (classificationTarget == "Games"):
    # Extract arrays with Test and Train data for classification from all played Games
    arrayForClassificationGameX = []
    arrayForClassificationGameY = []
    gameID = -1
    for game in gamesPlayed:
        gameID += 1
        if ("tightAggressive" in game.nickname):
            arrayForClassificationGameX.append(df_pca.iloc[gameID].to_numpy() )
            arrayForClassificationGameY.append(0)
        if ("tightPassive" in game.nickname):
            arrayForClassificationGameX.append(df_pca.iloc[gameID].to_numpy() )
            arrayForClassificationGameY.append(1)
        if ("looseAggressive" in game.nickname):
            arrayForClassificationGameX.append(df_pca.iloc[gameID].to_numpy() )
            arrayForClassificationGameY.append(2)
        if ("loosePassive" in game.nickname):
            arrayForClassificationGameX.append(df_pca.iloc[gameID].to_numpy() )
            arrayForClassificationGameY.append(3)
    arrayForClassificationGameX = np.array(arrayForClassificationGameX)
    arrayForClassificationGameY = np.array(arrayForClassificationGameY)
    X = arrayForClassificationGameX
    Y = arrayForClassificationGameY

# Visualize original Train Dataset
df_train = pd.DataFrame({'pcaX': X[:, 0], 'pcaY': X[:, 1], 'pcaZ': X[:, 2]})
df_train["label"] = Y.astype(str)
df_train = df_train.sort_values(by=['label'])
# Visualize Tree in 3D with PCA
fig = px.scatter_3d(df_train, x='pcaX', y='pcaY', z='pcaZ',
              color='label',
              title="PCA of original Train Data")
fig.show()

# Classificaion

# Creating Train and Test datasets with KFold to check classifier Metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
if (classificationTarget == "Players"):
    splits = 2
if (classificationTarget == "Games"):
    splits = 5
skf = StratifiedKFold(n_splits=splits)
skf.get_n_splits(X,Y)
StratifiedKFold(n_splits=splits, random_state=42, shuffle=True)
for train_index, test_index in skf.split(X,Y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = Y[train_index], Y[test_index]

# Tree Classifier
from sklearn import tree

clf = tree.DecisionTreeClassifier()

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("PCA Tree F1: " + str(f1_score(y_test, y_pred, average=None)))
print("PCA Tree Accuracy: " + str(accuracy_score(y_test, y_pred, normalize=True)))

clf = clf.fit(X, Y)
labelTree = clf.predict(df_pca)
# Save Tree
plt.figure(figsize=(120,30))
tree.plot_tree(clf,
                   feature_names=feature_names,  
                   class_names=class_names_target,
                   fontsize=8.5,
                   filled=True)
plt.savefig(os.path.join(dirname, "treeClassifierPCA.png"), bbox_inches='tight')
# Add labels
df_pca_full["labelTree"] = labelTree.astype(str)


 # SVM

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

# SVC Linear
clf = make_pipeline(StandardScaler(), LinearSVC(random_state=0, tol=1e-5))

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("PCA SVM F1: " + str(f1_score(y_test, y_pred, average=None)))
print("PCA SVM Accuracy: " + str(accuracy_score(y_test, y_pred, normalize=True)))

clf.fit(X, Y)
labelSVClinear = clf.predict(df_pca)
# Add labels
df_pca_full["labelSVClinear"] = labelSVClinear.astype(str)

# SVC kernel
clf = make_pipeline(StandardScaler(), SVC(kernel='rbf', gamma='scale', C=1.0))

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("PCA SVM RBF F1: " + str(f1_score(y_test, y_pred, average=None)))
print("PCA SVM RBF Accuracy: " + str(accuracy_score(y_test, y_pred, normalize=True)))

clf.fit(X, Y)
labelSVC = clf.predict(df_pca)
# Add labels
df_pca_full["labelSVC"] = labelSVC.astype(str)

# Gaussian
# It's a fuzzy classifier, it generates interesting results but to analyze them we need proper visualization
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
kernel = 1.0 * RBF(1.0)
gpc = GaussianProcessClassifier(kernel=kernel, random_state=0).fit(X, Y)
gpc.score(X, Y)
#print(gpc.predict_proba(df))


# VISUALISATION PCA 3D
import plotly.express as px

# Visualize Tree in 3D with PCA
df_pca_full = df_pca_full.sort_values(by=['labelTree'])
fig = px.scatter_3d(df_pca_full, x='pcaX', y='pcaY', z='pcaZ',
              color='labelTree',
              title="PCA with Tree Classifier Labels")
fig.show()

# Visualize SVC linear in 3D with PCA
df_pca_full = df_pca_full.sort_values(by=['labelSVClinear'])
fig = px.scatter_3d(df_pca_full, x='pcaX', y='pcaY', z='pcaZ',
              color='labelSVClinear',
              title="PCA with Linear SVM Classifier Labels")
fig.show()


# Visualize SVC kernel in 3D with PCA
df_pca_full = df_pca_full.sort_values(by=['labelSVC'])
fig = px.scatter_3d(df_pca_full, x='pcaX', y='pcaY', z='pcaZ',
              color='labelSVC',
              title="PCA with RBF SVM Classifier Labels")
fig.show()
