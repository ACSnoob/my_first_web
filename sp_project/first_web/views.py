from django.shortcuts import render ,HttpResponse,redirect
from first_web.models import Memberinfo as mem
from first_web.models import PwdSaveInfo as pwds

# Create your views here.





def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
          get_date = request.POST
          username = get_date.get('username')
          pwd = get_date.get('pwd')
          date = pwds.objects.all()
          num = date.count()#读取数据库中已注册的人数
          for n in range(1,num+1):
               date_check = pwds.objects.filter(id = n).first()#读取单行的信息
               if date_check:
                    if username == date_check.user and str(pwd) == date_check.pwd:
                              print('yes')
                              return redirect('/system/')
                    else:
                         continue
          return render(request,'login.html',{'tip':'用户名或密码错误'})          

def register(request):
     if request.method == "GET":
          return render(request,'register.html')
     elif request.method == "POST":
          date = request.POST
          username = date.get('user')
          post_pwd = date.get('pwd')
          pwds.objects.create(user = username,pwd = post_pwd)
          return render(request,'register.html',{'tip':'注册成功'})




def system(request):
        #系统的正式页
        tests = mem.objects.all()
        return render(request,'system.html',{'all':tests})
def member_add(request):
     #添加人员
     if request.method == "POST":
          post_date = request.POST
          mem.objects.create(
               name = post_date.get('name') ,
               department = post_date.get('department'),
               join_time = post_date.get('join_time')
               )#将添加的人员名称加入到数据库中
          return redirect('/system/')
     elif request.method == 'GET':
          return render(request,'member_add.html')
def member_delete(request):
     # 进行人员的删除
     if request.method == "GET":
        num_date = request.GET.get('id')
        mem.objects.filter(id = num_date).delete()
        return redirect('/system/')
def member_change(request):
     #对人员信息的修改
     if request.method == "GET":
        num_date = request.GET.get('id')
        return render(request,'member_change.html',{'num_date':num_date,})
     elif request.method == "POST":
          date = request.POST
          #确保各项值的有效性并将其加入字典update_date，实现可指定修改内容
          update_date = {}
          if date.get('name'):
              update_date['name'] = date.get('name')
          if date.get('department'):
              update_date['department'] = date.get('department')
          if date.get('join_time'):
              update_date['join_time'] = date.get('join_time')
          print(update_date)
          num = date.get('id')
          print(int(num))
          mem.objects.filter(id = int(num)).update(**update_date)#将字典中的值展开
          return redirect('/system/')
          
