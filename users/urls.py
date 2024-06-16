from django.urls import include, path
# from rest_framework import routers
# from . import views
from .views import ListOfUserViews

# router = routers.DefaultRouter()
# router.register('users', views.ListOfUserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', ListOfUserViews.as_view()),
    path('users/<int:id>', ListOfUserViews.as_view()),
]