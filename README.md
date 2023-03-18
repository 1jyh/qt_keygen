project.py中可以构建您的代码

xiaoyu.py是各类接口，可以自己编写并且调用

对于打包，用pyinstaller 就行了

记得用一个相对干净的环境

```
conda create -n pyqt_keygen_39 python=3.9
conda activate pyqt_keygen_39
# 其他的你需要用什么就自己装
# qt环境不讲
pyinstaller -Fw main.py
```



