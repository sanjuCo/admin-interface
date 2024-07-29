from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('items/', views.items, name='items'),
    path('transactions/', views.transactions, name='transactions'),
    path('stats/', views.stats, name='stats'),
    path('documentation/', views.documentation, name='documentation'),
    path('logout/', views.logout_user, name='logout'),
    path('add_product/', views.addProd, name='add-prod'),
    path('del_product/', views.delProd, name='del-prod'),
    path('add_item/', views.addItem, name='add-item'),
    path('del_item/', views.delItem, name='del-item'),
    path('test/', views.test, name='test'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)