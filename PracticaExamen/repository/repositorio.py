class Repositorio:
    def __init__(self):
        self.data=[]
        self.index={}

    def add(self,key,obj):
        if key in self.index:
            raise ValueError("Elemento ya existe")

        self.data.append(obj)
        self.index[key]=obj

    def get(self,key):
        return self.index.get(key)

    def get_all(self):
        return self.data

    def delete(self,key):
        obj=self.index.pop(key,None)
        if obj:
            self.data.remove(obj)
