from multiprocessing import Pool, cpu_count
from subprocess import Popen, PIPE, TimeoutExpired
import time


# In test file, we will multiprocess the execution of exercises from 1_1 to 2_1.


def process_communicator(exercise: str, args: tuple = None, inputs: tuple = None) -> tuple[str, str, float]:
    """
    This is the function which constructs the process and communicates with it: that is, when the script being executed
    asks for user-input, it writes and flush, when it doesn't it's executed normally.

    It's worth to point out: the arguments of this function are mostly optional for a reason: be volatile, so we can
    adapt it to all student's functions based on their requirement.

    :param exercise: The only obligatory argument, since an exercise may not require arguments.
    :param args:     Optional, for exercises in which the function requires arguments. Tuple, so we can iterate.
    :param inputs:   Optional, for exercises that require user-inputs. Tuple, so we can iterate.
    :return:         Tuple composed of output, error and execution time.
    """

    if args is not None and args != ():  # to not generate error in case the exercise does not require arguments.
        function_argument: str = f'*{args}'
    else:
        function_argument: str = ''

    process = Popen(args=["python", "-c",  # constructing the child process
                          f"import sys; from funcoes_exercicios import exercicio_{exercise};"
                          f"x = exercicio_{exercise}({function_argument}); print(f'{exercise}: ' + str(x));"],
                    stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding='utf-8', text=True)

    start_time = time.time()  # so we can catch the execution time

    if inputs is not None and inputs != ():  # this exercise contains input, so we write to its stdin PIPE
        for u_input in inputs:
            process.stdin.write(str(u_input) + '\n')
            process.stdin.flush()

    try:
        output, error = process.communicate(timeout=0.5)
    except TimeoutExpired:  # in case the student's function enters a loop
        process.kill()
        output, error = (f'None\n', f'TimeoutExpired || Entered loop for arg(s): {args}')

    finished_time = time.time()
    delta_time = finished_time - start_time

    return output, error, delta_time


if __name__ == '__main__':

    p = Pool(min(cpu_count(), 61))
    messages: list[tuple] = [('2_1', (-1, 0), (1, 3, 7, -1)), ('1_1', (10,)), ('1_1', (6,)), ('1_2', (3,)),
                             ('1_3', (2,)), ('1_4', (5,))]
    results: list[tuple] = p.starmap(process_communicator, messages)

    total_time: float = 0
    for i, t in enumerate(results):  # i, index. t, tuple.
        print('===============================================================================',
              f'\n>>> Exercício_{messages[i][0]}'
              f'\n--Argument(s): {messages[i][1]}' if messages[i][1] != () else '\n--Argument(s): None',
              f'\n--Input(s): {messages[i][2]}' if len(messages[i]) > 2 else '\n--Input: None',
              f'\n--Output: {t[0][0:-1]}',  # 0:-1 so the final \n is not printed.
              f'\n--Error: {t[1]}' if t[1] != '' else '\n--Error: None, execution successful',
              f'\n--Execution Time (seconds): {t[2]}',
              '\n===============================================================================')
        total_time += t[2]

    print(f'§§§ Total Execution Time (seconds): {total_time}')
    p.close()
