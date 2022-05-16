import inquirer

from crop import crop
from file import load_photos_folder


def main():
    directory = 'photos'
    choices = ['Load photos folder and make json file', 'Crop photos']
    questions = [
        inquirer.List('choice',
            message="Choice your command:",
            choices=choices,
        ),
    ]

    answer = inquirer.prompt(questions)['choice']

    if answer == choices[0]:
        load_photos_folder(directory)
    elif answer == choices[1]:
        crop()
    else:
        print('invalid command')
        


if __name__ == '__main__':
    main()
    