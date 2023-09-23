import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("app.log", mode='w')
logger.addHandler(handler)

original_print = print


def print_to_log_and_console(message):
    logger.info(message)
    original_print(message)


print = print_to_log_and_console


def log_function(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Func {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper

