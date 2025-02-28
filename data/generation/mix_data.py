import json
import random

all_outputs = []

json_path1 = "/home/ubuntu/BitDistiller/data/datasets/qwen2.5-1.5b/wikitext_T0.7_N1024_S42_32.json"
json_path2 = "/home/ubuntu/BitDistiller/data/datasets/qwen2.5-1.5b/alpaca_T0.7_N1024_S42_16.json"

with open(json_path1, 'r') as f:
    dataset_for_eval = f.readlines()
for line in dataset_for_eval:
    json_data = json.loads(line)
    all_outputs.append(json_data)

with open(json_path2, 'r') as f:
    dataset_for_eval = f.readlines()
for line in dataset_for_eval:
    json_data = json.loads(line)
    all_outputs.append(json_data)

random.shuffle(all_outputs)

with open('../datasets/qwen2.5-1.5b/mix_wiki_alpaca_48.json', 'w') as f:
    for item in all_outputs:
        f.write(json.dumps(item) + '\n')
