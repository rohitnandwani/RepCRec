import LockManager
import DataManager


def fail():
    #TransactionManager.abort_all_ongoing_transactions
    pass

def recover():
    pass



def process_pending_operations(time_step):
    #if there are any read only transactions let them go through first
    #check if there are any exclusive locks / read locks on the variable
        #if yes:
            #check if there are any operations for that transaction
            #if yes:
                #do the first pending operation for that variable
            #if no: 
                #keep waiting

        #if no:
            #do the first pending operation 
                #if read 
                    #give shared lock 
                #if write:
                    #give exclusive lock

    for site in sites:
        pending_operations_by_key = {}
        for pending_operation in site['pending_operations']:
            if pending_operation['variable'] not in pending_operations_by_key.keys():
                pending_operations_by_key[pending_operation['variable']] = [pending_operation]
            else:
                pending_operations_by_key[pending_operation['variable']].append(pending_operation)
        for pending_operations_for_key in pending_operations_by_key.keys():
            #if there are any read only transactions let them go through first
            for pending_operation_for_key in pending_operations_for_key:
                if pending_operation_for_key['type'] == 'read_only':
                    DataManager.read_value(site, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], time_step, pending_operation_for_key['type'])
                    break
            
            #check if there are any exclusive locks / read locks on the variable
            existing_lock = False
            existing_lock_transaction = None
            for lock in site[pending_operation_for_key['variable']]['locks']:
                if lock['type'] == 'exclusive' or lock['type'] == 'shared':
                    existing_lock = True
                    existing_lock_transaction = lock['transaction']
            
            if existing_lock == True:
                for pending_operation_for_key in reversed(pending_operations_for_key):
                    if pending_operation_for_key['transaction'] == existing_lock_transaction:
                        if pending_operation_for_key['type'] == 'read':
                            LockManager.acquire_lock(site, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], 'shared')
                            DataManager.read_value(site, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], time_step, 'read')
                        elif pending_operations_for_key[-1]['type'] == 'write':
                            LockManager.acquire_lock(site, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], 'exclusive')
                            DataManager.write_value(site, pending_operation_for_key['variable'], pending_operation_for_key['transaction'], time_step, pending_operation_for_key['value'])
                        break
                break
            else:
                if pending_operations_for_key[-1]['type'] == 'read':
                    LockManager.acquire_lock(site, pending_operations_for_key[-1]['variable'], pending_operations_for_key[-1]['transaction'], 'shared')
                    DataManager.read_value(site, pending_operations_for_key[-1]['variable'], pending_operations_for_key[-1]['transaction'], time_step, 'read')
                elif pending_operations_for_key[-1]['type'] == 'write':
                    LockManager.acquire_lock(site, pending_operations_for_key[-1]['variable'], pending_operations_for_key[-1]['transaction'], 'exclusive')
                    DataManager.write_value(site, pending_operations_for_key[-1]['variable'], pending_operations_for_key[-1]['transaction'], time_step, pending_operations_for_key[-1]['value'])
                    break





def process_recovery():
    pass

def process_failure():
    pass
