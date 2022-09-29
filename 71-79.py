71-79
# TODO 10: insert new player and score
    scores.insert(index, player_score)
    names.insert(index, player_name)
    print(scores)
    print(names)
  # TODO 11: keep both lists at 5 elements only (top 5 players)
    if (len(names) > 5): 
        names.pop(5)
        scores.pop(5)






        # TODO 10: insert new player and score
    scores.insert(index, player_score)
    names.insert(index, player_name)
  # TODO 11: keep both lists at 5 elements only (top 5 players)
    if (len(names) > 5): 
        names.pop(5)
        scores.pop(5)