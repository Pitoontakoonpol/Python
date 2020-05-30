from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from math import pi, sin, cos
from panda3d.core import Filename
from direct.actor.Actor import Actor


winfile = "/home/pitoon/snap/python/3D/Box.egg"
pandafile = Filename.fromOsSpecific(winfile)
print(pandafile)

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("/home/pitoon/snap/python/3D/Wolf.egg")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.125, 0.225, 0.25)
        self.scene.setPos(-8, 45, 0)

        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        self.pandaActor = Actor("/home/pitoon/snap/python/3D/Wolf.egg",{"Walk":"/home/pitoon/snap/python/3D/Box.egg"})
        self.pandaActor.reparentTo(self.render)

        self.pandaActor.loop("Walk")

    def spinCameraTask(self, task):
        angleDegree = task.time * 6.0
        angleRadins = angleDegree * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadins), -20 * cos(angleRadins), 3)
        self.camera.setHpr(angleDegree, 0, 0)
        return task.cont


app = MyApp()
app.run()