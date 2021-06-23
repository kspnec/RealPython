import time

def count_items(items):
    print('Counting ', end='', flush=True)
    num = 0
    for item in items:
        num += 1
        time.sleep(1)
        print('.', end='', flush=True)

    print(f'\nThere were {num} items')
