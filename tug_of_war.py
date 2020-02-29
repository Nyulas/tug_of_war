def separation(arr, n, curr_elements, no_of_selected_elements,
            soln, min_diff, Sum, curr_sum, curr_position, operation):

    #ha a vegere jutottunk megall
    if (curr_position == n):
        return

    # megfigyeljuk, hogy tobb maradott elem van mint kivalasztott
    if ((int(n / 2) - no_of_selected_elements) >
            (n - curr_position)):
        return

    # ha a jelenlegi elem nincs hoazzaadva a  megoldashoz
    separation(arr, n, curr_elements, no_of_selected_elements,
            soln, min_diff, Sum, curr_sum, curr_position + 1, operation)

    # jelenlegi elemet megoldasnak tekintjuk
    no_of_selected_elements += 1
    curr_sum = curr_sum + arr[curr_position]
    curr_elements[curr_position] = True
    operation[0] += 1

    # megnezzuk, hogy van megoldas
    if (no_of_selected_elements == int(n / 2)):

        # megnezzuk, hogy jobb a megoldas mint ami volt
        if (abs(int(Sum / 2) - curr_sum) < min_diff[0]):
            min_diff[0] = abs(int(Sum / 2) - curr_sum)
            for i in range(n):
                soln[i] = curr_elements[i]
    else:

        # megfigyeljuk mikor a jelenlegi elem mar a megoldasban van
        separation(arr, n, curr_elements, no_of_selected_elements,
                soln, min_diff, Sum, curr_sum, curr_position + 1, operation)

    # jelenlegi elemet helytelennek rakjuk
    operation[0] += 1
    curr_elements[curr_position] = False


def action(arr, length):


    #ebben a tombbe figyeljuk, hogy melyik elem volt felhasznalva
    curr_elements = [None] * length

    #ebben meg azt, hogy melyik fog belekerulni az elso csapatba es melyik a masodikba
    soln = [None] * length

    min_diff = [999999999999]

    operation = [0]

    Sum = 0
    for i in range(length):
        Sum += arr[i]
        curr_elements[i] = soln[i] = False

    separation(arr, length, curr_elements, 0,
            soln, min_diff, Sum, 0, 0, operation)

    print("first team: ")
    for i in range(length):
        if (soln[i] == True):
            print(arr[i], end=" ")
    print()
    print("second team: ")
    for i in range(length):
        if (soln[i] == False):
            print(arr[i], end=" ")
    print()
    print("operation went to get the result:", operation[0])


if __name__ == '__main__':

    arr = [23, 45, -99, 4, 189, -1]

    length = len(arr)

    action(arr, length)

