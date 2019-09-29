import os,json

class Loader():
    def __init__(self):
        self.path = "./jsons/"
        self.t_names = {}
        self.a_names = {}
        self.ag_names = {}
        
        self.listOfDirectories("Test/",self.t_names)
        self.listOfDirectories("Action/",self.a_names)
        self.listOfDirectories("Aggregation/",self.ag_names)

    def listOfDirectories (self,folder,names):
        list_dir = os.listdir(self.path + folder)
        for i in range(len(list_dir)) :
            name = list_dir[i].split("-",1) 
            if name[0] != ".DS_Store":
                names.update({name[0].upper() : list_dir[i]})
        
    def readFile(self,folder,file_name):
        with open(os.path.join(self.path,folder,file_name)) as json_file:
            data = json.load(json_file)
        return data
