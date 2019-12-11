from util.config import *

def acquire_lock(site_name, variable, transactionName, lock_type):
    #if the transaction already has a write lock, do nothing
    sites[site_name]['site_data'][variable]['locks'].append({
        'type' : lock_type, 
        'transaction' : transactionName
    })


def release_lock(site_name, variable, transactionName, lock_type='exclusive'):
    sites[site_name]['site_data'][variable]['locks'] = [lock for lock in sites[site_name]['site_data'][variable]['locks'] if not lock['transaction'] == transactionName]


def release_locks_on_transaction(transactionName):
    for site in sites.keys():
        for variable in sites[site]['site_data']:
            release_lock(site, variable, transactionName)
