from util.config import *

import LockManager
import DataManager
import TransactionManager


def process_pending_operation(pending_operation):



def process_pending_operations(time_step):
    #transactions are not read or write then miss the time step
    #if there are any read only transactions let them go through first
    #check if there are any exclusive locks on the variable
        #if yes:
            #check if there are any operations for that transaction
            #if yes:
                #do the first pending operation for that variable
            #if no: 
                #keep waiting

        #if no:
            #do the first pending operation 
            #keep doing this till end of pending operations or when one transaction gets satisfied
                #if read 
                    #give shared lock 
                #if write: 
                    #check if there are any read locks on the transaction
                    #if not:
                        #give exclusive lock

    for site_name, site in sites.iteritems():

        if site['available'] == False:
            break

        pending_operations_by_key = {}
        for pending_operation in site['pending_operations']:
            if pending_operation['variable'] not in pending_operations_by_key.keys():
                pending_operations_by_key[pending_operation['variable']] = [pending_operation]
            else:
                pending_operations_by_key[pending_operation['variable']].append(pending_operation)
        for key_name, pending_operations_for_key in pending_operations_by_key.iteritems():
            #if there are any read only transactions let them go through first
            for pending_operation_for_key in pending_operations_for_key:
                if pending_operation_for_key['type'] == 'read_only':
                    DataManager.read_value(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], time_step, pending_operation_for_key['type'])
                    break
            
            #check if there are any exclusive locks / read locks on the variable
            existing_lock = False
            existing_lock_type = None
            existing_lock_transaction = None
            

            for lock in sites[site_name]['site_data'][pending_operation_for_key['variable']]['locks']:
                if lock['type'] == 'exclusive':
                    existing_lock = True
                    existing_lock_type = 'exclusive'
                    existing_lock_transaction = lock['transaction']
            
            if existing_lock == True and existing_lock_type == 'exclusive':
                completed_pending_operation = None
                for pending_operation_for_key in reversed(pending_operations_for_key):
                    if pending_operation_for_key['transaction'] == existing_lock_transaction:
                        if pending_operation_for_key['type'] == 'read':
                            LockManager.acquire_lock(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], 'shared')
                            DataManager.read_value(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], time_step, 'read')
                            completed_pending_operation = pending_operation_for_key
                        elif pending_operation_for_key['type'] == 'write':
                            LockManager.acquire_lock(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], 'exclusive')
                            DataManager.write_value(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], time_step, pending_operation_for_key['value'])
                            completed_pending_operation = pending_operation_for_key

                        if completed_pending_operation is not None:
                            updated_pending_operations_for_site = []
                            deleted_pending_operation = False
                            for pending_operation in reversed(sites[site_name]['pending_operations']):
                                if (not pending_operation == completed_operation) and deleted_pending_operation == False:
                                    updated_pending_operations_for_site.append(pending_operation)
                            sites[site_name]['pending_operations'] = reversed(updated_pending_operations_for_site)
                            break


            else:
                completed_pending_operation = None
                for pending_operation_for_key in reversed(pending_operations_for_key):
                    #do not forget to pending operations once processed
                    if pending_operation_for_key['type'] == 'read':
                        LockManager.acquire_lock(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], 'shared')
                        DataManager.read_value(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], time_step, 'read')
                        completed_pending_operation = pending_operation_for_key
                    elif pending_operation_for_key['type'] == 'write':
                        if existing_lock == False:
                            LockManager.acquire_lock(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], 'exclusive')
                            DataManager.write_value(site_name, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], time_step, pending_operation_for_key['value'])
                            completed_pending_operation = pending_operation_for_key

                    if completed_pending_operation is not None:
                        updated_pending_operations_for_site = []
                        deleted_pending_operation = False
                        for pending_operation in reversed(sites[site_name]['pending_operations']):
                            if (not pending_operation == completed_operation) and deleted_pending_operation == False:
                                updated_pending_operations_for_site.append(pending_operation)
                        sites[site_name]['pending_operations'] = reversed(updated_pending_operations_for_site)
                        break


def process_uncommitted_transactions(transaction, is_transaction_successful):
    for site in sites.keys():
        for variable in sites[site]['site_data'][variable]:
            if is_transaction_successful == True:
                sites[site]['site_data'][variable]['committed_transactions'].append(sites[site]['site_data'][variable]['uncommitted_transactions'])
            else:
                sites[site]['site_data'][variable]['uncommitted_transactions'] = []



def fail(site, time_step):
    sites[site]['available'] == False
    #sites[site]['pending_operations'] = []
    TransactionManager.process_site_failure(site)
    return


def recover(site, time_step):
    sites[site]['available'] == True
    sites[site]['reset_time'] == time_step
    #TransactionManager.process_site_recovery
