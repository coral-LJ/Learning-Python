# -*- coding:utf-8 -*-
import vars

def ins_api(apiname,dataStr='{}'):
    try:
        incidentEntity1 = vars.INS_VALUE[apiname]
        headers = vars.INS_HEADER["header"]


    except KeyError:
        print("不存在的api名，请重新输入")

    if dataStr == '':
        dataStr = '{}'

    dataNew = eval(dataStr)
    incidentEntityCopy = incidentEntity1.copy()
    incidentEntityCopy.update(dataNew)  # 这句是关键,把数据update到模板取到的data中去
    return [apiname,incidentEntityCopy,headers]

# test=ins_api('incidentEntity',dataStr='{}')
