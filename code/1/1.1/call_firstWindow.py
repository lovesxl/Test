#导入模块、导入类
import sys
from  PyQt5.QtWidgets import QApplication,QWidget
if __name__ =="__main__":
    #实例化一个应用
    app=QApplication(sys.argv)
    #实例化一个窗口
    w=QWidget()
    #设置窗口大小
    w.resize(400,200)
    #移动窗口
    w.move(300,300)
    #设置窗口标题
    w.setWindowTitle("这是第一个窗口")
    #打开窗口
    w.show()
    #循环安全退出
    sys.exit(app.exec_())
