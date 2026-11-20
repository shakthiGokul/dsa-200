class Program {
    let HOME_TEAM_WON = 1

    func tournamentWinner(_ competitions: [[String]], _ results: [Int]) -> String {
        var bestTeam = ""
        var scores = [bestTeam: 0]

        for (idx, competition) in competitions.enumerated() {
            let (homeTeam, awayTeam) = (competition[0], competition[1])
            let currentWinner = results[idx] == HOME_TEAM_WON ? homeTeam : awayTeam

            // Cleaner way to add 3 without needing an if/else nil check
            scores[currentWinner, default: 0] += 3

            if scores[currentWinner]! > scores[bestTeam]! {
                bestTeam = currentWinner
            }
        }

        return bestTeam
    }
}
