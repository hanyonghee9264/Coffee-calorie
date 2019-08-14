from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from .models import Coffee, CoffeeCategory, CoffeeImage


def starbucks_total_list(request):
    details = Coffee.objects.all()

    # pagination (전체보기 적용)
    paginator = Paginator(details, 6)

    page = request.GET.get('page')

    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)

    # url의 쿼리스트링을 가져옴. 없는 경우 None을 리턴
    calorie = request.GET.get('calorie')

    if calorie == 'high':
        details = Coffee.objects.all().order_by('-calorie')
        return render(request, 'coffeeshop/starbucks_total_list.html', {'details': details})

    elif calorie == 'low':
        details = Coffee.objects.all().order_by('calorie')
        return render(request, 'coffeeshop/starbucks_total_list.html', {'details': details})

    context = {
        'details': details,
    }
    return render(request, 'coffeeshop/starbucks_total_list.html', context)


def starbucks_category_coffee(request, category):
    coffee = Coffee.objects.filter(category__name__contains=category)
    # url의 쿼리스트링을 가져옴. 없는 경우 None을 리턴
    calorie = request.GET.get('calorie', 'None')

    if calorie == 'high':
        coffee = Coffee.objects.filter(category__name__contains=category).order_by('-calorie')
        return render(request, 'coffeeshop/starbucks_category_coffee.html', {'coffee': coffee})

    elif calorie == 'low':
        coffee = Coffee.objects.filter(category__name__contains=category).order_by('calorie')
        return render(request, 'coffeeshop/starbucks_category_coffee.html', {'coffee': coffee})

    context = {
        'coffee': coffee,
    }
    return render(request, 'coffeeshop/starbucks_category_coffee.html', context)
