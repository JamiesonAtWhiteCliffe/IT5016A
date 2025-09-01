class Engine:
    def ignite(self): return "Engine on."

class Car:
    def __init__(self):
        self.engine = Engine() #Car has-an Engine
    
    def start(self): return self.engine.ignite()

c = Car()
print(c.start())