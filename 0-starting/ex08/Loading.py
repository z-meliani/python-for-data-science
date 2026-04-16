import os


def ft_tqdm(lst: range) -> None:
    """
    Print a progress bar.

    Example:
        for x in ft_tqdm(range(10)):
            sleep(0.1)
    """
    lst_size = len(lst)
    width = os.get_terminal_size().columns

    for i, value in enumerate(lst):
        yield i, value
        i += 1
        percent = f"{int(i * 100 / lst_size):3d}%"
        progress = f"{i}/{lst_size}"
        timer = "[00:00<00:00, 000.00it/s]"
        bar_with = width - len(percent) - len(progress) - len(timer) - 3
        bar = f"{'█' * int((i / lst_size) * bar_with):<{bar_with}s}"

        print(f"\r{percent}|{bar}| {progress}", end="")
