#coding:utf-8

import xlwt,xlrd,string
from xlutils.copy import copy
import datetime

class cddata():

    def __init__(self,filename,cdnumber):
        self.filename=filename
        self.cdnumber=cdnumber
        self.date=''
        self.nowtime=''


    def getsheets(self):
        fileopen=xlrd.open_workbook(self.filename)  #读取文件
        sheetnumber=len(fileopen.sheets())    #获取页签数
        self.nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#当前时间为字符串格式
        self.date=datetime.datetime.now().strftime('%y%m%d')
        print(sheetnumber)
        return sheetnumber

    def getcell(self):
        fileopen=xlrd.open_workbook(self.filename)   #读取文件    
        writefile=copy(fileopen)  #写入文件打开
        currentsheet=self.getsheets()     #获取文件页签数
        inttype=['int','integer','number','long','tinyint','smalint','short']
        floattype=['float','double']
        nntime=datetime.datetime.strptime(self.nowtime,'%Y-%m-%d %H:%M:%S')  #转换当前时间为datetime，转换后才可加减运算
        timestyle = xlwt.XFStyle()   #格式初始化
        timestyle.num_format_str ='YYYY-MM-DD HH:MM:SS'  #设置timestamp格式
        
        for sheetcn in range(0,currentsheet):
            readcurrsheet=fileopen.sheet_by_index(sheetcn)  #读取当前页签
            writesheet=writefile.get_sheet(sheetcn)   #指定当前写入页签序列
            cellnumber=readcurrsheet.ncols  #读取文件时才可以获取当前sheet页列数
            for colindex in range(0,cellnumber):
                for values in range(2,self.cdnumber):
#                    if readcurrsheet.cell(1,colindex).value in ('varchar','varchar2','string','char','text','nvarchar','nchar'):
                    if   readcurrsheet.cell(1,colindex).value =='timestamp':
                        writesheet.write(values,colindex,nntime+datetime.timedelta(seconds=values),timestyle)  #时间以秒单位增加，每次增加量为values
                    elif readcurrsheet.cell(1,colindex).value in inttype:    #判断字段类型
                        writesheet.write(values,colindex,values)
                    elif readcurrsheet.cell(1,colindex).value in floattype:
                        writesheet.write(values,colindex,0.02+values)
                    elif readcurrsheet.cell(1,colindex).value =='date':
                        writesheet.write(values,colindex,self.date)
                    else:    
                        writesheet.write(values,colindex,'ABC00gfdkgkfjfgdf01024121'+str(values))
            writefile.save(self.filename)


if __name__=='__main__':

    newcddata=cddata('D:\\dedeskstop\\xxxx.xls',10)
    newcddata.getcell()
    print("ok") 