__author__ = 'mpearmain'

'''
    A set of functions to take an xgboost model and extract the feature importance.
    The use case is to take out 'best' model and split into mod(n) sets of features, we are then able to retrain
    the the _n_ new models using the same parameters that produced out model and ensemble the resulting predictions

'''

def generate_feature_labels(booster, mod_no):
    '''
        After training an xgboost model (bst) expected input to function would be 'bst._Booster'
    :param booster : Booster, XGBModel or dict
                     Booster or XGBModel instance, or dict taken by Booster.get_fscore()
    :param mod_no: The mod number of lists to create a return.
    :return: A list of lists, with length mod(n)
    '''

    if isinstance(booster, Booster):
        importance = booster.get_fscore()
    elif isinstance(booster, dict):
        importance = booster
    else:
        raise ValueError('tree must be Booster or dict instance')

    if len(importance) == 0:
        raise ValueError('Booster.get_fscore() results in empty')

    tuples = [(k, importance[k]) for k in importance]
    # Sort the features
    tuples = sorted(tuples, key=lambda x: x[1])
    feature_lists = [tuples[i::mod_no] for i in range(mod_no)]

    # Finally lets get the feature labels we want in a list

    feature_labels = [[item[0] for item in l] for l in feature_lists]

    return feature_labels








