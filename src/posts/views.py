from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Sermon, Song, Article



def result(request):
    sermons = Sermon.objects.all()
    songs = Song.objects.all()
    articles = Article.objects.all()
    query = request.GET.get('q')
    if query:
        sermon = sermons.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(category__title__icontains=query) |
            Q(tag__title__icontains=query) |
            Q(minister__minister__icontains=query)
        ).distinct()
    if query:
        song = songs.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(tag__title__icontains=query) |
            Q(minister__minister__icontains=query)
        ).distinct()
    if query:
        article = articles.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(tag__title__icontains=query)
        ).distinct()

    context = {
        'sermon': sermon,
        'song': song,
        'article': article,
        'query': query,
    }
    return render(request, 'result.html', context)


#Category counter functions

def get_intimacy_category_count():
    title = "Intimacy"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)
    count = len(data)
    return count

def get_relationship_counter():
    title = "Relationship"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_marriage_counter():
    title = "Relationship"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_academic_counter():
    title = "Academic"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_revival_counter():
    title = "Revival"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_annointing_counter():
    title = "Annointing"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_wealth_counter():
    title = "Wealth"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_kingdom_lifestyle_counter():
    title = "Kingdom Lifestyle"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_mind_development_counter():
    title = "Mind Development"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_holy_spirit_counter():
    title = "Holy Spirit"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_leadership_counter():
    title = "Leadership"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_character_counter():
    title = "Character"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_prayer_counter():
    title = "Prayer"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_singleness_counter():
    title = "Singleness"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_blessing_counter():
    title = "Blessing"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_mantle_counter():
    title = "Mantle"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_overcoming_addiction_counter():
    title = "Overcoming Addiction"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count

def get_others_counter():
    title = "Others"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    count = len(data)
    return count
#Sermon category counter functions ends here

#Minister category counter starts hers
def get_dr_paul_enenche_counter():
    title = "Pastor Dr. Paul Enenche"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count

def get_apostle_joshua_selman_counter():
    title = "Apostle Joshua Selman Nimmak"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count


def get_apostle_arome_osayi_counter():
    title = "Apostle Arome Osayi"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count

def get_apostle_micheal_orokpo_counter():
    title = "Apostle Micheal Orokpo"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count

def get_bishop_david_oyedepo_counter():
    title = "Bishop David Oyedepo"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count

def get_bro_gbile_akani_counter():
    title = "Bro Gbile Akani"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count

def get_pastor_kingsley_okonkwo_counter():
    title = "Pastor Kinhsley Okonkwo"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count
    
def get_pastor_jerry_eze_counter():
    title = "Pastor Jerry Eze"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count

def get_pastor_ejemi_counter():
    title = "Pastor Ejemi"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count


def get_bishop_david_ibieyomie_counter():
    title = "Bishop David Ibieyomie"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count


def get_apostle_johnson_sulaiman_counter():
    title = "Apostle Johnson Sulaiman"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count


def get_pastor_adeboye_counter():
    title = "Pastor E.A Adeboye"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count

def get_pastor_sam_adeyemi_counter():
    title = "Pastor E.A Adeboye"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count

def get_pastor_chris_oyakhilome_counter():
    title = "Pastor E.A Adeboye"
    sermons = Sermon.objects.all()
    data = []
    for sermon in sermons:
        ints = sermon.minister.all()
        for i in ints:
            if title in i.minister:
                data.append(sermon)

    count = len(data)
    return count



#Minister category counter ends here



def index(request):
    lattest_sermon = Sermon.objects.order_by('-timestamp')[:12]
    lattest_song = Song.objects.order_by('-timestamp')[:10]
    lattest_article  = Article.objects.order_by('-timestamp')[:4]
    context = {
        'lattest_sermon': lattest_sermon,
        'lattest_song': lattest_song,
        'lattest_article': lattest_article,
    }
    return render(request, 'index.html', context)

def article(request):
    article = Article.objects.all().order_by('-timestamp')

    paginator = Paginator(article, 12)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'article.html', context)

def articleView(request, id):
    article = get_object_or_404(Article, id=id)
    lattest_article = Article.objects.order_by('-timestamp')[:4]
    context = {
        'article': article,
        'lattest_article': lattest_article,
    }
    return render(request, 'view-article.html', context)

