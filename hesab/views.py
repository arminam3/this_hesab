from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import Week, Shopping, Money
from .forms import MoneyForm


class WeekList(generic.ListView):
    model = Week
    template_name = 'hesab/week_list.html'
    context_object_name = 'week_list'


def refresh(request,pk):

    week = Week.objects.get(id=pk)
    shopping = Shopping.objects.filter(week=week).order_by('name')
    moneys = Money.objects.filter(week=week)
    # print(moneys)
    for money in moneys:
        print('=')
        my_money = 0
        chosen_shopping = Shopping.objects.filter(week=week)
        chosen_shopping_buyer = Shopping.objects.filter(week=week, buyer=money.user)
        for shop in chosen_shopping_buyer:
            my_money += int(shop.amount)
        sum=0
        for shop in chosen_shopping:
            sum += shop.amount
            numbers = shop.consumer.all().count()
            # print((shop.consumer.all()))
            if money.user in shop.consumer.all():
                my_money -= int(shop.amount / numbers)
            Money.objects.filter(user=money.user, week=week).update(money=my_money)
    try:
        return render(request, 'hesab/week_details.html', {'week': week, 'sum':sum, 'shopping': shopping})
    except:
        return render(request, 'hesab/week_details.html', {'week': week, 'sum': 0, 'shopping': shopping})





















# class WeekDetails(generic.DetailView):
#     model = Week
#     template_name = 'hesab/week_details.html'
#     context_object_name = 'week'
#
#
# def refresh2(request, pk):
#     week = Week.objects.get(id=pk)
#     shopping = Shopping.objects.filter(week=week)
#     moneys = Money.objects.filter(week=week)
#     for shop in shopping:
#         numbers = shop.consumer.all().count()
#         for con in shop.consumer.all():
#             print(con)
#             my_money = 0
#             my_money -= int(shop.amount/numbers)
#             print('money : ' ,my_money , )
#             if shop.buyer == con:
#                 print(con)
#                 print(shop.buyer == con)
#                 my_money += int(shop.amount)
#             me = Money.objects.filter(user=con, week=week).update(money=my_money)
#             print('me money :',me,'000')
#             # my_con =con
#             print('-------------------------------------------')
#     print('=====================================================')
#             # me_2 = Money.objects.update_or_create(user=my_con
#             #                                       ,week=week,money=10)
#             # money_form = MoneyForm()
#             # print(me_2)
#             # me2 = me.objects.update(money=my_money)
#     return render(request, 'hesab/week_details.html', {'week': week})
