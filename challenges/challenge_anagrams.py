def partition(word, init, fin):
    pivot = word[fin]
    delimiter = init - 1

    for index in range(init, fin):
        if word[index] <= pivot:
            delimiter = delimiter + 1
            word[index], word[delimiter] = word[delimiter], word[index]

    word[delimiter + 1], word[fin] = word[fin], word[delimiter + 1]

    return delimiter + 1


def quick_sort(word, init, fin):
    if init < fin:
        p = partition(word, init, fin)
        quick_sort(word, init, p - 1)
        quick_sort(word, p + 1, fin)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    first = list(first_string.lower())
    second = list(second_string.lower())

    quick_sort(first, 0, len(first) - 1)
    quick_sort(second, 0, len(second) - 1)

    first_ordered = "".join(first)
    second_ordered = "".join(second)

    if first_ordered == second_ordered:
        return (first_ordered, second_ordered, True)
    return (first_ordered, second_ordered, False)
