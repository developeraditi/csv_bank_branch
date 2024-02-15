from django.shortcuts import render

# Create your views here.
from app.models import *

from django.http import HttpResponse

import csv
def insert_bank(self):
    with open('C:\\Users\\Aditi Srivastava\\Desktop\\djangoproject\\Aditi\\Scripts\\CSVFile\\app\\bank.csv','r') as FO:
        IOD =csv.reader(FO)
        for i in IOD:
            bn= i[0].strip()
            BO= Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank Data is inserted')


def insert_branch(self):
    with open('C:\\Users\\Aditi Srivastava\\Desktop\\djangoproject\\Aditi\\Scripts\\CSVFile\\app\\branch1.csv','r') as FO:
        IOD= csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                d=i[6]
                s=i[7]

                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=d,state=s)
                BRO.save()
    return HttpResponse('Data is inserted')
                

