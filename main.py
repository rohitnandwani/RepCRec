import sys

from util.config import *
from util.initialise import initialise

from core import TransactionManager
from core import SiteManager

TIME_STEP = 0

if __name__ == '__main__':

    initialise()

    inputSource = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        if f.mode == 'r':
            inputSource = f.readlines()

    for originalLine in inputSource:
        line = ''.join(filter(lambda c: c != ' ' and c != '\t' and c != '\n' and c is not None, originalLine))
        print(originalLine.strip())

        indexOfCommentStart = line.find('//')

        if indexOfCommentStart != -1:
            line = line[:indexOfCommentStart]

        if line == '' and indexOfCommentStart != -1:
            continue

        elif line.startswith('quit'):
            break

        TIME_STEP = TIME_STEP + 1

        if len(line) == 0:
            continue

        elif line.startswith('beginRO'):
            transaction = line[8:-1]
            TransactionManager.begin_transaction(transaction, TIME_STEP, True)


        elif line.startswith('begin'):
            transaction = line[6:-1]
            TransactionManager.begin_transaction(transaction, TIME_STEP, False)


        elif line.startswith('W'):
            write_tuple = line[2:-1]
            write_list = write_tuple.split(',')
            transaction = write_list[0].strip()
            key = write_list[1].strip()
            value = write_list[2].strip()
            TransactionManager.write_operation(transaction, key, value)
            SiteManager.process_pending_operations(TIME_STEP)


        elif line.startswith('R'):
            write_tuple = line[2:-1]
            write_list = write_tuple.split(',')
            transaction = write_list[0].strip()
            key = write_list[1].strip()
            TransactionManager.read_operation(transaction, key)
            SiteManager.process_pending_operations(TIME_STEP)


        elif line.startswith('fail'):
            site = line[5:-1]
            SiteManager.fail(site, TIME_STEP)


        elif line.startswith('recover'):
            site = line[8:-1]
            SiteManager.recover(site, TIME_STEP)


        elif line.startswith('end'):
            transaction = line[4:-1]
            TransactionManager.end_transaction(transaction, TIME_STEP)


        elif line.startswith('dump'):
            TransactionManager.dump()

        else:
            print('Command not recognised')
            break

            