def sermon(request):
    intimacy_count = get_intimacy_category_count()
    relationhip_count = get_relationship_counter()
    marriage_counter = get_marriage_counter()
    academic_counter = get_academic_counter()
    revival_counter = get_revival_counter()
    annointing_counter = get_annointing_counter()
    wealth_counter = get_wealth_counter()
    kingdom_lifestyle_counter = get_kingdom_lifestyle_counter()
    mind_development_counter = get_mind_development_counter()
    holy_spirit_counter =  get_holy_spirit_counter()
    leadership_counter = get_leadership_counter()
    character_counter = get_character_counter()
    prayer_counter = get_prayer_counter()
    singleness_counter = get_singleness_counter()
    blessing_counter = get_blessing_counter()
    mantle_counter = get_mantle_counter()
    overcoming_addiction_counter = get_overcoming_addiction_counter()
    others_counter = get_others_counter()
    dr_paul_eneche_counter = get_dr_paul_enenche_counter()
    apostle_joshua_selman_counter = get_apostle_joshua_selman_counter()
    apostle_arome_osayi_counter = get_apostle_arome_osayi_counter()
    apostle_micheal_orokpo_counter = get_apostle_micheal_orokpo_counter()
    bidhop_david_oyedepo_counter = get_bishop_david_oyedepo_counter()
    bro_gbile_akani_counter = get_bro_gbile_akani_counter()
    pastor_kingsley_okonkwo_counter = get_pastor_kingsley_okonkwo_counter()
    pastor_jerry_eze_counter = get_pastor_jerry_eze_counter()
    pastor_ejemi_counter = get_pastor_ejemi_counter()
    bishop_david_ibieyomie_counter = get_bishop_david_ibieyomie_counter()
    apostle_johnson_sulaiman_counter = get_apostle_johnson_sulaiman_counter()
    pastor_adeboye_counter = get_pastor_adeboye_counter()
    pastor_sam_adeyemi_counter = get_pastor_sam_adeyemi_counter()
    pastor_chris_oyakhilome_counter = get_pastor_chris_oyakhilome_counter()
    context = {
        'intimacy_count': intimacy_count,
        'relationhip_count': relationhip_count,
        'marriage_counter': marriage_counter,
        'academic_counter': academic_counter,
        'revival_counter': revival_counter,
        'annointing_counter': annointing_counter,
        'wealth_counter': wealth_counter,
        'kingdom_lifestyle_counter': kingdom_lifestyle_counter,
        'mind_development_counter': mind_development_counter,
        'holy_spirit_counter': holy_spirit_counter,
        'leadership_counter': leadership_counter,
        'character_counter': character_counter,
        'prayer_counter': prayer_counter,
        'singleness_counter': singleness_counter,
        'blessing_counter': blessing_counter,
        'mantle_counter': mantle_counter,
        'overcoming_addiction_counter': overcoming_addiction_counter,
        'others_counter': others_counter,
        'dr_paul_eneche_counter': dr_paul_eneche_counter,
        'apostle_joshua_selman_counter': apostle_joshua_selman_counter,
        'apostle_arome_osayi_counter': apostle_arome_osayi_counter,
        'apostle_micheal_orokpo_counter': apostle_micheal_orokpo_counter,
        'bidhop_david_oyedepo_counter': bidhop_david_oyedepo_counter,
        'bro_gbile_akani_counter': bro_gbile_akani_counter,
        'pastor_kingsley_okonkwo_counter': pastor_kingsley_okonkwo_counter,
        'pastor_jerry_eze_counter': pastor_jerry_eze_counter,
        'pastor_ejemi_counter': pastor_ejemi_counter,
        'bishop_david_ibieyomie_counter': bishop_david_ibieyomie_counter,
        'apostle_johnson_sulaiman_counter': apostle_johnson_sulaiman_counter,
        'pastor_adeboye_counter': pastor_adeboye_counter,
        'pastor_sam_adeyemi_counter': pastor_sam_adeyemi_counter,
        'pastor_chris_oyakhilome_counter': pastor_chris_oyakhilome_counter,
    }
    return render(request, 'sermon.html', context)


