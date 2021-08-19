from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myApp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('show/',views.available_files,name='show'),
    path('adding_branch_result/<int:id>/',views.adding_branch,name='add_branch_res'),
    path('br_reslt/<int:id>/',views.available_branch_files,name='abf'),
    path('publish/<int:id>/',views.publish,name='publish'),
    path('result/',views.get_result,name='result')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)