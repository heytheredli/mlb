import pandas as pd
import yaml

with open("config.yml", 'r') as stream:
    config = yaml.load(stream)

raw_data = {}

for rawfile in config['rawfiles'].keys():
    raw_data[rawfile] = {"data": pd.read_csv(config['rawfiles'][rawfile], nrows=10)}
    raw_data[rawfile]["all_cols"] = raw_data[rawfile]["data"].columns
    raw_data[rawfile]["id_cols"] = [col
                                        for col in raw_data[rawfile]["data"].columns
                                            if col.lower() in [x.lower() for x in config['id_cols']]
                                    ]
for dataset in raw_data.keys():
    print(dataset, "all cols : ", raw_data[dataset]["all_cols"])
    print(dataset, "id cols: ", raw_data[dataset]["id_cols"])
