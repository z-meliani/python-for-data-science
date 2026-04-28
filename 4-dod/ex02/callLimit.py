
def callLimit(limit: int):
    """Arguments for callLimiter decorator"""
    count = 0

    def callLimiter(function):
        """Decorator"""
        def limit_function(*args: any, **kwds: any):
            """Wrapper function"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)

            return print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
