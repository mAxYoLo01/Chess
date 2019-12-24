all: linux

gui:
	pyuic5 -o ui_chessboard.py chessboard.ui

ressources:
	pyrcc5 resources/resource.qrc -o resource_rc.py

linux: gui ressources

clean:
	rm -rf dist build ui.py
