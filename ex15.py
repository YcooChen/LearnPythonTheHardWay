from sys import argv  #引入参数变量
script, filename = argv #解包，参数赋予左边的变量名

txt = open(filename) #打开名为filename的文件

print "Here's your file %r:" % filename #打印字符串
print txt.read() #打印filename文件内容
txt.close()

print "Type the filename again:" #打印字符串
file_again = raw_input(">") #输入文件名

txt_again = open(file_again) #打开文件名为file_again的文件

print txt_again.read() #打印file_again的文件内容
txt_again.close()