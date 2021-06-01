import pickle
import json
import numpy as np
import gzip, pickle, pickletools

__locations = None
__data_columns = None
__types = None
__model = None

def get_estimated_price(suburb, type, rooms, distance):
    try:
        loc_index = __data_columns.index(suburb.lower())
    except:
        loc_index = -1

    try:
        type_index = __data_columns.index(type.lower())
    except:
        type_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = rooms
    x[1] = distance

    if loc_index >= 0:
        x[loc_index] = 1

    if type_index >= 0:
        x[type_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __types

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:-3]
        __types = __data_columns[-3:]

    global __model
    if __model is None:
        # with open('./artifacts/melbourne_housing_model.pickle', 'rb') as f:
        #     rf = pickle.Unpickler(f)
        #     __model = pickle.load(rf)

        with open('./artifacts/melbourne_housing_model.pickle', 'rb') as f:
            p = pickle.Unpickler(f)
            __model = p.load()

    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

def get_type_names():
    return __types

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_type_names())
    print(get_estimated_price('Suburb_Abbotsford', 'Type_h', 3, 3))