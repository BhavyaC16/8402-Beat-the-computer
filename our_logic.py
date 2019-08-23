from functools import reduce
from subprocess import run, PIPE, call
def get_participant_output(game_file, game_board, move_by_ai):
    input_to_player = '\n'.join(list(map(lambda x: ' '.join(list(map(lambda y: str(y), x))), game_board))) + '\n' + move_by_ai
    print(input_to_player)
    p = run(game_file, stdout=PIPE, input=input_to_player, encoding='ascii', timeout=1)
    print('stdout', p.stdout)
    p = p.stdout.splitlines()
    return([[int(p[0].split(' ')[0]), int(p[0].split(' ')[1])], int(p[1])])
