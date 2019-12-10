def acquire_lock(site, variable, transactionName, lock_type):
    #if the transaction already has a write lock, do nothing
    sites[site][site_data][variable][locks].append({
        'lock_type' : lock_type, 
        'transaction' : transactionName
    })


def release_lock(site, variable, transactionName, lock_type):
    sites[site][variable]['locks'] = [lock for lock in sites[site][variable]['locks'] if not lock['transaction'] == transactionName]

        