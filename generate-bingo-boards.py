#!/usr/bin/python3
import os
from argparse import Namespace


class Env:
    """ Helpful stuff """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, 'output')
    dictionary_folder = os.path.join(script_dir, 'dictionaries')
    config_folder = os.path.join(script_dir, 'config')
    pass


def empty_output_folder() -> None:
    """ Clear all contents from the output folder """
    import shutil
    if os.path.exists(Env.output_folder):
        shutil.rmtree(Env.output_folder)
    os.mkdir(Env.output_folder)


def read_dictionary(config: dict[str, object]) -> list[str]:
    """
    Read input dictionary of words from file.
    :return: list of tuples of words and their frequency
    """
    with open(config['Dictionary']) as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]
    lines = list(set(lines))    # Remove duplicate words
    return lines


def read_config_file(args: Namespace) -> dict[str, object]:
    """
    Read configuration file
    :return: dictionary of keys and values
    """
    import configparser

    def to_int(s: str) -> int:
        try:
            return int(s)
        except Exception as e:
            raise e

    config_parser = configparser.ConfigParser()
    config_parser.read(args.config_file)
    # Gather values into dictionary
    config = {}
    config['Dictionary'] = config_parser['MAIN']['Dictionary']
    config['People'] = config_parser['MAIN']['People']
    config['BoardsPerPerson'] = config_parser['MAIN']['BoardsPerPerson']
    config['BoardWidth'] = config_parser['MAIN']['BoardWidth']
    config['BoardHeight'] = config_parser['MAIN']['BoardHeight']
    config['FreeCenter'] = config_parser['MAIN']['FreeCenter']

    # Parse values
    config['Dictionary'] = os.path.join(Env.dictionary_folder, config['Dictionary'])
    if not os.path.exists(config['Dictionary']) or not os.path.isfile(config['Dictionary']):
        raise ValueError(f"Dictionary file does not exist {config['Dictionary']}")
    config['People'] = list(set(p.strip() for p in config['People'].split(',')))
    config['BoardsPerPerson'] = to_int(config['BoardsPerPerson'])
    config['BoardWidth'] = to_int(config['BoardWidth'])
    config['BoardHeight'] = to_int(config['BoardHeight'])
    config['FreeCenter'] = config['FreeCenter'].lower() in ['yes', 'true']

    return config


def parse_cmd_args() -> Namespace:
    """
    Parse CLI arguments
    :return:
    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file", default='default-config.ini', help="Config file to use")
    args = parser.parse_args()
    args.config_file = os.path.join(Env.config_folder, args.config_file)
    # Check the config file exists
    if not os.path.exists(args.config_file) or not os.path.isfile(args.config_file):
        raise(ValueError(f'Config file {args.config_file} does not exist'))
    return args


def generate_board(config: dict[str, object], dictionary: list[str]) -> list[list[str]]:
    """ Generate a single board """
    import copy
    from random import shuffle
    width = config['BoardWidth']
    height = config['BoardHeight']
    if width * height > len(dictionary):
        raise ValueError(f'The dictionary needs more words! At least {width * height} words please!')

    words = copy.deepcopy(dictionary)
    shuffle(words)
    words = words[0: width * height]   # Cut off words to make a board
    if config['FreeCenter']:
        words[len(words) // 2] = 'FREE!'

    # Convert 1D list to 2D board
    def reshape(_list, _lengths):
        index = 0
        for _len in _lengths:
            yield _list[index: index + _len]
            index += _len

    return list(reshape(words, [width] * height))


def board_to_string(board: list[list[str]]) -> tuple[str, int]:
    """
    Board to fancy string
    :param board: a single 2D board of words
    :return: tuple of string representation board, and width in characters of the board
    """
    corner_char = '+'
    vertical_border_char = '|'
    horizontal_border_char = '-'
    max_char_word = max(max(len(word) for word in line) for line in board)
    interior_width = max_char_word + 2              # Two spaces
    interior_height = int(interior_width * 0.3)     # Height in chars is some percentage of width
    interior_height = max(3, interior_height)
    if interior_height % 2 == 0:                    # Make height odd
        interior_height += 1
    num_empty_rows_above_below = (interior_height - 1) // 2

    # Generate row
    def get_row() -> str:
        s = ''
        for _ in range(len(board[0])):
            s = f'{s}{corner_char}{horizontal_border_char * interior_width}'
        return s + corner_char + '\n'

    # Empty rows
    def get_empty_row() -> str:
        s = ''
        for _ in range(len(board[0])):
            s = f'{s}{vertical_border_char}{" " * interior_width}'
        return s + vertical_border_char + '\n'

    # Row with words
    def get_row_words(words) -> str:
        s = ''
        for word in words:
            s = f'{s}{vertical_border_char}{word:^{interior_width}}'
        return s + vertical_border_char + '\n'

    board_str = ''
    for row in board:
        board_str += get_row()                                       # Row border
        board_str += get_empty_row() * num_empty_rows_above_below    # Empty rows
        board_str += get_row_words(row)                              # Rows with words
        board_str += get_empty_row() * num_empty_rows_above_below    # Empty rows
    board_str += get_row()                                           # Last row border
    return board_str, len(get_row())


def board_strings_to_whole_file(board_strs: list[str], max_board_width: int) -> str:
    header = 'Here are your bingo boards! Print this page out or open it in a text editor! Fill out the spaces as people say the words!'
    footer = 'Generated with love using github.com/calvincramer/covid-bingo'

    def section_separator() -> str:
        return '\n\n\n'

    def board_header(board_name: object) -> str:
        return f'##### BOARD {str(board_name)} #####'

    max_width = max(len(header), len(footer), max_board_width)
    s = ''
    s += f'{header:^{max_width}}'
    s += section_separator()
    for i, board_str in enumerate(board_strs):
        # Board header
        s += f'{board_header(i+1):^{max_width}}\n'
        # Print board centered
        board_lines = board_str.split('\n')
        for board_line in board_lines:
            s += f'{board_line:^{max_width}}\n'
        s += section_separator()
    s += f'{footer:^{max_width}}\n'
    return s


def board_to_html(board: list[list[str]]) -> str:
    """ Board to html page """
    pass


def person_name_to_folder_name(name: str) -> str:
    return name.replace(' ', '_')


def generate_stuff_for_everyone(config: dict[str, object], dictionary: list[str]):
    """ Generate all the boards for everyone """
    for person in config['People']:
        # Make folder
        folder_name = person_name_to_folder_name(person)
        folder_name = os.path.join(Env.output_folder, folder_name)
        os.mkdir(folder_name)
        os.chdir(folder_name)

        # Generate N boards for them
        boards = [generate_board(config, dictionary) for _ in range(config['BoardsPerPerson'])]

        # Generate string representation of boards
        board_strings = []
        board_widths = []
        for b in boards:
            board_str, board_width = board_to_string(b)
            board_strings.append(board_str)
            board_widths.append(board_width)
        max_board_width = max(board_widths)

        # Save board strings as text file
        board_strings_whole = board_strings_to_whole_file(board_strings, max_board_width)
        with open(f'{folder_name}_all_boards.txt', 'w') as fp:
            fp.write(board_strings_whole)

        # Save boards as html files

        # Generate email

        for board, board_str in zip(boards, board_strings):
            print(board)
            print(board_str)
        print()
        pass



def main():
    args = parse_cmd_args()
    config = read_config_file(args)
    empty_output_folder()
    generate_stuff_for_everyone(config, read_dictionary(config))


if __name__ == '__main__':
    main()
