def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    # Default Arguments in Python - Hacker Rank Solution END ----->
    for _ in range(n):
        print(stream.get_next())