def playSermon(request, id):
    sermon = get_object_or_404(Sermon, id=id)
    lattest_sermon = Sermon.objects.order_by('-timestamp')[:4]
    context = {
        'sermon': sermon,
        'lattest_sermon': lattest_sermon,
    }
    return render(request, 'play-sermon.html', context)

def playAudio(request, id):
    song = get_object_or_404(Song, id=id)
    lattest_song = Song.objects.order_by('-timestamp')[:4]
    context = {
        'song': song,
        'lattest_song': lattest_song,
    }
    return render(request, 'play-audio.html', context)


def song(request):
    songs = Song.objects.all().order_by('-timestamp')
    paginator = Paginator(songs, 12)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'songs.html', context)

# def songCat(request):
#     return render(request, 'song-category.html', {})


#Sermon category by Categories
def sermonIntimacy(request):
    title = "Intimacy"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)
    page_request_var = 'page'
    paginator = Paginator(data, 16)
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        
    }
    return render(request, 'sermon-intimacy.html', context)

def sermonRelaionship(request):
    title = "Relationship"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        ints = sermon.category.all()
        for i in ints:
            if title in i.title:
                data.append(sermon)

    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-relationship.html', context)

def sermonAcademic(request):
    title = "Academic"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)

    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-academic.html', context)

def sermonAnnointing(request):
    title = "Annointing"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)

    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-annointing.html', context)

def sermonMarriage(request):
    title = "Marriage"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)

    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-marriage.html', context)

def sermonRevival(request):
    title = "Revival"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)

    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-revival.html', context)

def sermonWealth(request):
    title = "Wealth"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-wealth.html', context)

def sermonKingdomLifestyle(request):
    title = "Kingdom Lifestyle"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-kingdom-lifestyle.html', context)

def sermonMindDevelopment(request):
    title = "Mind Development"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-mind-development.html', context)

def sermonHolySpirit(request):
    title = "Holy Spirit"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-holy-spirit.html', context)

def sermonLeadership(request):
    title = "Leadership"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-leadership.html', context)

def sermonCharacter(request):
    title = "Character"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-character.html', context)

def sermonPrayer(request):
    title = "Prayer"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-prayer.html', context)

def sermonSingleness(request):
    title = "Singleness"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-singleness.html', context)

def sermonBlessing(request):
    title = "Blessing"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-blessing.html', context)


def sermonMantle(request):
    title = "Mantle"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    

    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-mantle.html', context)

def sermonOvercomingAddiction(request):
    title = "Overcoming Addiction"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-overcoming-addiction.html', context)

def sermonOthers(request):
    title = "Others"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.category.all()
        for i in inits:
            if title in i.title:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-others.html', context)

#Sermon  category by Ministers
def sermonMinsterDrPaul(request):
    title = "Pastor Dr. Paul Enenche"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    

    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-dr-paul-enenche.html', context)

def sermonMinisterBroGbileAkani(request):
    title = "Bro GBile Akani"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-bro-gbile-akani.html', context)

def sermonMinisterPastorKingsley(request):
    title = "Pastor Kingsley Okonkwo"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-pastor-kingsley.html', context)

def sermonMinisterPastorJerryEze(request):
    title = "Pastor Jerry Eze"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-pastor-jerry-eze.html', context)

def sermonMinisterPastorEjimi(request):
    title = "Pastor Ejemi"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-pastor-ejemi.html', context)

def sermonMinisterBishopDavidIbieyomie(request):
    title = "Bishop David Ibieyomie"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-bishop-david-ibieyomie.html', context)

def sermonMinisterApostleJohnsonSulaiman(request):
    title = "Apostle Johnson Sulaiman"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-apostle-johnson-sulaiman.html', context)

def sermonMinisterPastorAdeboye(request):
    title = "Pastor E.A Adeboye"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-pastor-adeboye.html', context)

def sermonMinisterPastorSamAdeyemi(request):
    title = "Pastor Sam Adeyemi"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-pastor-sam-adeyemi.html', context)

def sermonMinisterPastorChrisOyakhilome(request):
    title = "Pastor Chris Oyakhilome"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-pastor-chris-oyakhilome.html', context)

