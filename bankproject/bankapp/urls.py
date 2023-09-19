

from django.urls import path

from bankapp import views
app_name='bank'
urlpatterns = [

    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('details',views.details,name='details'),
    path('add',views.Add_Details,name='add'),
    path('<int:pk>/', views.Update_view, name='details_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
    # path('add',views.AddDetailsView.as_view(),name='add'),
    # path('ajax-load-branches',views.load_branches, name='ajax_load_branches'),

]
