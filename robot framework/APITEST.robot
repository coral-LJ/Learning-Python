*** Settings ***
Library  requests
Library  RequestsLibrary
Library  Collections
Library  common.py
Variables  vars.py


*** Variables ***
${url}      http://127.0.0.1:0000

*** Keywords ***
incidentEntity
    ${Pyreturn}     insight_api    incidentEntity.do      dataStr={}
    log         ${Pyreturn}
    create session    api    ${url}     headers=${Pyreturn[2]}
    ${addr}    post request   api  /PAS/inc/incidentEntity.do    data=${Pyreturn[1]}
    log    ${addr.status_code}
    should be equal as strings  ${addr.status_code}         200
    ${conjson}      to json  ${addr.content}
    ${data}     get from dictionary  ${conjson}  data
    should not be empty  ${data}

findGISData
    ${Pyreturn}     insight_api    findGISData      dataStr={}
    log         ${Pyreturn}
    ${return1}=     create list       ${Pyreturn[1]}    #将dic转化为list，变量形式不会自动加引号
    create session    api    ${url}     ${Pyreturn[2]}
    ${addr}=    post request   api  /PAS/gis/findGISData    data=${return1}    headers=${Pyreturn[2]}
    log    ${addr.status_code}
    should be equal as strings  ${addr.status_code}         200
    ${conjson}      to json  ${addr.content}
    ${incidents}     get from dictionary  ${conjson}  incidents     #json结果中取出key=incidents所对应的value
    ${incidents0}     evaluate  [incidents0['totalityNum'] for incidents0 in ${conjson['incidents']}]  #获取json串中某一key的值（数组类型）中的某一个key的值
    ${sum}  evaluate    sum(${incidents0})
    should not be empty  ${incidents}
    should be equal as integers  ${sum}     10106

prelist
    ${Pyreturn}     insight_api    prelist      dataStr={}
    log         ${Pyreturn}
    create session    api    ${url}     ${Pyreturn[2]}
    ${response}=    post request   api  /PAS/pre/list   data=${Pyreturn[1]}  headers=${Pyreturn[2]}
    log    ${response.status_code}
    should be equal as strings  ${response.status_code}         200
    ${conjson}      to json  ${response.content}
    ${incPreData0}       evaluate  [incPreData0['ipNum'] for incPreData0 in ${conjson['data']['data']['incPreData']}]
    should not be empty  ${incPreData0}

incHours
    ${Pyreturn}     insight_api    incHours      dataStr={}
    log         ${Pyreturn}
    create session    api    ${url}      ${Pyreturn[2]}
    ${response}=    post request   api  /PAS/inc/incHours   data=${Pyreturn[1]}  headers=${Pyreturn[2]}
    log    ${response.status_code}
    should be equal as strings  ${response.status_code}         200
    ${conjson}      to json  ${response.content}
    ${data}       get from dictionary   ${conjson}  data
    should not be empty   ${data}

*** Test Cases ***
case1
    incidentEntity

case2
    findGISData

case3
    prelist

case4
    incHours
