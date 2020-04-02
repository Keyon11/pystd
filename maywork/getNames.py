import os
import io
import sys

sacePath = "D:\\tmp\\may\\核维制度管理"

def gci(path):
  parents = os.listdir(path)
  for parent in parents:
    child = os.path.join(path,parent)
    if os.path.isdir(child):
      gci(child)
    else:
      pathStr = os.path.split(child)[0]	#获取文件目录
      pathStr = pathStr[len(sacePath)+1:]	#文件目录丢弃输入目录部分
      fileName,extName = os.path.splitext(child)
      fileName = os.path.basename(child)
      onlyName = fileName[:len(fileName)-len(extName)]	#去除文件后缀
      pathStr = pathStr.replace('\\',',')	#输出csv文件格式，将\替换成,
      print("%s,%s"% (pathStr,onlyName))
      #pathArray = path.split('\\')
      #arraySize = len(pathArray)
      #print("%s,%s,%s"%(pathArray[arraySize-2],pathArray[arraySize-1],onlyName))
      #print(path ,onlyName)

if __name__ == '__main__':
  sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
  gci(sacePath)