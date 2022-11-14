from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # Create scene
    self.image_item = QGraphicsPixmapItem()
    scene = QGraphicsScene(self)
    scene.addItem(self.image_item)

    # Create GraphicView display
    self.view = QGraphicsView(scene, self)
    # Adding right click menus
    self.view.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
    self.zoomout_action = QAction("Fit canvas", self)
    self.view.addAction(self.zoomout_action)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

image = QImage(camera_image, w, h, w, QImage.Format_Grayscale8)
self.image_item.setPixmap(QPixmap.fromImage(image))
self.view.fitInView(self.image_item)
