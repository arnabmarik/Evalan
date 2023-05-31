# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:10:24 2022
"""

#%% Imports and global variables
import http.client
import json
import pkce
import requests as rq
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from collections.abc import Iterable
from random import *
from datetime import datetime, timedelta

#%% Variables MEDRECORD
CLIENT_ID_MR = "f04a0416-c4dc-4076-871e-f5f9a7d17a85"
EMAIL_MR="sofia.perezsimbor@evalan.com"
PASSWORD_MR="p2VnMvYqMyS6cdC!"
REDIRECT_URI_MR="https://foodfriend-coach.medvision360.org"
state = "engineer"


#%% Variables BACE
endpoint_BACE="https://dashboard.bace-iot.com/"
CLIENT_ID_BACE = "mqHEPzzN6uzi8KdvoW1zDuKezHbFsNT3"
CLIENT_SECRET_BACE = "acgeZkW4qaYZFXcAkRoS1n8dbo446GI4"
EMAIL_BACE = "sofia_test@evalan.com"
PASSWORD_BACE = "Sodium"
REDIRECT_URI_BACE = "https://foodfriend.evalan.com"



#%% Definitions

def signin_password(code_challenge=None):
    conn = http.client.HTTPSConnection("foodfriend-auth.medvision360.org")
    payload = json.dumps({
        "client_id": CLIENT_ID_MR,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "email": EMAIL_MR,
        "password": PASSWORD_MR,
        "redirect_uri": REDIRECT_URI_MR,
        "response_type": "CODE",
        "state": state
        })
    headers = {
        'Content-Type': 'application/json'
        }
    conn.request("POST", "/signin/password", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data2 = json.loads(data)
    # print(data2)
    return data2

def oauth_token (Code=None, code_verifier=None):

    conn = http.client.HTTPSConnection("foodfriend-auth.medvision360.org")
    payload = json.dumps({
        "client_id": CLIENT_ID_MR,
        "code": Code,
        "code_verifier": code_verifier,
        "grant_type": "AUTHORIZATION_CODE",
        "redirect_uri": REDIRECT_URI_MR
        })
    headers = {
        'Content-Type': 'application/json'
        }
    conn.request("POST", "/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data2 = json.loads(data)
    # print(data2)
    return data2

def refreshing_token (Code =None, code_verifier=None,refresh_token=None, access_token=None):
    conn = http.client.HTTPSConnection("foodfriend-auth.medvision360.org")
    payload =f"client_id={CLIENT_ID_MR}&code={Code}&code_verifier={code_verifier}&grant_type=refresh_token&redirect_uri={REDIRECT_URI_MR}&refresh_token={refresh_token}"
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    conn.request("POST", "/oauth/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data2 = json.loads(data)
    # print(data.decode("utf-8"))
    return data2['access_token']

def create_oauth_link():
    params = {
        "client_id": CLIENT_ID_BACE,
        "redirect_uri":CLIENT_SECRET_BACE,
        "scope": "user",
        "grant_type":"password",
        }
    ep=f"{endpoint_BACE}/oauth2/token"
    response=rq.get(ep, data=params)
    url=response.url
    return url

def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID_BACE,
        "client_secret": CLIENT_SECRET_BACE,
        "redirect_uri": REDIRECT_URI_BACE,
        "grant_type":'password',
        "username": EMAIL_BACE,
        "password": PASSWORD_BACE,
    }
    headers = {"Accept": "application/json"}
    ep = f"{endpoint_BACE}/oauth2/token"
    response = rq.post(ep, data=params, headers=headers).json()
    return response["access_token"]


def adding_HR (userId=None,comment=None,rate=None,access_token=None, date=None):
    conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
    payload = json.dumps({
        "comment": comment,
        "effective": {
            "date": date,
            "precision": "SECOND"
            },
        "rate": rate,
        "regularity": "REGULAR"
        })
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
        }
    conn.request("POST", f"/patient/{userId}/observation/pulseRate", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))

def adding_RR (userId=None, comment=None, rate=None, access_token=None, date=None):
    conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
    payload = json.dumps({
      "comment": comment,
      "effective": {
        "date": date,
        "precision": "SECOND"
      },
      "rate": rate
    })
    headers = {
      'Authorization': f'Bearer {access_token}',
      'Content-Type': 'application/json'
    }
    conn.request("POST", f"/patient/{userId}/observation/respiratoryRate", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("This is the payload", payload)
    # print(data.decode("utf-8"))

def adding_Spo2 (userId=None, comment=None, rate=None, access_token=None, date=None):
    conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
    payload = json.dumps({
        "comment": comment,
        "effective": {
            "date": date,
            "precision": "SECOND"
            },
        "saturation": rate
        })
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
        }
    conn.request("POST", f"/patient/{userId}/observation/oxygenSaturation", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))


def adding_BodyWeight (userId=None, comment=None, rate=None, access_token=None, date=None):
    conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org")
    payload = json.dumps({
        "clothing": "FULL",
        "comment": comment,
        "effective": {
            "date": date,
            "precision": "DAY"
            },
        "weight": rate
        })
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
        }
    conn.request("POST", f"/patient/{userId}/observation/bodyWeight", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))

def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:
             yield item


#%% Printing Letters

print("||||||||| ||||||||| ||||||||| |||||||\\\ ||||||||| |||||||\\\ |||||||  |||||||||  |||\\\    ||| ||||||||\\")
print("|||       |||   ||| |||   ||| |||   ||| |||       |||   |||   |||    |||        ||| \\\   ||| |||    |||")
print("|||||     |||   ||| |||   ||| |||   ||| |||||     |||||||||   |||    ||||||     |||  \\\  ||| |||    |||")
print("|||       |||   ||| |||   ||| |||   ||| |||       |||  \\\     |||    |||        |||   \\\ ||| |||    |||")
print("|||       ||||||||| ||||||||| ||||||//  |||       |||   \\\  |||||||  |||||||||  |||    \\\||| |||||||//    ")
#%% Authentication MEDRECORD
print("Authenticating in MedRecord")
code_verifier, code_challenge = pkce.generate_pkce_pair()
signin=signin_password(code_challenge=code_challenge)

redirect_uri_after_signin=signin['redirectUri']
find_code=redirect_uri_after_signin.find("code")
find_state=redirect_uri_after_signin.find("&state")
Code=redirect_uri_after_signin[(find_code+5):find_state]

oauth= oauth_token (Code=Code, code_verifier=code_verifier)
access_token_MR=oauth['access_token']
refresh_token=oauth['refresh_token']
print("Authentication in MedRecord successful")

#%% REFRESH TOKEN #%%
access_token_MR=refreshing_token(Code =Code, code_verifier=code_verifier,refresh_token=refresh_token, access_token=access_token_MR)
print("This is the access token", access_token_MR)
#%% Is token Valid?


conn = http.client.HTTPSConnection("foodfriend-auth.medvision360.org")
payload = ''
headers = {
  'Authorization': f'Bearer {access_token_MR}'
}
conn.request("GET", "/token/validate", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#%% WhoamI MEdrecord

conn = http.client.HTTPSConnection("foodfriend-auth.medvision360.org")
payload = ''
headers = {
  'Authorization': f'Bearer {access_token_MR}'
}
conn.request("GET", "/token/whoami", payload, headers)
res = conn.getresponse()
data = res.read()
data2 = json.loads(data)
print(data.decode("utf-8"))
userId_MR=data2['id']

#%% Authentication BACE
print("Starting Authentication with BACE")
link = create_oauth_link()
# print(f"Follow the link to start the authentication with Evalan: {link}")
access_token_BACE = exchange_code_for_access_token()
# print(f"access token: {access_token_BACE}")
#This gives information about the current user
ep_me = f"{endpoint_BACE}/api/v2/user/self"
headers = {"Authorization": f"Bearer {access_token_BACE}","Accept": "application/json" }
rp_me = rq.get(ep_me, headers=headers).json()
userId_BACE=rp_me['user']['id_user']

print("Authentication in BACE successful")

#%% Getting the data from BACE Cloud
print("Getting data from BACE backend")
ep_physical_device=f"{endpoint_BACE}/api/v2/physical-device?filter[id_device_type]=bace-go"
headers = {"Authorization": f"Bearer {access_token_BACE}","Accept": "application/json"}
print(headers)
rp_physical_device= rq.get(ep_physical_device, headers=headers).json()
ep_groups=f"{endpoint_BACE}/api/v2/group?filter[label]=BaceGo-001-002-00020&expand=latestSession"
rp_groups=rq.get(ep_groups, headers=headers).json()
From_timestamp = str(rp_groups['items'][0]['latestSession']['start'])
id_group_=rp_groups['items'][0]['id']
print("print_id_group", id_group_)

# ep_data_downsampled_spo2=f"{endpoint_BACE}/api/v2/data-downsampled?filter[id_group]={id_group_}&filter[timestamp_seconds][gt]={From_timestamp}&filter[datatype]=6002"
# rp_data_downsampled_spo2= rq.get(ep_data_downsampled_spo2, headers=headers).json()
# rp_data_downsampled_spo2 = sorted(rp_data_downsampled_spo2['items'], key=lambda k: k.get('timestamp_seconds', 0), reverse=True)


# ep_data_downsampled_rr=f"{endpoint_BACE}/api/v2/data-downsampled?filter[id_group]={id_group_}&filter[timestamp_seconds][gt]={From_timestamp}&filter[datatype]=6001"
# rp_data_downsampled_rr= rq.get(ep_data_downsampled_rr, headers=headers).json()
#
# ep_data_raw_bw=f"{endpoint_BACE}/api/v2/data-downsampled/index?filter[id_group]={id_group_}&filter[timestamp_seconds][gt]={From_timestamp}&filter[datatype]=6011"
# rp_data_raw_bw= rq.get(ep_data_raw_bw, headers=headers).json()


# SpO2_downsampled = [rp_data_downsampled_spo2['items'][i]['avg_val']for i in range (rp_data_downsampled_spo2['_meta']['totalCount'])]
# Time_SpO2=[rp_data_downsampled_spo2['items'][i]['timestamp_seconds']for i in range (rp_data_downsampled_spo2['_meta']['totalCount'])]
#
# rr_downsampled = [rp_data_downsampled_rr['items'][i]['avg_val']for i in range (rp_data_downsampled_rr['_meta']['totalCount'])]
# Time_rr=[rp_data_downsampled_rr['items'][i]['timestamp_seconds']for i in range (rp_data_downsampled_rr['_meta']['totalCount'])]
#
# weight_downsampled = [rp_data_raw_bw['items'][i]['avg_val']for i in range (rp_data_raw_bw['_meta']['totalCount'])]
# Time_weight=[rp_data_raw_bw['items'][i]['timestamp_seconds']for i in range (rp_data_raw_bw['_meta']['totalCount'])]





sensor_id= {"oxygenSaturation": "6002", "pulseRate":"6000"}
function_list = {"oxygenSaturation": adding_Spo2, "pulseRate": adding_HR}

for key, value in sensor_id.items():
    # fetch data from medrecords and upload new value if applicable

    rp_data_downsampled_ = sorted(rq.get(f"{endpoint_BACE}/api/v2/data-downsampled?filter[id_group]={id_group_}&filter[timestamp_seconds][gt]={From_timestamp}&filter[datatype]=" + value, headers=headers).json()['items'], key=lambda k: k.get('timestamp_seconds', 0), reverse=True)

    # ep_data_downsampled_=f"{endpoint_BACE}/api/v2/data-downsampled?filter[id_group]={id_group_}&filter[timestamp_seconds][gt]={From_timestamp}&filter[datatype]=" + value
    # rp_data_downsampled_= rq.get(ep_data_downsampled_, headers=headers).json()
    # print(rp_data_downsampled_)
    # rp_data_downsampled_ = sorted(rp_data_downsampled_['items'], key=lambda k: k.get('timestamp_seconds', 0), reverse=True)

    if rp_data_downsampled_ !=[]:
        conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
        payload = ''
        headers2= {
          'Authorization': f'Bearer {access_token_MR}',
          'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request("GET", f"/patient/{userId_MR}/observation/" + key + "?count=5&start=0", payload, headers2)
        data=json.loads(conn.getresponse().read())
        latest_time = data[0]['effective']['date']
        from_BACE = datetime.isoformat(datetime.fromtimestamp(rp_data_downsampled_[0]['timestamp_seconds']))[0:-3]
        from_Med  = datetime.isoformat(datetime.fromisoformat(latest_time) + timedelta(hours = 2))[0:-9]

        if from_BACE != from_Med:
            print("New value found, uploading to Medrecords")
            dt_obj = datetime.fromtimestamp(rp_data_downsampled_[0]['timestamp_seconds'])
            dt = datetime.isoformat(dt_obj)
            dt = datetime.fromisoformat(dt)
            # Add two hours to the datetime object
            dt += timedelta(hours=-2)
            date=datetime.isoformat(dt)
            print(date)
            Comment=f"Mesurement performed with BACE Go ID 20"
            function_list[key](userId=userId_MR,comment=Comment, rate=rp_data_downsampled_[0]['avg_val'],access_token=access_token_MR, date=date)
            print("Uploaded  values into MEDrecord platform")
        else:
            print("No new value of HR found")

    else:
        print("HR sensor is not turned ON")



# # fetch Spo2 data from medrecords and upload new value if applicable
# rp_data_downsampled_hr = sorted(rq.get(f"{endpoint_BACE}/api/v2/data-downsampled?filter[id_group]={id_group_}&filter[timestamp_seconds][gt]={From_timestamp}&filter[datatype]=6000", headers=headers).json()['items'], key=lambda k: k.get('timestamp_seconds', 0), reverse=True)
#
# conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
# payload = ''
# headers = {
#   'Authorization': f'Bearer {access_token_MR}',
#   'Content-Type': 'application/x-www-form-urlencoded'
# }
# conn.request("GET", f"/patient/{userId_MR}/observation/pulseRate?count=20&start=0", payload, headers)
# data=json.loads(conn.getresponse().read())
# latest_time = data[0]['effective']['date']
# from_BACE = datetime.isoformat(datetime.fromtimestamp(rp_data_downsampled_hr[0]['timestamp_seconds']))[0:-3]
# from_Med  = datetime.isoformat(datetime.fromisoformat(latest_time) + timedelta(hours = 2))[0:-9]
#
# if from_BACE != from_Med:
#     print("New value found, uploading to Medrecords")
#     dt_obj = datetime.fromtimestamp(rp_data_downsampled_hr[0]['timestamp_seconds'])
#     dt = datetime.isoformat(dt_obj)
#     dt = datetime.fromisoformat(dt)
#     # Add two hours to the datetime object
#     dt += timedelta(hours=-2)
#     date=datetime.isoformat(dt)
#     print(date)
#     Comment_HR=f"Mesurement performed with BACE Go ID 20"
#     adding_HR (userId=userId_MR,comment=Comment_HR, rate=rp_data_downsampled_hr[0]['avg_val'],access_token=access_token_MR, date=date)
#     print("Uploaded HR values into MEDrecord platform")
# else:
#     print("No new value of HR found")





# #%% Reading HR
#
# conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
# payload = ''
# headers = {
#   'Authorization': f'Bearer {access_token_MR}',
#   'Content-Type': 'application/x-www-form-urlencoded'
# }
# conn.request("GET", f"/patient/{userId_MR}/observation/heartRate/count", payload, headers)
# res=conn.getresponse()
# data= res.read()
# data=json.loads(data)
# count=data['count']
#
# HR_list=[]
# if count <= 50:
#
#     conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
#     conn.request("GET", f"/patient/{userId_MR}/observation/heartRate?count=50&start=0", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     HR_list = json.loads(data)
#     print(data.decode("utf-8"))
# else:
#     module=np.ceil(count/50)
#     module=int(module)
#     for i in range (module):
#         conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
#         conn.request("GET", f"/patient/{userId_MR}/observation/heartRate?count=100&start={i*50}", payload, headers)
#         res = conn.getresponse()
#         data = res.read()
#         data_2=json.loads(data)
#         HR_list.append(data_2)
#         # print(data.decode("utf-8"))
#
# print("Uploaded HR")
#
# #%% Adding Respiration Rate
#
# for i in range(len(Time_rr)):
#     dt_obj = datetime.fromtimestamp(Time_rr[i])
#     date=datetime.isoformat(dt_obj)
#     Comment_rr=f"Mesurement performed with BACE Go ID 20"
#     adding_RR (userId=userId_MR,comment=Comment_rr, rate=rr_downsampled[i],access_token=access_token_MR, date=date)
#
# print("Uploading RR values into MEDrecord platform")
#
# #%% Reading rr
#
# conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
# payload = ''
# headers = {
#   'Authorization': f'Bearer {access_token_MR}',
#   'Content-Type': 'application/x-www-form-urlencoded'
# }
# conn.request("GET", f"/patient/{userId_MR}/observation/respiratoryRate/count", payload, headers)
# res=conn.getresponse()
# data= res.read()
# data=json.loads(data)
# count=data['count']
#
# rr_list=[]
# if count <= 50:
#
#     conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
#     conn.request("GET", f"/patient/{userId_MR}/observation/respiratoryRate?count=50&start=0", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     rr_list = json.loads(data)
#     print(data.decode("utf-8"))
# else:
#     module=np.ceil(count/50)
#     module=int(module)
#     for i in range (module):
#         conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
#         conn.request("GET", f"/patient/{userId_MR}/observation/respiratoryRate?count=100&start={i*50}", payload, headers)
#         res = conn.getresponse()
#         data = res.read()
#         data_2=json.loads(data)
#         rr_list.append(data_2)
#         # print(data.decode("utf-8"))
#
# print("Uploaded RR")
#
#
# #%% Adding Oxygen saturation
#
# for i in range (len(Time_SpO2)):
#     dt_obj = datetime.fromtimestamp(Time_SpO2[i])
#     date=datetime.isoformat(dt_obj)
#     Comment_Spo2=f"Mesurement performed with BACE Go ID 20"
#     adding_Spo2 (userId=userId_MR,comment=Comment_Spo2, rate=SpO2_downsampled[i],access_token=access_token_MR, date=date)
#
# print("Uploading SpO2 values into MEDrecord platform")
#
#
# #%% Reading SpO2
# conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
# payload = ''
# headers = {
#   'Authorization': f'Bearer {access_token_MR}',
#   'Content-Type': 'application/x-www-form-urlencoded'
# }
# conn.request("GET", f"/patient/{userId_MR}/observation/oxygenSaturation/count", payload, headers)
# res=conn.getresponse()
# data= res.read()
# data=json.loads(data)
# count=data['count']
#
# spo2_list=[]
# if count <= 50:
#
#     conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
#     conn.request("GET", f"/patient/{userId_MR}/observation/oxygenSaturation?count=50&start=0", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     spo2_list = json.loads(data)
#     print(data.decode("utf-8"))
# else:
#     module=np.ceil(count/50)
#     module=int(module)
#     for i in range (module):
#         conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
#         conn.request("GET", f"/patient/{userId_MR}/observation/oxygenSaturation?count=100&start={i*50}", payload, headers)
#         res = conn.getresponse()
#         data = res.read()
#         data_2=json.loads(data)
#         spo2_list.append(data_2)
#         # print(data.decode("utf-8"))
#
# print("Uploaded SpO2")
#
#
#
#
# #%%Adding Body Weight
#
# for i in range (len(Time_weight)):
#     dt_obj = datetime.fromtimestamp(Time_weight[i])
#     date=datetime.isoformat(dt_obj)
#     Comment_Weight=f"Mesurement performed with BACE Go ID 20"
#     adding_BodyWeight (userId=userId_MR,comment=Comment_Weight, rate=weight_downsampled[i],access_token=access_token_MR, date=date)
#
# print("Uploading Body Weight values into MEDrecord platform")
#
#
# #%%Reading Body Weight
#
#
# conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
# payload = ''
# headers = {
#   'Authorization': f'Bearer {access_token_MR}',
#   'Content-Type': 'application/x-www-form-urlencoded'
# }
# conn.request("GET", f"/patient/{userId_MR}/observation/bodyWeight/count", payload, headers)
# res=conn.getresponse()
# data= res.read()
# data=json.loads(data)
# count=data['count']
#
# weight_list=[]
# if count <= 50:
#
#     conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
#     conn.request("GET", f"/patient/{userId_MR}/observation/bodyWeight?count=50&start=0", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     weight_list = json.loads(data)
#     # print(data.decode("utf-8"))
# else:
#     module=np.ceil(count/50)
#     module=int(module)
#     for i in range (module):
#         conn = http.client.HTTPSConnection("foodfriend-backend.medvision360.org​")
#         conn.request("GET", f"/patient/{userId_MR}/observation/oxygenSaturation?count=100&start={i*50}", payload, headers)
#         res = conn.getresponse()
#         data = res.read()
#         data_2=json.loads(data)
#         weight_list.append(data_2)
#         # print(data.decode("utf-8"))
#
# print("Uploaded Body Weight")
#
#
# #%% Printing Nice table
# table_hr=[]
# print("Reading the Data from MEDRecord backend")
#
# print("")
# print("")
#
# print("Printing HR")
#
# for i in range (len(HR_list)):
#     for j in range (len(HR_list[i])):
#         value=HR_list[i][j]
#         del value["context"]
#         del value["device"]
#         del value["interpretation"]
#         del value["method"]
#         del value["nhgCode"]
#         del value["referenceRanges"]
#         del value["performer"]
#         del value["rate"]["system"]
#         del value["effective"]["precision"]
#         del value["rate"]["code"]
#         del value["references"]
#         del value["comment"]
#         del value["regularity"]
#         del value["subject"]["identifier"]
#         table_hr.append(value)
#
# header = table_hr[0].keys()
# rows=[x.values() for x in table_hr]
# print (tabulate(rows,header))
# print("")
# print("")
# print("Printing RR")
#
# table_rr=[]
# for i in range (len(rr_list)):
#     for j in range (len(rr_list[i])):
#         value=rr_list[i][j]
#         del value["context"]
#         del value["device"]
#         del value["interpretation"]
#         del value["nhgCode"]
#         del value["referenceRanges"]
#         del value["performer"]
#         del value["rate"]["system"]
#         del value["effective"]["precision"]
#         del value["rate"]["code"]
#         del value["references"]
#         del value["comment"]
#         del value["subject"]["identifier"]
#         table_rr.append(value)
#
# header = table_rr[0].keys()
# rows=[x.values() for x in table_rr]
# print (tabulate(rows,header))
# print("")
# print("")
# print("Printing SpO2")
#
# table_SpO2=[]
# for i in range (len(spo2_list)):
#     for j in range (len(spo2_list[i])):
#         value=spo2_list[i][j]
#         del value["context"]
#         del value["device"]
#         del value["interpretation"]
#         del value["nhgCode"]
#         del value["referenceRanges"]
#         del value["performer"]
#         del value["saturation"]["system"]
#         del value["effective"]["precision"]
#         del value["saturation"]["code"]
#         del value["references"]
#         del value["comment"]
#         del value["subject"]["identifier"]
#         del value["extraOxygen"]
#         table_SpO2.append(value)
#
# header = table_SpO2[0].keys()
# rows=[x.values() for x in table_SpO2]
# print (tabulate(rows,header))
# print("")
# print("")
# ("Printing Body Weight")
#
#
# table_weight=[]
# for i in range (len(weight_list)):
#         value=weight_list[i]
#         del value["context"]
#         del value["device"]
#         del value["interpretation"]
#         del value["nhgCode"]
#         del value["referenceRanges"]
#         del value["performer"]
#         del value["weight"]["system"]
#         del value["effective"]["precision"]
#         del value["weight"]["code"]
#         del value["references"]
#         del value["comment"]
#         del value["subject"]["identifier"]
#         table_weight.append(value)
#
# header = table_weight[0].keys()
# rows=[x.values() for x in table_weight]
# print (tabulate(rows,header))

