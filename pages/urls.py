from django.urls import path
from .views import PageListView,PageDetailView,PageCreate,PageUpdate,PageDelete
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/',staff_member_required(PageCreate.as_view(template_name="page_form.html")),name="create"),
    path('update/<int:pk>/',PageUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',PageDelete.as_view(),name='delete')
],'pages')