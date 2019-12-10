def acquire_lock(site, variable, transaction, lock_type):



def release_lock(site, variable, transaction, lock_type):
    #remove the lock from the site variable
    for lock in site[variable][locks]:
    #if 
    #if lock_type == 'exclusive':
        
