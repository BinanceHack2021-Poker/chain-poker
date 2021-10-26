from django.urls import path

from web.views import IndexView


app_name = 'web'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('gift/<slug:slug>', GiftDetailView.as_view(), name='gift_detail'),
    # path('ethereum-wallet', EhtereumWalletView.as_view(), name='ethereum_wallet'),
    # path('check-gift/<str:to_wallet>', SendAndCheckGiftView.as_view(), name='send_and_check'),
]
