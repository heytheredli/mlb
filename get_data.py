import pandas as pd
import yaml

with open("config.yml", 'r') as stream:
    CONFIG = yaml.load(stream)

# Grabbing and generating raw data (global variables)
RAW_DATA = {}

for rawfile in CONFIG['rawfiles'].keys():
    RAW_DATA[rawfile] = {"data": pd.read_csv(CONFIG['rawfiles'][rawfile], nrows=10)}
    RAW_DATA[rawfile]["all_cols"] = RAW_DATA[rawfile]["data"].columns
    RAW_DATA[rawfile]["id_cols"] = [col
                                        for col in RAW_DATA[rawfile]["data"].columns
                                            if col.lower() in [x.lower() for x in CONFIG['id_cols']]
                                    ]
for dataset in RAW_DATA.keys():
    print(dataset, "all cols : ", RAW_DATA[dataset]["all_cols"])
    print(dataset, "id cols: ", RAW_DATA[dataset]["id_cols"])

def join_data(data1_name, data2_name):
    """
    Function to join two datasets together (left on data1, data2 into data1)

    Inputs
    ------

    data1_name: String - base dataset
    data2_name: String - dataset to be joined to data1

    Returns
    -------

    dict(joined_dataset, all columns of joined dataset, id columns of joined dataset)
    """
    data1 = pd.read_csv(CONFIG['rawfiles'][data1_name])
    data2 = pd.read_csv(CONFIG['rawfiles'][data2_name])
    join_keys = list(set(RAW_DATA[data1_name]['id_cols']).intersection(RAW_DATA[data2_name]['id_cols']))
    joined_data = data1.merge(data2, how='left', on=join_keys)
    return {"data": joined_data, "all_cols": joined_data.columns, "id_cols": join_keys}

final_data = {}
final_data['People_Batting'] = join_data('People', 'Batting')
print(final_data['People_Batting'])
