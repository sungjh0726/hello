# 검색결과 : getDanjiComboAjax.do 
# #APT_CODE: 20332148
# APT_NAME: "670-7"
# BUN1: "0670"
# BUN2: "0007"
# EUB: "10300"
# JIBUN_NAME: "서울특별시 노원구  공릉동"
# REG: "11350"
# ROAD_BUILDBUN1: "00443"
# ROAD_BUILDBUN2: "00000"
# ROAD_NAME: "화랑로"


# #menuGubun: A
# srhLastYear: 2018
# sidoCode: 11
# gugunCode: 11350
# dongCode: 1135010300
# rentAmtType: 3

# 맨처음에 동코드
# 그다음에 아파트코드
# json을 가지고 와서 최종정보르 갖고 있느 파일 저장

from bs4 import BeautifulSoup
import requests
import json
import time

url = "http://rt.molit.go.kr/new/gis/getDongListAjax.do" #POST

params = {
    'menuGubun': 'A' ,
    'gubunCode': 'LAND',
    'sidoCode': '11',
    'gugunCode': '11350'
}

headers = {
   'Referer': 'http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

html = requests.post(url, params=params, headers=headers).text
# print(html)
jsonData = json.loads(html)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))
dongCode = {}

for gu in jsonData["jsonList"]:
    # print(gu['NAME'], gu['CODE'])
    dongCode[gu['NAME']] = gu['CODE']
# print(">>>>>>>>>>>>>>>>>", dongCode)


############################## 동코드 완료.

url = "http://rt.molit.go.kr/new/gis/getDanjiComboAjax.do" #POST

params = {
    'menuGubun': 'A', 
    'srhYear': '2019',
    'srhLastYear': '2018',
    'gubunCode': 'LAND',
    'sidoCode': '11',
    'gugunCode': '11350',
    'dongCode': '1135010300',
    'rentAmtType': '3'
}

headers = {
  'Referer': 'http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

html = requests.post(url, params=params, headers=headers).text
# print(html)
jsonData = json.loads(html)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))
APT_CODE = {}

for APT in jsonData["jsonList"]:
    # print(APT['APT_NAME'], APT['APT_CODE'])
    APT_CODE[APT['APT_NAME']] = APT['APT_CODE']
# print(">>>>>>>>>>>>>>>>>", APT_CODE)
# print(APT_CODE)


############################# 아파트코드 완료

url = "http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun=A&p_apt_code=20332148&p_house_cd=1&p_acc_year=2018&areaCode=&priceCode=" 
#GET

headers = {
  'Referer': 'http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

for i, j in enumerate(APT_CODE):
    params = {
        'menuGubun': 'A',
        'p_apt_code': "'"+str(APT_CODE[j])+"'",
        'p_house_cd': '1',
        'p_acc_year': '2018'
    }
    # print(params)
    html = requests.get(url, params=params, headers=headers).text
    # print(html)
    jsonData = json.loads(html)
    # print(json.dumps(jsonData, ensure_ascii=False, indent=2))

    APT_FINAL_INFOS = []
    # print(jsonData)
    # exit()
    for APT_FINAL_INFO in jsonData["result"]:
        print(APT_FINAL_INFO)
        FINAL = {APT_FINAL_INFO["BLDG_CD"] : 
            {
                "DNAME"   : APT_FINAL_INFO["DNAME"],
                # "BLDG_NM": APT_FINAL_INFO["BLDG_NM"],
                # "BOBN": APT_FINAL_INFO["BOBN"],
                # "BLDG_AREA": APT_FINAL_INFO["BLDG_AREA"],
                # "DEAL_MM": APT_FINAL_INFO["DEAL_MM"],
                # "DEAL_DD": APT_FINAL_INFO["DEAL_DD"],
                # "SUM_AMT": APT_FINAL_INFO["SUM_AMT"],
                # "APTFNO": APT_FINAL_INFO["APTFNO"],
                # "BUILD_YEAR": APT_FINAL_INFO["BUILD_YEAR"],
                # "ROAD_LEN": APT_FINAL_INFO["ROAD_LEN"],
                # "BC_RAT": APT_FINAL_INFO["BC_RAT"],
                # "VL_RAT": APT_FINAL_INFO["VL_RAT"]
            }
        }
        # time.sleep(6)
print(FINAL)    

with open("./web/realstate_goreng.html", mode="w") as file:
    file.write(html)
    
# BLDG_CD: 20332148
# DNAME: "공릉동"
# BLDG_NM: "670-7"
# BOBN: "670-7"
# BLDG_AREA: 17.27
# DEAL_MM: "10"
# DEAL_DD: "11~20"
# SUM_AMT: "17,400"
# APTFNO: 12
# BUILD_YEAR: 2016
# ROAD_LEN: "25m이상"
# BC_RAT: "56~60%"
# VL_RAT: "626~630%"


# HO_CODE: 53
# LAND_USE_LAW: "[포함]학교환경위생정화구역<학교보건법>(공릉초. 최종확인은 관할교육청에 반드시 문의),[포함]학교환경위생정화구역<학교보건법>(최종확인은관할교육청에반드시확인),[포함]대공방어협조구역<군사기지 및 군사시설보호법>(위탁고도:77-257m),[포함]가축사육제한구역<가축분뇨의관리및이용에관한법률>,[포함]한강폐기물매립시설설치제한지역<한강수계상수원수질개선및주민지원등에관한법률>(자세한사항은 자원순환과로 문의),[포함]과밀억제권역<수도권정비계획법>"
# LAND_USE_NM: "[포함]도시지역,[포함]일반상업지역,[포함]제1종지구단위계획구역,[접합]제3종일반주거지역,[접합]도로"
# BLDG_CD: 20332148
# DONG_CODE: 1
# ETC_STRCT: "철근콘크리트구조"
# GRND_FLR_CNT: "-"
# JIBUN_NAME: "서울특별시 노원구  공릉동"
# LAND_MOVE1: "198*"
# LAND_MOVE2: "행정관할구역변경"




# ##### 최종정보