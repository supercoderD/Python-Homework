from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def showdevice(self, name):
        print("The device name is", name)

    @abstractmethod
    def turnon():
        pass

class SmartLight(SmartDevice):
    def turnon():
        print("Smart Light is now officialy on.")
class SmartFan(SmartDevice):
    def turnon():
        print("Smart Fan is now officialy on.")
class SmartSpeaker(SmartDevice):
    def turnon():
        print("Smart Speaker is now officialy on.")

Light=SmartLight()
Fan=SmartFan()
Speaker=SmartSpeaker()
Light.showdevice("The Bedroom Light is on.")
Fan.showdevice("the Bedroom Fan is on.")
Speaker.showdevice("The Bedroom Music Speaker is on.")
class SmartCamera:
    def statuscheck(self):
        print("The Smart Camera is now recording.")
class SmartDoorLock:
    def statuscheck(self):
        print("All doors are locked.")

allotherdevices=[SmartCamera(), SmartDoorLock()]
print("")
print("=Smart Device Status==")
for device in allotherdevices:
    device.statuscheck()
print("====")
