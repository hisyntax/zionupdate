from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import (
    index,  article, articleView, sermon, playSermon,
    song, playAudio, result, sermonIntimacy, sermonRelaionship,
    sermonAcademic, sermonAnnointing, sermonMarriage, sermonRevival,
    sermonWealth, sermonKingdomLifestyle, sermonMindDevelopment,
    sermonHolySpirit, sermonLeadership, sermonCharacter, sermonPrayer,
    sermonSingleness, sermonBlessing, sermonMantle, sermonOvercomingAddiction,
    sermonOthers, sermonMinsterDrPaul, sermonMinisterBroGbileAkani, sermonMinisterPastorKingsley,
    sermonMinisterPastorJerryEze, sermonMinisterPastorEjimi, sermonMinisterBishopDavidIbieyomie,
    sermonMinisterApostleJohnsonSulaiman, sermonMinisterPastorAdeboye, sermonMinisterPastorSamAdeyemi,
    sermonMinisterPastorChrisOyakhilome, sermonMinisterApostleJoshuaSelman, sermonMinisterApostleAromeOsayi,
    sermonMinisterApostleMichealOrokpo, sermonMinisterBishopDavidOyedepo,
    # articleAcademic, articleAnnointing,
    # articleBlessing, articleCharacter, articleHolySpirit, articleIntimacy, articleKingdomLifestyle, articleLeadership,
    # articleMantle, articleMarriage, articleMindDevelopment, articleOthers, articleOvercomingAddiction,
    # articlePrayer, articleRelaionship, articleRevival, articleSingleness, articleWealth


    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('article', article),

    #List of all article categories
    # path('article/category/intimacy', articleIntimacy),
    # path('article/category/relationship', articleRelaionship),
    # path('article/category/academic', articleAcademic),
    # path('article/category/marriage', articleMarriage),
    # path('article/category/revival', articleRevival),
    # path('article/category/annointing', articleAnnointing),
    # path('article/category/wealth', articleWealth),
    # path('article/category/kingdom-lifestyle', articleKingdomLifestyle),
    # path('article/category/mind-development', articleMindDevelopment),
    # path('article/category/holy-spirit', articleHolySpirit),
    # path('article/category/leadership', articleLeadership),
    # path('article/category/character', articleCharacter),
    # path('article/category/prayer', articlePrayer),
    # path('article/category/singleness', articleSingleness),
    # path('article/category/blessing', articleBlessing),
    # path('article/category/mantle', articleMantle),
    # path('article/category/overcoming-addiction', articleOvercomingAddiction),
    # path('article/category/others', articleOthers),

    path('article/category/<id>/', articleView, name='readArticle'),
    path('sermon', sermon),


    #List of all sermon categories
    path('sermon/category/intimacy', sermonIntimacy),
    path('sermon/category/relationship', sermonRelaionship),
    path('sermon/category/academic', sermonAcademic),
    path('sermon/category/marriage', sermonMarriage),
    path('sermon/category/revival', sermonRevival),
    path('sermon/category/annointing', sermonAnnointing),
    path('sermon/category/wealth', sermonWealth),
    path('sermon/category/kingdom-lifestyle', sermonKingdomLifestyle),
    path('sermon/category/mind-development', sermonMindDevelopment),
    path('sermon/category/holy-spirit', sermonHolySpirit),
    path('sermon/category/leadership', sermonLeadership),
    path('sermon/category/character', sermonCharacter),
    path('sermon/category/prayer', sermonPrayer),
    path('sermon/category/singleness', sermonSingleness),
    path('sermon/category/blessing', sermonBlessing),
    path('sermon/category/mantle', sermonMantle),
    path('sermon/category/overcoming-addiction', sermonOvercomingAddiction),
    path('sermon/category/others', sermonOthers),

    #List of all sermon ministers
    path('sermon/minister/dr-paul-eneche', sermonMinsterDrPaul),
    path('sermon/minister/bro-gbile-akani', sermonMinisterBroGbileAkani),
    path('sermon/minister/pastor-kingsley-okonkwo', sermonMinisterPastorKingsley),
    path('sermon/minister/pastor-jerry-eze', sermonMinisterPastorJerryEze),
    path('sermon/minister/pastor-ejimi', sermonMinisterPastorEjimi),
    path('sermon/minister/bishop-david-ibieyomie', sermonMinisterBishopDavidIbieyomie),
    path('sermon/minister/bishop-david-oyedepo', sermonMinisterBishopDavidOyedepo),
    path('sermon/minister/apostle-johnson-sulaiman', sermonMinisterApostleJohnsonSulaiman),
    path('sermon/minister/pastor-adeboye', sermonMinisterPastorAdeboye),
    path('sermon/minister/pastor-sam-adeyemi', sermonMinisterPastorSamAdeyemi),
    path('sermon/minister/pastor-chris-oyakhilome', sermonMinisterPastorChrisOyakhilome),
    path('sermon/minister/apostle-joshua-selman', sermonMinisterApostleJoshuaSelman),
    path('sermon/minister/apostle-arome-osayi', sermonMinisterApostleAromeOsayi),
    path('sermon/minister/apostle-micheal-orokpo', sermonMinisterApostleMichealOrokpo),

    path('sermon/category/<id>/', playSermon, name='playSermon'),

    path('song', song),
    path('song/<id>/', playAudio, name='playSong'),
    path('search', result, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
