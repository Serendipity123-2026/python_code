def main_task():
    step_one()


def step_one():
    step_two()


def step_two():
    int("abc")


if __name__ == '__main__':
    try:
        main_task()
    except Exception as e:
        print(e)
