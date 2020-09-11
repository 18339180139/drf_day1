from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response

from app1.models import User

@csrf_exempt
def user(request):
    if request.method == "GET":
        print(request.GET.get("username"))
        return HttpResponse("GET 访问成功")

    if request.method == "POST":
        print(request.POST.get("username"))
        return HttpResponse("POST 访问成功")

    if request.method == "PUT":
        print("PUT 更新成功")
        return HttpResponse("PUT 更新成功")

    if request.method == "DELETE":
        print("DELETE 删除成功")
        return HttpResponse("DELETE 删除成功")


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):

    def get(self, request, *args, **kwargs):
        print("GET请求  查询")
        return HttpResponse("GET SUCCESS")

    def post(self, request, *args, **kwargs):
        print("POST请求  新增")
        return HttpResponse("POST SUCCESS")

    def put(self, request, *args, **kwargs):
        print("PUT请求  更新")
        return HttpResponse("PUT SUCCESS")

    def delete(self, request, *args, **kwargs):
        print("DELETE请求  删除")
        return HttpResponse("DELETE SUCCESS")


@method_decorator(csrf_exempt, name="dispatch")
class EmployeeView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")

        if user_id:
            user_obj = User.objects.filter(pk=user_id).values("username", "password", "gender", "email").first()
            print(user_obj, type(user_obj))
            if user_obj:
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user_obj
                })
        else:
            user_list = User.objects.all().values("username", "password", "gender", "email")
            return JsonResponse({
                "status": 200,
                "message": "查询所有用户成功",
                "results": list(user_list)
            })

        return JsonResponse({
            "status": 500,
            "message": "查询用户不存在",
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")

        try:
            user_obj = User.objects.create(username=username, password=pwd, email=email)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "email": user_obj.email}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print("这是drf的get请求")
        return Response("DRF GET OK")

    def post(self, request, *args, **kwargs):
        print("这是drf的post请求")
        return Response("DRF POST OK")
