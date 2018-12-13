import os,yaml

class Read_Yaml:
    def __init__(self,file_name):
        self.file_path = os.getcwd() + os.sep + 'Yaml' + os.sep + file_name
    def read_yaml(self):
        with open(self.file_path,'r',encoding='utf-8') as f:
            yaml_data = yaml.load(f)
        return yaml_data
