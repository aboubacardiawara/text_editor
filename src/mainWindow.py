import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile, QTextStream
class MainWindow(QMainWindow):
	"""Main window of the text editor.
		The text editor contains:
  			- a tool bar
			- a central zone
			- a status bar

	Args:
		QMainWindow ([type]): [description]
	"""
	def __init__(self) -> None:
		super().__init__()
		self.zone_centrale = QTextEdit()
		self.setCentralWidget(self.zone_centrale)
		self.toolBar = self.addToolBar('File')
		self.menuBar = self.menuBar()
		self.status_bar = self.statusBar()
		
	
	def AddFileMenu(self, ):
		"""
		build the components of the tool bar.
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
		manage the building of the menu bar. 
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
		"""run the building of window components 
		"""
		self.AddFileMenu()


	def openFile(self):
		"""
			allow to open a directory manager. (see slot)
  		"""
		filePath = QFileDialog.getOpenFileName(self, 'Open file', '/home', 'All Files (*.*)')
		file = QFile(filePath[0])
		file.open(QFile.ReadOnly | QFile.Text)
		stream = QTextStream(file)
		contains = stream.readAll()
		self.zone_centrale.setPlainText(contains)


	def saveFile(self):
		"""allow to save file in local file system (see slot)
		"""
		filePath = QFileDialog.getSaveFileName(self, 'Save File', '/home')
		contain = self.zone_centrale.toPlainText()
		with open(filePath[0], 'w') as file:
			file.write(contain)


	def copy(self):
		"""copy a textual contain
		"""
		print("copy")
	
	def cut(self):
		"""cut a textual contain"""
		print("cut")

	def new(self):
		"""create a new file
		"""
		print("new")

	def past(self):
		"""past a textual contain"""
		print("past")

	def quitApp(self):
		"""allow to close safety the app"""
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