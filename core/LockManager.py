def acquire_lock(site, variable, transaction, lock_type):
    #read only transaction does not require locks
    #But all previous transactions have to have been committed
    #if transaction['read_only'] == True:
    #    return True
    existing_exclusive_lock = False
    for lock in site[variable][locks]:
        if lock['type'] == 'exclusive':
            existing_exclusive_lock = True
    if existing_exclusive_lock == True:
        site[pending_operations].append({
            'transaction' : transaction, 
            'variable' : variable, 
            'lock_type' : lock_type,
        })
        return False
    elif existing_exclusive_lock == False and lock_type == 'shared':
        site[variable][locks].append({
            'type' : 'shared', 
            'transaction' : transaction
        })
        transaction[locks].append({
            'type' : 'shared'
            'site' : site, 

        })
        return True



def release_lock(site, variable, transaction, lock_type):
    #remove the lock from the site variable
    for lock in site[variable][locks]:
        if 
    if lock_type == 'exclusive':
        
