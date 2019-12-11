from util.config import *

#Assume locking and transaction queing is taken care of by the relevant manager

def read_value(site, variable, transactionName, time_step, read_type):
    if read_type == 'read_only':
       for i in range (0, len(sites[site]['site_data'][variable]['committed_transactions'])):
            committed_time = sites[site]['site_data'][variable]['committed_transactions'][i]['committed_time']
            if time_step < committed_time:
                continue
            if time_step == committed_time:
                return sites[site]['site_data'][variable]['committed_transactions'][i]['value']
            if time_step > committed_time:
                return sites[site]['site_data'][variable]['committed_transactions'][i]['value']

    elif read_type == 'read':
        #if the transaction has a lock on the variable, read from uncommitted, else from committed.
        transactionHasLock = False
        for lock in sites[site]['site_data'][variable]['locks']:
            if lock['transaction'] == transactionName:
                transactionHasLock = True

        if transactionHasLock == True:
            if len(sites[site]['site_data'][variable]['uncommitted_transactions']) > 0:
                return sites[site]['site_data'][variable]['uncommitted_transactions'][-1]['value']
            else:
                return sites[site]['site_data'][variable]['value']
        else:
            return sites[site]['site_data'][variable]['committed_transactions'][-1]['value']
 

def write_value(site, variable, transactionName, time_step, value):
    sites[site]['site_data'][variable]['uncommitted_transactions'].append({
        'transaction' : transactionName, 
        'value' : value, 
        'committed_time' : time_step, 
    })





