from django.contrib import admin
from django.urls import path
from services.api_views import ServiceListAPIView
from universities.api_views import UniversityListAPIView
from applications.api_views import ApplicationCreateAPIView, ApplicationListAPIView
from testimonials.api_views import TestimonialListAPIView
from blogs.api_views import BlogListAPIView
from events.api_views import EventListAPIView
from contacts.api_views import ContactMessageCreateAPIView, ContactMessageListAPIView

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/services/', ServiceListAPIView.as_view(), name='service-list'),
    path('api/universities/', UniversityListAPIView.as_view(), name='university-list'),
    path('api/applications/', ApplicationListAPIView.as_view(), name='application-list'),
    path('api/applications/create/', ApplicationCreateAPIView.as_view(), name='application-create'),
    path('api/testimonials/', TestimonialListAPIView.as_view(), name='testimonial-list'),
    path('api/blogs/', BlogListAPIView.as_view(), name='blog-list'),
    path('api/events/', EventListAPIView.as_view(), name='event-list'),
    path('api/contacts/', ContactMessageListAPIView.as_view(), name='contact-list'),
    path('api/contacts/create/', ContactMessageCreateAPIView.as_view(), name='contact-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
