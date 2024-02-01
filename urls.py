from django.urls import path
from .import views

urlpatterns = [
    path('', views.homefn),
    path('register', views.registertionfn),
    path('login', views.loginfn),
    path('category/<int:c_id>', views.categoryfn),
    path('profile', views.profilefn),
    path('profileform', views.Profileform),
    path('logout', views.logoutfn),
    path('viewpage/<int:p_id>',views.viewfn),
    path('search',views.searchfn),
    # path('add_to_cart/',views.addtocart, name="add-to-cart"),
    # path('cart/',views.cart, name="cart")
]
