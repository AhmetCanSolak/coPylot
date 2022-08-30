# flake8: noqa
from time import sleep

from skimage import data
from vispy import app

from copylot.gui.viewer.viewer import Viewer


def main():
    camera = data.cell()

    viewer = Viewer(img_data=camera)

    def update_methd(ev):
        sleep(1)
        viewer.update(data.camera())
        # sleep(1)
        # viewer.update(data.cell())

    timer = app.Timer()
    timer.connect(update_methd)
    timer.start(0)

    viewer.run()


if __name__ == '__main__':
    main()
