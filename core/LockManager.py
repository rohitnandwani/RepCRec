from util.config import *

def acquire_lock(site_name, variable, transactionName, lock_type):
    #if the transaction already has a write lock, do nothing
    sites[site_name]['site_data'][variable]['locks'].append({
        'type' : lock_type, 
        'transaction' : transactionName
    })


def release_lock(site_name, variable, transactionName, lock_type):
    sites[site_name][variable]['locks'] = [lock for lock in sites[site_name][variable]['locks'] if not lock['transaction'] == transactionName]

        