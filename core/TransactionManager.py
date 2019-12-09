


def begin_transaction(time_step, read_only):
    transactions[transactionName] = {
        'read_only': read_only,
        'pending_operations': []
        'start_time': time_step,
        'locks': {},
        'failed': False,
        'abort_reason' : None
    }


#assumes no transaction is waiting at any site on end
def end_transaction(transaction):
    


def commit_transaction(transaction):
    #release locks

    #if aborted, what happens to the tasks after?
        #Delete all pending operations for variables for which the lock was held by the transaction
    del transactions[transaction]

def abort_transaction():
    pass


def dump(sites):
    for site in sites.keys():
        print ("Site")
        print (Site)
        for site_data in sites[site].keys():
            print ("variable")
            print site_data
            print ("value")
            print sites[site][site_data].value


def get_sites_for_variable(variable):
    sites_for_variable = []
    for site in sites:
        if variable in site.site_data.keys():
            sites_for_variable.append(site)
    return sites_for_variable

def write_operation(transaction, key, value):
    site[pending_operations].append({
        'transaction' : transaction, 
        'variable' : variable, 
        'value' : value, 
        'type' : 'write'
    })


def read_operation(transaction, key):
    if (transactions[transaction].read_only == True):
        read_type = 'read_only'
    else:
        read_type = "read"
    site[pending_operations].append({
        'transaction' : transaction, 
        'variable' : variable, 
        'type' : read_type
    })






