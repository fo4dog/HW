from functools import wraps


def type_logger(level=0):

    def logger(func):

        @wraps(func)
        def decor(*argv):


            if level > 0:

                return 'calc_cube(' + ", ".join([f"{func(x)}:{type(func(x))}" for x in argv]) + ")"

            else:

                return "calc_cube(" + ", ".join([str(func(x)) for x in argv]) + ")"

        return decor

    return logger


@ type_logger(1)
def calc_cube(x):
    """ cube of args """
    return x ** 3


if __name__ == "__main__":
    print(calc_cube(5, 10))