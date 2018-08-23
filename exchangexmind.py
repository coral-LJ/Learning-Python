# coding:utf-8
import  xlrd,os
import string,random,re

def getpath(filename1):
        path =os.path.split(filename1)
        return path

def key_gen(KEY_LEN):       #生成随机字符串+数字类型(generate random string and number)
    keylist = [random.choice(string.ascii_letters+string.digits) for i in range(KEY_LEN)]
    return ("".join(keylist))

# def key_int(int_len):  #生成随机数字类型(generate random  number)
#     value=[random.choice(string.digits) for i in range(int_len)]
#     return ("".join(value))

def excelchange(filename1,sheetname):		#传入文件名及excel中需要被读取的页签名称(the filename and lable in file)
    filename=xlrd.open_workbook(filename1)
    sheet=filename.sheet_by_name(sheetname)
    nrow=sheet.nrows
	numlen=''

    newpath=getpath(filename1)
    xmlfilename=open(newpath[0]+'\ecmind.doc','w+',encoding='utf-8')
    xmlfilename.write('<html>\n<head>\n<META http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<meta content="text/html; charset=utf-8" http-equiv="Content-Type">\n<meta content="text/css" http-equiv="Content-Style-Type">\n')
    title=sheet.cell(1,0).value
    xmlfilename.write('<title>'+title+'</title>\n</head>\n<body>\n<h1 align="center" class="root">\n')
    name=key_gen(26)
    xmlfilename.write('<a name="'+name+'">'+title+'</a>\n</h1>\n')  #h1标签的内容(h1 content)

    for rondows in range(2,nrow):
        if sheet.cell(rondows,1).value!='':         #判断第二列是否为空，为空则是标题行(if the second cloumn is null,the row is only title)
            # nodeID1 = key_gen(26)
            text1=sheet.cell(rondows,2).value       #获取用例名称列(get test case name)
            # xmlfilename.write('<h'+str(numlen+1) +' class="topic">\n<a name="'+nodeID1+'">'+text1+'</a>\n</h2>\n')
            nodeID2 = key_gen(26)
            text2=sheet.cell(rondows,6).value       #获取用例预期结果列(get test expected result)
                        xmlfilename.write('<h'+str(numlen+1) +' class="topic">\n<a name="'+nodeID2+'">'+text1+'\n预期结果：'+text2+'</a>\n'+'</h'+str(numlen+1)+'>\n')      
			#插入用例内容中用例标题及用例预期结果(file adds get test case name and test expected result of the row,Using tag h)
            # xmlfilename.write('<h' + str(numlen + 1) + ' class="topic">\n<a name="' + nodeID2 + '">' + text1 + '<font style="font-weight:bold";size="1";>'+text2 +'</font>'+ '</a>\n</h3>\n')
        else:
            nodeID3 = key_gen(26)
            text3=sheet.cell(rondows,0).value       #获取标题名称(get title)
            numlen=len(re.sub("\D", "", text3))     #通过标题中数字位数判断标题层级(Determining the title level by the length of digits in the title)
            xmlfilename.write('<h'+str(numlen) +' class="topic">\n<a name="'+nodeID3+'">'+text3+'</a>\n'+'</h'+str(numlen)+'>\n')   #写入标题行(file add title)
    xmlfilename.write('</body>\n</html>')
    xmlfilename.close()


	
resul=excelchange('D:\xx测试用例.xlsx','测试用例')

#思路：Xmind中创建图形，以word格式导出doc文件，导出使用文档编辑工具打开，查看每个层级之间的关系，以及html脚本的结构
#熟悉html结构后，使用pycharm编辑代码，生成相应的doc文件，导入Xmind
