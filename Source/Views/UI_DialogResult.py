# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/DialogResult.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgResult(object):
    def setupUi(self, DlgResult):
        DlgResult.setObjectName("DlgResult")
        DlgResult.setWindowModality(QtCore.Qt.NonModal)
        DlgResult.resize(422, 454)
        DlgResult.setMinimumSize(QtCore.QSize(300, 300))
        DlgResult.setStyleSheet("QWidget{\n"
"background-color:rgb(247, 255, 229);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:white;\n"
"border:1px solid rgb(196, 215, 178);\n"
"border-radius:5px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:white;\n"
"border:1px solid rgb(196, 215, 178);\n"
"border-radius:5px;\n"
"padding:5px;\n"
"min-height:25px;\n"
"}")
        DlgResult.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DlgResult)
        self.verticalLayout.setContentsMargins(20, 15, 20, 15)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_name_title = QtWidgets.QLabel(DlgResult)
        self.lbl_name_title.setObjectName("lbl_name_title")
        self.gridLayout.addWidget(self.lbl_name_title, 2, 0, 1, 1)
        self.lbl_info_1_title = QtWidgets.QLabel(DlgResult)
        self.lbl_info_1_title.setObjectName("lbl_info_1_title")
        self.gridLayout.addWidget(self.lbl_info_1_title, 3, 0, 1, 1)
        self.lbl_ctg_title = QtWidgets.QLabel(DlgResult)
        self.lbl_ctg_title.setObjectName("lbl_ctg_title")
        self.gridLayout.addWidget(self.lbl_ctg_title, 1, 0, 1, 1)
        self.lbl_spedies_title = QtWidgets.QLabel(DlgResult)
        self.lbl_spedies_title.setObjectName("lbl_spedies_title")
        self.gridLayout.addWidget(self.lbl_spedies_title, 0, 0, 1, 1)
        self.lbl_info_2_title = QtWidgets.QLabel(DlgResult)
        self.lbl_info_2_title.setObjectName("lbl_info_2_title")
        self.gridLayout.addWidget(self.lbl_info_2_title, 4, 0, 1, 1)
        self.lbl_spedies_txt = QtWidgets.QLabel(DlgResult)
        self.lbl_spedies_txt.setText("")
        self.lbl_spedies_txt.setObjectName("lbl_spedies_txt")
        self.gridLayout.addWidget(self.lbl_spedies_txt, 0, 1, 1, 1)
        self.lbl_ctg_txt = QtWidgets.QLabel(DlgResult)
        self.lbl_ctg_txt.setText("")
        self.lbl_ctg_txt.setObjectName("lbl_ctg_txt")
        self.gridLayout.addWidget(self.lbl_ctg_txt, 1, 1, 1, 1)
        self.lbl_name_txt = QtWidgets.QLabel(DlgResult)
        self.lbl_name_txt.setText("")
        self.lbl_name_txt.setObjectName("lbl_name_txt")
        self.gridLayout.addWidget(self.lbl_name_txt, 2, 1, 1, 1)
        self.lbl_info_txt = QtWidgets.QLabel(DlgResult)
        self.lbl_info_txt.setText("")
        self.lbl_info_txt.setObjectName("lbl_info_txt")
        self.gridLayout.addWidget(self.lbl_info_txt, 3, 1, 1, 1)
        self.lbl_info_2_txt = QtWidgets.QLabel(DlgResult)
        self.lbl_info_2_txt.setText("")
        self.lbl_info_2_txt.setObjectName("lbl_info_2_txt")
        self.gridLayout.addWidget(self.lbl_info_2_txt, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_analyze = QtWidgets.QPushButton(DlgResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_analyze.sizePolicy().hasHeightForWidth())
        self.btn_analyze.setSizePolicy(sizePolicy)
        self.btn_analyze.setMinimumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_analyze.setFont(font)
        self.btn_analyze.setStyleSheet("")
        self.btn_analyze.setObjectName("btn_analyze")
        self.horizontalLayout.addWidget(self.btn_analyze)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_main = QtWidgets.QPushButton(DlgResult)
        self.btn_main.setMinimumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_main.setFont(font)
        self.btn_main.setAutoDefault(False)
        self.btn_main.setFlat(True)
        self.btn_main.setObjectName("btn_main")
        self.horizontalLayout.addWidget(self.btn_main)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(DlgResult)
        QtCore.QMetaObject.connectSlotsByName(DlgResult)

    def retranslateUi(self, DlgResult):
        _translate = QtCore.QCoreApplication.translate
        DlgResult.setWindowTitle(_translate("DlgResult", "진단결과"))
        self.lbl_name_title.setText(_translate("DlgResult", "내용 : "))
        self.lbl_info_1_title.setText(_translate("DlgResult", "원인 : "))
        self.lbl_ctg_title.setText(_translate("DlgResult", "구분 : "))
        self.lbl_spedies_title.setText(_translate("DlgResult", "품종 : "))
        self.lbl_info_2_title.setText(_translate("DlgResult", "대처법 : "))
        self.btn_analyze.setText(_translate("DlgResult", "추가진단"))
        self.btn_main.setText(_translate("DlgResult", "메인화면"))
