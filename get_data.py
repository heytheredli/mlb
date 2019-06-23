import pandas as pd
import yaml



with open("config.yml", 'r') as stream:
    config = yaml.load(stream)

# print(config)
raw_data = {}

for rawfile in config['rawfiles'].keys():
    raw_data[rawfile] = pd.read_csv(config['rawfiles'][rawfile], nrows=10)

print(raw_data)
