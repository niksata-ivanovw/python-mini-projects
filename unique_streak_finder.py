def find_longest_streaks(data: list) -> tuple:
    current_streak = []
    longest_streaks = []
    max_length = 0
    current_start_index = 0

    for i, number in enumerate(data):
        if number not in current_streak:
            current_streak.append(number)
        else:
            if len(current_streak) > max_length:
                longest_streaks = [(current_streak, current_start_index)]
                max_length = len(current_streak)
            elif len(current_streak) == max_length:
                longest_streaks.append((current_streak, current_start_index))

            current_streak = [number]
            current_start_index = i

    #final check after loop
    if len(current_streak) > max_length:
        longest_streaks = [(current_streak, current_start_index)]
    elif len(current_streak) == max_length:
        longest_streaks.append((current_streak, current_start_index))

    return longest_streaks

def main():
    data = input('Please enter a serie of integers seperated by ", ": ')
    data_list = data.split(', ')
    dat_as_ints = [int(num) for num in data_list]

    result = find_longest_streaks(dat_as_ints)
    print(f'There were a total of {len(result)} longest streaks found:')
    for streak, index in result:
        print(f'-streak: {streak}, starting index: {index}')

if __name__ == '__main__':
    main()