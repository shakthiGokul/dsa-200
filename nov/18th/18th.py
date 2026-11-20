HOME_TEAM = 1
AWAY_TEAM = 0

def tournamentWinner(competitions, results):
    scores = {'':0}
    bestTeam = ''
    for idx , competition in enumerate(competitions):
        [homeTeam, awayTeam] = competition
        currentWinner = homeTeam if results[idx] == HOME_TEAM else awayTeam
        updateScores(scores ,currentWinner, 3)
        bestTeam = updateBestTeam(scores, currentWinner, bestTeam)
    return bestTeam

def updateBestTeam(scores, currentTeam , bestTeam):
    if scores[currentTeam] > scores[bestTeam]:
        return currentTeam
    return bestTeam 

def updateScores(scores ,team, point):
    if team in scores:
        scores[team] += point
    else:
        scores[team] = point    