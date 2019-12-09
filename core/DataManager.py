#Assume locking and transaction queing is taken care of by the relevant manager


def read_value(site, variable, transaction, time_step, read_type):
    #if the transaction has a lock on the variable, read from uncommitted
    if read_type == 'read': 
        #Return the last committed value (Confirm weather it should read the last uncommitted value instead)
        return sites[site][site_data][variable][value]
    #elif read_type == 'read_only':
    #    #Return when the transaction started
    #    transaction[start_time]
    #    return sites[site][site_data][variable][value]


def write_value(site, variable, transaction, time_step, value):
    sites[site][site_data][variable][uncommitted_transactions].append({
        'transaction' : transaction, 
        'value' : value, 
        'time_step' : time_step, 
    })



