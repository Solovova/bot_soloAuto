import time
from PyQt5.QtCore import QThread, pyqtSignal  # pylint: disable=no-name-in-module, import-error
from engine import Engine
import pyautogui
from funArea import areaStrToList # pylint: disable=no-name-in-module, import-error

class TreadWorker(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    loop = 0

    def __init__(self, window):
        QThread.__init__(self)
        self._isRunning = True
        self._isActive = False
        self.engine = Engine(window.listAutoObject)
        
    def run(self):
        while self._isRunning:
            time.sleep(0.1)
            if self._isActive:
                self.mainLoop()

    def stop(self):
        self._isRunning = False

    def changeState(self):
        self._isActive = not self._isActive

    def _commandGoToScreenMain(self):
        while not self.engine.isAreaByName("btnSleep"):
            self.engine.clickToAreaByName("btnFind")
            

    def _commandGoToScreenSearch(self):
        while not self.engine.isAreaByName("btnWoodHarvest"):
            self.engine.clickToAreaByName("btnFind")

    def _commandFES(self):
        food = int(self.engine.getTextByName("txtFood"))
        water = int(self.engine.getTextByName("txtWater"))
        energy = int(self.engine.getTextByName("txtEnergy"))

        maxFood = 100
        maxWater = 100
        oneFood = 20
        oneWater = 35

        if (food<20):
            while True:
                self._commandGoToScreenMain()
                self.engine.clickToAreaByName("btnFood")
                food = int(self.engine.getTextByName("txtFood"))
                if (food > (maxFood - oneFood)):
                    break

        if (water<20):
            while True:
                self._commandGoToScreenMain()
                self.engine.clickToAreaByName("btnWater")
                water = int(self.engine.getTextByName("txtWater"))
                if (water > (maxWater - oneWater)):
                    break

        if (energy < 30):
            self._commandGoToScreenMain()
            self.engine.clickToAreaByName("btnSleep")
            self.engine.clickToAreaByName("bntSleepDoIt")
            time.sleep(8)

    def _commandHarvestMoveSlider(self):
        find, point = self.engine.getAreaCoordByName("btnHarverWoodSlider")
        if find:
            isObj, autoObject  = self.engine.getAutoObjectByName("btnHarverWoodSlider")
            if isObj:
                area2 = areaStrToList(autoObject.area2)
                moveFX = point[0] + area2[0]
                moveFY = point[1] + area2[1]
                pyautogui.moveTo(moveFX, moveFY)
                pyautogui.drag(area2[2] - moveFX, 0, 1, button='left')
                time.sleep(0.2)

    def _commandHarvest(self):
        self._commandGoToScreenSearch()
        self.engine.clickToAreaByName("btnWoodHarvest")
        self._commandHarvestMoveSlider()
        self.engine.clickToAreaByName("btnWoodHarvestDoIt")
        time.sleep(1)
        while self.engine.isAreaByName("pbHarvestWood"):
            time.sleep(0.5)
        
    def mainLoop(self):
        print(self.loop)
        self.loop = self.loop + 1
        time.sleep(0.1)
        self._commandFES()
        self._commandFES()
        self._commandHarvest()
