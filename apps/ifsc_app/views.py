import requests
import json
from django.shortcuts import render

def main(request):
    url='https://ifsc.razorpay.com/'
    url=url+request.GET.get("question")
    json_data=requests.get(url).json()
    print(json_data)
    '''
    print(url)
    final_url=url+ifsc_code
    print(final_url)

    
    bank_information = []
    try:
        r = requests.get(final_url).json()
        print(r)
    except json.decoder.JSONDecodeError:
        print("Didn't make it.")
    '''
    json_info = {
    'ifsc_code' : json_data['IFSC'],
    'STATE' : json_data['STATE'],
    'ADDRESS' : json_data['ADDRESS'],
    'BRANCH' : json_data['BRANCH'],
    'CONTACT' : json_data['CONTACT'],
    'CITY' : json_data['CITY'],
    'BANK' : json_data['BRANCH'],
    'BANKCODE' : json_data['BANKCODE'],
    }
    '''
    final_list=[]

    final_list.append(json_info['ifsc_code'])
    final_list.append(json_info['STATE'])
    final_list.append(json_info['ADDRESS'])
    final_list.append(json_info['BRANCH'])
    final_list.append(json_info['CONTACT'])
    final_list.append(json_info['CITY'])
    final_list.append(json_info['BANK'])
    final_list.append(json_info['BANKCODE'])
    
    '''
    context={'json_info':json_info}
    return render(request, 'main.html',context)

def index(request):
    return render(request,'index.html')
