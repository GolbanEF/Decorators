import time
from functools import wraps


def logger(path):

    def _logger(old_function):

        @wraps(old_function)
        def write_to_file(*args):
            start_time = time.ctime(time.time())
            result = old_function(*args)
            log_string = f'Function call time: {start_time}\nFunction name: {old_function.__name__}\n'
            log_string += f'Arguments: {args}\nResult: {result}\n\n'
            if path:
                filename = path + 'log.txt'
            else:
                filename = 'log.txt'

            with open(filename, 'a') as log:

                log.write(log_string)

            return result

        return write_to_file

    return _logger

