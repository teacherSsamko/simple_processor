import time

sample = [x for x in range(10)]


def some_process(x):
    return True


total = len(sample)
start = time.time()

for i, some in enumerate(sample):
    some_process(some)
    now = time.time()
    print(f'\r{i+1}/{total} runtime: {now - start:.2f}', end='')
    # Use follow code if your python version is before v3.6
    # print('\r{}/{} runtime: {:.2f}'.format(i+1, total, now - start), end='')
    time.sleep(0.5)
