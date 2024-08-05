from random import randint


def main():
    while True:
        start_number = input('Please enter the starting number: ')
        end_number = input('Please enter the ending number: ')

        if start_number.isdigit() and end_number.isdigit:
            print(f'Generating a random number between {start_number} and {end_number}:',
                  f'{randint(int(start_number), int(end_number))}\n')
        else:
            print('Please enter valid numbers for both the starting and ending values.\n')

            
if __name__ == '__main__':
    main()