import streamlit as st
import requests

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' 
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items):
    optionlist=[]
    for item in items:
        name=item["cityName"][0:3]
        if name not in optionlist:
            optionlist.append(name)
    return optionlist

def getSpecificBookstorelist(items,county):
    specificBookstorelist=[]
    for item in items:
        name=item["cityName"]
        if county in name:
            if name[-3:-1] not in  specificBookstorelist:
                 specificBookstorelist.append(name[-3:-1])
        else:
            continue
    return specificBookstorelist


def app():
    bookstorelist=getAllBookstore()
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstorelist))
    county = st.selectbox('請選擇縣市', getCountyOption(bookstorelist))
    district = st.multiselect('請選擇區域', getSpecificBookstorelist(bookstorelist,county))

if __name__ == '__main__':
    app()
    