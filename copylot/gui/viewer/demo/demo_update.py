# flake8: noqa
from time import sleep

from skimage import data

from copylot.gui.viewer.viewer import Viewer


def main():
    camera = data.camera()

    viewer = Viewer(img_data=camera)

    viewer.run()

    sleep(1)

    viewer.update(data.cell())


if __name__ == '__main__':
    main()
