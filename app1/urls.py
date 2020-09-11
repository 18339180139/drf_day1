from django.urls import path

from app1 import views

urlpatterns = [
    path("user/", views.user),
    # 类视图url的定义 与函数视图方式不一样
    path('user2/', views.UserView.as_view()),
    # 匹配包含参数的路由
    path("emp/", views.EmployeeView.as_view()),
    path("emp/<str:id>/", views.EmployeeView.as_view()),
    # DRF 类视图
    path('api_user/', views.UserAPIView.as_view()),
]
