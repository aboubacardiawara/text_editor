import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile, QTextStream
class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		self.zone_centrale = QTextEdit()
		self.setCentralWidget(self.zone_centrale)
		self.toolBar = self.addToolBar('File')
		self.menuBar = self.menuBar()
		self.status_bar = self.statusBar()
		
	
	def AddFileMenu(self, ):
		"""
		open
		save
		copy
		quit
		"""
		fileMenu = self.menuBar.addMenu("Fichier")
		
		self.addToMenu({'name': 'open', 'shortCut': 'Ctrl+o'}, [fileMenu, self.toolBar])
		self.addToMenu({'name': 'save', 'shortCut': 'Ctrl+s'}, [fileMenu, self.toolBar])
		self.addToMenu({'name': 'copy', 'shortCut': 'Ctrl+c'}, [fileMenu, self.toolBar])
		self.addToMenu({'name': 'cut', 'shortCut': 'Ctrl+x'}, [fileMenu, self.toolBar])
		self.addToMenu({'name': 'new', 'shortCut': 'Ctrl+N'}, [fileMenu, self.toolBar])
		self.addToMenu({'name': 'paste', 'shortCut': 'Ctrl+v'}, [fileMenu, self.toolBar])
		self.addToMenu({'name': 'quit', 'shortCut': 'ctrl+Q'}, [fileMenu, self.toolBar])
		
		
		
	def addToMenu(self, props, menuParents):
		"""
		"""
		actions = {
			"open": self.openFile,
			"close": self.close,
			"save": self.saveFile,
			"copy": self.copy,
			"cut": self.cut,
			"new": self.new,
			"paste": self.past,
			"quit": self.quitApp
		}
		
		name_0 = props['name']
		path = "../assets/"
		iconPath = path + name_0 + ".png"
		name = name_0[0].upper() + name_0[1:] + "..."
		shortCut = props['shortCut']

		newAct = QAction (QIcon(iconPath), name, self)
		newAct.setShortcut(shortCut)
		newAct.triggered.connect(actions[name_0])
		#connect(click, SIGNAL(), this, SLOT(lambda x:print("hummm!")))
		for parent in menuParents:
			parent.addAction(newAct)

	def init(self):
		self.AddFileMenu()


	def openFile(self):
		filePath = QFileDialog.getOpenFileName(self, 'Open file', '/home', 'All Files (*.*)')
		file = QFile(filePath[0])
		file.open(QFile.ReadOnly | QFile.Text)
		stream = QTextStream(file)
		contains = stream.readAll()
		self.zone_centrale.setPlainText(contains)


	def saveFile(self):
		filePath = QFileDialog.getSaveFileName(self, 'Save File', '/home')
		contain = self.zone_centrale.toPlainText()
		with open(filePath[0], 'w') as file:
			file.write(contain)


	def copy(self):
		print("save")
	
	def cut(self):
		print("cut")

	def new(self):
		print("new")

	def past(self):
		print("past")

	def quitApp(self):
		msg = QMessageBox()
		choice = msg.question(self, '', "Do you want to exit ?", QMessageBox.Yes | QMessageBox.No)
		if choice == QMessageBox.Yes:
			QApplication.quit()

def main(args):
	app = QApplication(args[1:])
	mainWindow = MainWindow()
	mainWindow.init()
	mainWindow.show()
	app.exec_()


if __name__ == "__main__":
	import sys
	print("execution du programme")
	main(sys.argv)