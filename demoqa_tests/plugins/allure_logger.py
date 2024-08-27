# Code by yashaka

import re
import types
from functools import wraps


def humanify(name: str):
    return re.sub(r'_+', ' ', name).strip().capitalize()


def allure_step(function):
    @wraps(function)
    def function_with_logging(*args, **kwargs):
        is_method = (
            args
            and isinstance(args[0], object)
            and isinstance(getattr(args[0], function.__name__), types.MethodType)
        )

        args_to_log = args[1:] if is_method else args
        args_and_kwargs_to_log_as_strings = [
            *map(str, args_to_log),
            *[f'{key}={value}' for key, value in kwargs.items()],
        ]
        args_and_kwargs_string = (
            (': ' ','.join(map(str, args_and_kwargs_to_log_as_strings)))
            if args_and_kwargs_to_log_as_strings
            else ''
        )

        title = (
            (f'[{args[0].__class__.__name__}] ' if is_method else '')
            + humanify(function.__name__)
            + args_and_kwargs_string
        )

        return function(*args, **kwargs)

    return function_with_logging
