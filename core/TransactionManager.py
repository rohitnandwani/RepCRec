from util.config import *

import SiteManager
import LockManager

def get_sites_for_variable(variable):
    sites_for_variable = []
    for site_name, site in sites.iteritems():
        if variable in site['site_data'].keys():
            sites_for_variable.append(site_name)
    return sites_for_variable


def begin_transaction(transactionName, time_step, read_only):
    transactions[transactionName] = {
        'read_only': read_only,
        'pending_operations': [], 
        'start_time': time_step,
        'locks': {},
        'failed': False,
        'abort_reason' : None
    }


def read_operation(transaction, variable):
    if (transactions[transaction]['read_only'] == True):
        read_type = 'read_only'
    else:
        read_type = "read"
    sites_for_variable = get_sites_for_variable(variable)
    for site in sites_for_variable:
        sites[site]['pending_operations'].append({
            'transaction' : transaction, 
            'variable' : variable, 
            'type' : read_type
        })


def write_operation(transaction, variable, value):
    sites_for_variable = get_sites_for_variable(variable)
    for site in sites_for_variable:
        sites[site]['pending_operations'].append({
            'transaction' : transaction, 
            'variable' : variable, 
            'value' : value, 
            'type' : 'write'
        })


def commit_transaction(transaction):
    LockManager.release_locks_on_transaction(transaction)
    SiteManager.process_uncommitted_transactions(transaction, True)
    del transactions[transaction]


def abort_transaction(transaction, abort_reason="site_failure"):
    LockManager.release_locks_on_transaction(transaction)
    SiteManager.process_uncommitted_transactions(transaction, False)
    print ("Transaction " + transaction + "aborted. Reason " + abort_reason)
    del transactions[transaction]


#assumes no transaction is waiting at any site on end
def end_transaction(transaction, time_step):
    commit_transaction(transaction)


def process_site_failure(site):
    unique_transactions_to_abort = []
    for pending_operation in sites[site]['pending_operations']:
        if pending_operation['tansaction'] not in unique_transactions_to_abort:
            unique_transactions_to_abort.append(pending_operation['transaction'])
    for unique_transaction in unique_transactions_to_abort:
        abort_transaction(transaction, 'site_failure')



def dump():
    for site in sites.keys():
        to_print = ""
        to_print += "site " + site + " - "
        for variable in sorted(sites[site]['site_data'].keys()):
            to_print += variable + ": " + str(sites[site]['site_data'][variable]['value']) + " "
        print (to_print)










