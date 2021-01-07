from django.urls import path
from django.contrib.auth.decorators import login_required
# from django.contrib.sitemaps.views import sitemap
from . import views, sitemaps

app_name = 'baseApp'

# sitemaps_dict = {'Static_sitemap': sitemaps.StaticSitemap,
#                 'AllPostSitemap': sitemaps.AllPostSitemap,
#                 'Asset_sitemap': sitemaps.AssetSitemap,
#                 'AssetFa_sitemap': sitemaps.AssetFaSitemap,
#                 'Post_sitemap': sitemaps.PostSitemap,
#                 'PostFa_sitemap': sitemaps.PostFaSitemap,
#                 'FAQ_sitemap': sitemaps.FAQCategoriesSitemap,
#                 'FAQFa_sitemap': sitemaps.FAQCategoriesFaSitemap
#                 }

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='productView'),

    # AJAX test
    # path('ajaxtest/', views.AJAX_TEST.as_view(), name='ajax_test'),

    # All Asset Download Excel file
    # path('export-page/', login_required(views.ExcelOutputAssets.as_view()), name='export_page'),

    # This is for sitemap.xml
    # path('ResumeSiteMap.xml', sitemap, {'sitemaps': sitemaps_dict},
    #  name='django.contrib.sitemaps.views.sitemap'),
]


# handler404 = 'apps.baseApp.views.error_404'
# handler500 = 'apps.baseApp.views.error_500'
