#Assume locking and transaction queing is taken care of by the relevant manager

def read_value(site, variable, transactionName, time_step, read_type):
    if read_type == 'read_only':
       for i in range (0, len(sites[site][site_data][variable][committed_transactions]):
           if sites[site][site_data][variable][committed_transactions][i]['committed_time'] <=  time_step < sites[site][site_data][variable][committed_transactions][i+1]['committed_time']:
               return sites[site][site_data][variable][committed_transactions][i]['value']
    else:
        #if the transaction has a lock on the variable, read from uncommitted, else from committed.
        transactionHasLock = False
        for lock in sites[site][variable][locks]:
            if lock['transaction'] == transactionName:
                transactionHasLock = True

        if transactionHasLock == True:
            return sites[site][site_data][variable][uncommitted_transactions][-1]['value']
        else:
            return sites[site][site_data][variable][committed_transactions][-1]['value']


def write_value(site, variable, transactionName, time_step, value):
    sites[site][site_data][variable][uncommitted_transactions].append({
        'transaction' : transactionName, 
        'value' : value, 
        'time_step' : time_step, 
    })



