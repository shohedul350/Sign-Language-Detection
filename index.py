import yaml
with open("data.yml", 'r') as stream;
    num_classes = str(yaml.safe_load(stream)['nc'])