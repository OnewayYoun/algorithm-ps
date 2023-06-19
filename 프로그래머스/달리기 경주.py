def solution(players, callings):
    ranks = {v: i for i, v in enumerate(players)}
    for calling in callings:
        idx = ranks[calling]
        ranks[calling] -= 1
        ranks[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players
