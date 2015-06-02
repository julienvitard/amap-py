from django.conf.urls import url, include
from rest_framework import routers
from amappy.users.views import (
    UserViewSet,
    DistributorViewSet,
    SupervisorViewSet,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Add /users/ url
router.register(r'users', UserViewSet)
router.register(r'distributors', DistributorViewSet)
router.register(r'supervisors', SupervisorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
