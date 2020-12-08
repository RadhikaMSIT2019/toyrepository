class least_class:
    def __init__(self,size):
        self.size =size
        self.least =[]
        self.leastcache ={}

# this function gets least recently used
    def get(self,key):
        if key in self.least:
            return self.leastcache[key]
        else:
            return None
#
    def put(self,key):
        value ="www."+str(key)+".com"

        if(len(self.least) < self.size):
            if key in self.least:

                self.least.remove(key)
                self.least.append(key)
                self.leastcache[key] = value
            else:
                self.least.append(key)
                self.leastcache[key] = value

        else:
            val2 =self.least.pop(0)
            self.least.append(key)
            del self.leastcache[val2]
            self.leastcache[key] = value


    def get_cache(self):
            ls =[]
            for k in reversed(self.least):
                ls.append(k+" : "+self.leastcache[k] )
            return ls