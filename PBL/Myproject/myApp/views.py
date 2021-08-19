from django.shortcuts import render,redirect
from myApp.models import Adding_branch,CreatedDatabases,Published_Databases
from datetime import date
from Myproject.settings import BASE_DIR
from myApp.push import *
from myApp.check import *
from django.http import HttpResponse
from django.contrib import messages
def home(request):
    if request.method=='POST':
        pr=request.POST['program']
        reg=request.POST['regulation']
        sem=request.POST['Semister']
        et=request.POST['Examtype']
        cd=request.POST['submit']
        if str(cd)=='Create Database':
            CreatedDatabases.objects.create(program=pr,regulation=reg,semister=sem,examtype=et)
            return redirect('show/')
    return render(request,'index.html')
def available_files(request):
    data=CreatedDatabases.objects.order_by('-id')
    return render(request,'show.html',{'files':data})


def adding_branch(request,id):
    if request.method=="POST":
        br=request.POST['branch']
        file=request.FILES['document']
        if request.POST['submit']=="ADD":
            Adding_branch.objects.create(added_branch_file=file,added_branch_name=br,CDid=id,table_name=br+str(id))
            data=CreatedDatabases.objects.get(id=id)
            data.no_of_branches_result_user_add+=1
            data.save()
            file=Adding_branch.objects.get(CDid=id,added_branch_name=br)
            path=str(BASE_DIR)+'/media/'+str(file.added_branch_file)
            tn=file.table_name
            create_a_table_in_database(tn,path)
            push_data_to_table(path,tn)
            messages.info(request,"Successfully push data into database")
            return redirect('show')
    return render(request,'add_branch.html')


def available_branch_files(request,id):
    data=Adding_branch.objects.filter(CDid=id)
    return render(request,'available_branch_res.html',{'files':data})



def publish(request,id):
    data1=CreatedDatabases.objects.get(id=id)
    if data1.is_published==1:
        messages.warning(request, 'Already result is published')
        return redirect('show')
    else:
        data1.is_published=1
        data1.save()
        data2=Published_Databases.objects.create(CrData_id=id,is_published='YES')
        messages.info(request,"Successfully Published")
        return redirect('show')



def get_result(request):
    if request.method=='POST':
        ht=request.POST['hallticket']
        dob=request.POST['dateofbirth']
        ids=get_ids_of_databases()
        tables=get_tables_which_published(ids)
        data=search_result(ht,dob,tables)
        return render(request,'displayresult.html',{'data':data})
    return render(request,'get_result.html')