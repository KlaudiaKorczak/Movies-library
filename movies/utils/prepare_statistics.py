
def count_comments(movies, comments, date_from, date_to):
    movies_comments = {}
    for movie in movies:
        comments_count = comments.filter(created__range=[date_from, date_to], movie_id=movie.id).count()
        movies_comments[movie.id] = comments_count

    sorted_numbers = sorted(movies_comments.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_numbers


def generate_statistics(sorted_numbers):
    rank = 1
    current_value = sorted_numbers[0][1]
    results_list = []

    for pair in sorted_numbers:
        if pair[1] < current_value:
            current_value = pair[1]
            rank += 1
        results_list.append({'movie_id': pair[0], 'total_comments': pair[1], 'rank': rank})

    return results_list
