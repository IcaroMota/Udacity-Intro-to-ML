#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    
    ### your code goes here
    errors = []
    i = 0
    for predict in predictions:
        errors.append(abs(predict - net_worths[i]))
        i = i+1

    largest_list = []
    aux_errors = errors[:]

    for x in range(9):
        largest_error = max(aux_errors)
        largest_list.append(largest_error)
        aux_errors.remove(largest_error)
    
    cleaned_data = []
    i = 0
    
    for predict in predictions:
        if errors[i] in largest_list:
            pass
        else:
            cleaned_data.append((ages[i], net_worths[i], errors[i]))
        i = i+1
    
    
    return cleaned_data

