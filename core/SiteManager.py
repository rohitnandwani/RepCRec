def fail():
    #TransactionManager.abort_all_ongoing_transactions
    pass

def recover():
    pass

def process_pending_operations():
    for site in sites:
        for variable in site[site_data]:
            #if read only, process that first
            #check if there are any exclusive locks / read locks on the variable
                #if yes:
                    #check if there are any operations for that transaction
                    #if yes:
                        #do the first pending operation for that variables
                    #if no: 
                        #keep waiting
                #if no:
                    #do the first pending operation 
                        #if read 
                            #give shared lock 
                        #if write:
                            #give exclusive lock, 

def process_recovery():
    pass

def process_failure():
    pass
