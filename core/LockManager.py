def acquire_lock(site, variable, transaction, lock_type):
    existing_exclusive_lock = False
    for lock in site[variable][locks]:
        if lock['type'] == 'exclusive':
            existing_exclusive_lock = True
    



def release_lock(site, variable, transaction, lock_type):
