from django.conf.urls import url

from . import views


urlpatterns = [
    url(regex=r'een/$', view=views.LevelEenView.as_view(), name='opdrachteen'),
    url(regex=r'een/reset/$', view=views.LevelEenReset.as_view(), name='opdrachteenreset'),
    url(regex=r'twee/$', view=views.LevelTweeView.as_view(), name='opdrachttwee'),
    url(regex=r'twee/reset/$', view=views.LevelTweeReset.as_view(), name='opdrachttweereset'),
    url(regex=r'drie/$', view=views.LevelDrieView.as_view(), name='opdrachtdrie'),
    url(regex=r'drie/reset/$', view=views.LevelDrieReset.as_view(), name='opdrachtdriereset'),
    url(regex=r'vier/$', view=views.LevelVierView.as_view(), name='opdrachtvier'),
    url(regex=r'vier/reset/$', view=views.LevelVierReset.as_view(), name='opdrachtvierreset'),
    url(regex=r'index/$', view=views.IndexView.as_view(), name='index'),
]