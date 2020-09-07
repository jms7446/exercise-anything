import random

import tenacity
from tenacity import retry, wait_exponential, wait_fixed


@retry(wait=wait_fixed(2) + wait_exponential(multiplier=0.5, max=30, exp_base=2))
def do_something():
    if random.randint(0, 2) != 0:
        print('Failure')
        raise RuntimeError
    print('Success')


do_something()
