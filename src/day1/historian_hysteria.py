from collections import Counter


def read_lists_from_file(file: str) -> (list[int], list[int]):
    left, right = [], []
    with open(file) as f:
        for line in f:
            tokens = line.split(r"   ")
            left.append(int(tokens[0]))
            right.append(int(tokens[1]))

    return left, right


def calculate_pairwise_distance_between_lists(left: list[int], right: list[int]) -> int:
    """Calculates the pairwise distances between two lists, starting with the
    smallest two numbers in each list."""
    left.sort()
    right.sort()

    dist = 0
    for le, ri in zip(left_list, right_list):
        dist += abs(le - ri)

    return dist


def calculate_similarity_score_between_lists(left: list[int], right: list[int]) -> int:
    """Calculates the similarity score between two lists by summing the products of each
    number in the left list and the times it occurs in the right list."""
    occurrences_right = Counter(right)
    score = 0
    for k in left:
        score += k * occurrences_right[k]

    return score


if __name__ == '__main__':
    input_file = "input.txt"
    left_list, right_list = read_lists_from_file(input_file)
    distance = calculate_pairwise_distance_between_lists(left_list, right_list)
    print(f"The distance between the lists is: {distance}")

    similarity_score = calculate_similarity_score_between_lists(left_list, right_list)
    print(f"The similarity score between the lists is: {similarity_score}")
