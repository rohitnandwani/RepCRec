import sys

from core import TransactionManager
#from core import DataManager
#from core import LockManager
#from core import SiteManager

TIME_STEP = 0
NUMBER_OF_VARIABLES = 20
NUMBER_OF_SITES = 10


def initialise():
    transactions = {}
    data = {}
    locks = {}
    sites = {}

    for i in range(0, NUMBER_OF_VARIABLES):
        variable = "x" + str(i+1)
        value = 10 * (i + 1)
        data[variable] = {
            'value' : value, 
            'committed_transactions' : [
                #transaction
                #value
                #committed time
            ], 
            'uncommitted_transactions' : {
                #transaction
                #value
                #committed time
            }, 
            'locks' : [
                #type: //shared or exclusive
                #transaction: 
            ]
        }

    for i in range(0, NUMBER_OF_SITES):
        index = str(i+1)
        site_data_indices = []
        for j in range(0, NUMBER_OF_VARIABLES):
            if (1 + ((j+1) % 10) == i +1):
                site_data_indices.append(j+1)
            elif (j+1 % 2 == 0):
                 site_data_indices.append(j+1)
        
        site_data = [data["x" + str(k)] for k in site_data_indices]

        sites[index] = {
            'site_data' : site_data, 
            'available': True,
            'pending_operations': [],
            'reset_time' : TIME_STEP
        }

    return

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
            TransactionManager.begin_transaction(transaction, Timer.CURRENT_TIME, True)


        elif line.startswith('begin'):
            transaction = line[6:-1]
            TransactionManager.begin_transaction(transaction, Timer.CURRENT_TIME, False)


        elif line.startswith('W'):
            write_tuple = line[2:-1]
            write_list = write_tuple.split(',')
            transaction = write_list[0].strip()
            key = write_list[1].strip()
            value = write_list[2].strip()
            DataManager.write_value(transaction, key, value)


        elif line.startswith('R'):
            write_tuple = line[2:-1]
            write_list = write_tuple.split(',')
            transaction = write_list[0].strip()
            key = write_list[1].strip()
            DataManager.read_value(transaction, key)


        elif line.startswith('fail'):
            site = line[5:-1]
            SiteManager.fail(site)


        elif line.startswith('recover'):
            site = line[8:-1]
            SiteManager.recover(site, Timer.CURRENT_TIME)


        elif line.startswith('end'):
            transaction = line[4:-1]
            TransactionManager.end_transaction(transaction, Timer.CURRENT_TIME)


        elif line.startswith('dump'):
            site = line[5:-1]
            SM.dumpSite(site)

        else:
		    print('Command not recognised')
            

