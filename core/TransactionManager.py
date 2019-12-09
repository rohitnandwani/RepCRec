def commit_transaction(sites, transaction):
    for s

def abort_transaction():
    pass

def abort_all_ongoing_transactions():
    pass

def begin_transaction(time_step, read_only):
    transactions[transactionName] = {
        'read_only': read_only,
        'pendingOperation': {
            'operation': None,
            'options': {}
        },
        'start_time': time_step,
        'locks': {},
        'failed': False,
        'failed_reason' : None
    }



def end_transaction():
    pass
    #commit or abort
    #if 
    #delete transaction

def grant_lock():
    pass


def reject_lock():
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








