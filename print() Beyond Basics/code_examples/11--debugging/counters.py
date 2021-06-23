# counters.py

import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def count_lower_case(item):
    logger.info('count_lower_case(%s)', item)
    num = 0
    for letter in item:
        if 97 <= ord(letter) <= 122:
            logger.debug('  letter *%s* is lowercase', letter)
            num += 1

    logger.info('  returning %s', num)
    return num
