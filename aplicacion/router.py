from rest_framework.routers import DefaultRouter

router_post = DefaultRouter()
router_post.register(prefix="registro", basename="registro", viewset=RegApiView)