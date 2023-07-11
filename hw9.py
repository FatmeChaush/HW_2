def slope_style_score(scores):
    scores.sort()
    scores = scores[1:-1]
    average = sum(scores) / len(scores)
    final_score = round(average, 2)
    return final_score


print(slope_style_score([94, 95, 95, 95, 90]))