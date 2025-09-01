class TextSpeaker:
    def speak(self): return "Hello!"

class AirHorn:
    def speak(self): return "HOOONK!"

def make_it_speak(thing):
    # Works for any object that has a .speak() method
    print(thing.speak())



make_it_speak(TextSpeaker())
make_it_speak(AirHorn())