from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('studio/', include('studio.urls')),
    path('studios/', include('studio.urls')),
    path('question/', include('question.urls')),
    path('answer/', include('answer.urls')),
    path('portfolio/', include('photo.urls'))
]
