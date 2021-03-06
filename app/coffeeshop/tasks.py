import datetime

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from coffeeshop.crawling.starbucks import *
from coffeeshop.crawling.twosome import *
from config import celery_app


@celery_app.task(name='starbucks_crawling')
def starbucks_crawling():
    starbucks_log = Starbucks.get_coffee_info()

    message = render_to_string('coffeeshop/crawling_result_email.html',
            {'dict_log': starbucks_log},

    )
    # 위의 크롤링 함수가 종료되면 내 이메일 계정에 보고
    now_date = datetime.datetime.now().strftime('%Y-%m-%d')

    crawling_result = f'{now_date} 에 대한 크롤링 완료 메세지'
    to_email = 'hanyonghee9264@gmail.com'

    email = EmailMessage(crawling_result, message, to=[to_email])
    email.send()


@celery_app.task(name='twosome_crawling')
def twosome_crawling():
    twosomes_log = Twosome.get_coffee_info()

    message = render_to_string('coffeeshop/crawling_result_email.html',
            {'dict_log': twosomes_log},

    )
    # 위의 크롤링 함수가 종료되면 내 이메일 계정에 보고
    now_date = datetime.datetime.now().strftime('%Y-%m-%d')

    crawling_result = f'{now_date} 에 대한 크롤링 완료 메세지'
    to_email = 'hanyonghee9264@gmail.com'

    email = EmailMessage(crawling_result, message, to=[to_email])
    email.send()
