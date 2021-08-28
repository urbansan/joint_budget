def _integer_ids():
    i = 1
    while True:
        yield i
        i += 1


_gen = _integer_ids()


def get_next_unique_id():
    return str(next(_gen))


if __name__ == "__main__":
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
    print(get_next_unique_id())