def sermonMinisterApostleJoshuaSelman(request):
    title = "Apostle Joshua Selman Nimmak"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-apostle-joshua-selman.html', context)

def sermonMinisterApostleAromeOsayi(request):
    title = "Apostle Arome Osayi"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-apostle-arome-osayi.html', context)


def sermonMinisterApostleMichealOrokpo(request):
    title = "APpostle Micheal Orokpo"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-apostle-micheal-orokpo.html', context)


def sermonMinisterBishopDavidOyedepo(request):
    title = "Bishop David Oyedepo"
    sermons = Sermon.objects.all().order_by('-timestamp')
    data = []
    for sermon in sermons:
        inits = sermon.minister.all()
        for i in inits:
            if title in i.minister:
                data.append(sermon)
    
    
    paginator = Paginator(data, 16)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'sermon-M-bishop-david-oyedepo.html', context)


# def disclaimer(request):
#     disclaimer = Disclaimer.objects.first()
#     context = {
#         'disclaimer': disclaimer
#     }
#     return render(request, 'disclaimer.html', context

# def aboutUs(request):
#     return render(request, 'about-us.html', {})




#Song category by Categories
# def articleIntimacy(request):
#     title = "Intimacy"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         ints = sermon.category.all()
#         for i in ints:
#             if title in i.title:
#                 data.append(sermon)
#     context = {
#         'sermons': data,
        
#     }
#     return render(request, 'song-intimacy.html', context)

# def articleRelaionship(request):
#     title = "Relationship"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         ints = sermon.category.all()
#         for i in ints:
#             if title in i.title:
#                 data.append(sermon)

#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-relationship.html', context)

# def articleAcademic(request):
#     title = "Academic"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-academic.html', context)

# def articleAnnointing(request):
#     title = "Annointing"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-annointing.html', context)

# def articleMarriage(request):
#     title = "Marriage"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-marriage.html', context)

# def articleRevival(request):
#     title = "Revival"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-revival.html', context)

# def articleWealth(request):
#     title = "Wealth"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-wealth.html', context)

# def articleKingdomLifestyle(request):
#     title = "Kingdom Lifestyle"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-kingdom-lifestyle.html', context)

# def articleMindDevelopment(request):
#     title = "Mind Development"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-mind-development.html', context)

# def articleHolySpirit(request):
#     title = "Holy Spirit"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-holy-spirit.html', context)

# def articleLeadership(request):
#     title = "Leadership"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-leadership.html', context)

# def articleCharacter(request):
#     title = "Character"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-character.html', context)

# def articlePrayer(request):
#     title = "Prayer"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-prayer.html', context)

# def articleSingleness(request):
#     title = "Singleness"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-singleness.html', context)

# def articleBlessing(request):
#     title = "Blessing"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-blessing.html', context)


# def articleMantle(request):
#     title = "Mantle"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-mantle.html', context)

# def articleOvercomingAddiction(request):
#     title = "Overcoming Addiction"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-overcoming-addiction.html', context)

# def articleOthers(request):
#     title = "Others"
#     sermons = Sermon.objects.all()
#     data = []
#     for sermon in sermons:
#         inits = sermon.category.all()
#         for i in inits:
#             if title in i.title:
#                 data.append(sermon)
    
#     context = {
#         'sermons': data,
#     }
#     return render(request, 'song-others.html', context)


def sermon_apostle_joshua_selman_2012(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2012.html', {})

def sermon_apostle_joshua_selman_2013(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2013.html', {})

def sermon_apostle_joshua_selman_2014(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2014.html', {})

def sermon_apostle_joshua_selman_2015(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2015.html', {})

def sermon_apostle_joshua_selman_2016(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2016.html', {})

def sermon_apostle_joshua_selman_2017(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2017.html', {})

def sermon_apostle_joshua_selman_2018(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2018.html', {})

def sermon_apostle_joshua_selman_2019(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2019.html', {})

def sermon_apostle_joshua_selman_2020(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2020.html', {})

def sermon_apostle_joshua_selman_2021(request):
    return render(request, 'sermon_M_Apostle_Joshua_Selman_2021.html', {})

