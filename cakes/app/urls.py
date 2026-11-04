from django.urls import path
from .import views

urlpatterns = [
    path('cakes/', views.CakeCreateListCreateView.as_view()),

    path('cakes/<int:id>/', views.CakeRetrieveUpdateDestroyView.as_view()),

    path('Cake/', views.CakeCreateListCreateView.as_view()),

    path('Cake/<int:id>/', views.CakeRetrieveUpdateDestroyView.as_view()),

    path('Shape/', views.ShapeCreateListCreateView.as_view()),

    path('Shape/<int:id>/', views.ShapeRetrieveUpdateDestroyView.as_view()),

    path('Category/', views.CategoryCreateListCreateView.as_view()),

    path('Category/<int:id>/', views.CategoryRetrieveUpdateDestroyView.as_view()),

    path('Weight/', views.WeightCreateListCreateView.as_view()),

    path('Weight/<int:id>/', views.WeightRetrieveUpdateDestroyView.as_view())


]
