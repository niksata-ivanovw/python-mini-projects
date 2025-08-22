import sys

def compress(data: str):
    input_as_list = data.split(', ')
    counter = 0
    last_num = input_as_list[0]
    compressed_numbers = []
    for current_num in input_as_list:
        if current_num == last_num:
            counter += 1
        else:
            compressed_numbers.append({last_num: counter})
            counter = 1
        last_num = current_num
    compressed_numbers.append({last_num: counter})

    return compressed_numbers

def expand(compressed_data: list):
    expanded_list = []
    for current_character in compressed_data:
        for character, count in current_character.items():
            expanded_list.extend([character] * count)
    expanded_string = ', '.join(expanded_list)

    return expanded_string

def main():
    data = input()
    if data == '':
        print('There aren\'t any numbers in the given input.')
    else:
        compressed_data = compress(data)
        print(compressed_data)

    decision = input('Do you want to expand the given input to it\'s original form? (Y/N): ')
    if decision == 'Y':
        expanded_data = expand(compressed_data)
        print(expanded_data)


if __name__ == '__main__':
    main()