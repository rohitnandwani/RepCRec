def initialise():
    for i in range(0, NUMBER_OF_VARIABLES):
        variable = "x" + str(i+1)
        value = 10 * (i + 1)
        data[variable] = {
            'value' : value, 
            'committed_transactions' : [
                #transaction
                #value
                #committed_time
            ], 
            #This field will likely not be required. KEEP
            'uncommitted_transactions' : [
                #transaction
                #value
                #committed_time
            ], 
            'locks' : [
                #type: //shared or exclusive
                #transaction: 
            ], 
            #This field will likely not be required. REMOVE
            'waiting_locks' : [
                #type: //shared or exclusive
                #transaction: 
            ]
        }

    for i in range(0, NUMBER_OF_SITES):
        index = str(i+1)
        site_data_indices = []
        site_data = {}
        for j in range(0, NUMBER_OF_VARIABLES):
            if (1 + ((j+1) % 10) == i + 1):
                site_data_indices.append(j+1)
                site_data["x" + str(j+1)] = data["x" + str(j+1)]
            elif ((j+1) % 2 == 0):
                site_data_indices.append(j+1)
                site_data["x" + str(j+1)] = data["x" + str(j+1)]
        sites[index] = {
            'site_data' : site_data, 
            'available': True,
            'pending_operations': [],
            'failed_time' : TIME_STEP, 
            'recovered_time' : TIME_STEP
        }

    return