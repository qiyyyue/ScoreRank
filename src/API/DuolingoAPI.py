import duolingo


def get_duolingo_score(username, password):
    lingo = duolingo.Duolingo(username, password)
    lingo_score = lingo.get_language_details('Chinese')
    duolingo_info_list = {}
    try:
        duolingo_info_list['points'] = lingo_score['points']
        duolingo_info_list['level'] = lingo_score['level']
    except Exception:
        return {}

    return duolingo_info_list

#print(get_duolingo_score("qiyyyue", "Lee.951012"))