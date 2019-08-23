from functools import reduce
from subprocess import run, PIPE, call

class PenaltyError(Exception):
    pass

def get_participant_output(game_file, game_board, move_by_ai):
    input_to_player = '\n'.join(list(map(lambda x: ' '.join(list(map(lambda y: str(y), x))), game_board))) + '\n' + move_by_ai
    print(input_to_player)
    p = run(game_file, stdout=PIPE, input=input_to_player, encoding='ascii', timeout=1)
    parse_output = process_player_output(p.stdout)
    if game_board[parse_output[0][1]][parse_output[0][0]] != 0:
        raise PenaltyError();
    return(parse_output)

def process_player_output(output):
    out_l = output.splitlines()
    if len(out_l) == 2:
        indices = out_l[0].split(' ')
        if len(indices) == 2:
            x = int(indices[0])
            y = int(indices[1])
            if x>=0 and x<=3 and y>=0 and y<=3:
                if int(out_l[1]) in [2, 4]:
                    return([[x, y], int(out_l[1])])
                else:
                    raise ValueError("Invalid Output Format")
            else:
                raise ValueError("Invalid Output Format")    
        else:
            raise ValueError("Invalid Output Format")
    else:
        raise ValueError("Invalid Output Format")
