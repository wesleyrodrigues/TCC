rm file_img_rc.py
pyrcc5 file_img.qrc -o file_img_rc.py

rm img_fixas_rc.py
pyrcc5 img_fixas.qrc -o img_fixas_rc.py

rm mainUi.py
python -m PyQt5.uic.pyuic -x mainUi.ui -o mainUi.py
