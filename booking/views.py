from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from train import models as trainModel
from django.contrib.auth.models import User
from django.views import View

@login_required(login_url='/user/login')
def userBooking(request):
    if request.method != 'POST':
        return HttpResponse("Failed")
    param = {}
    train_id = int(request.POST.get("train-id"))
    seat_limit = list(trainModel.trainRecord.objects.filter(id=train_id).values())
    seat_limit = seat_limit[0]
    print(seat_limit['Seat_SL'])
    param['train_info'] = {
        'train_no': request.POST.get("train-no"),
        'train_id': request.POST.get("train-id"),
        'destination': request.POST.get("destination"),
        'boarding': request.POST.get("boarding"),
        'date': request.POST.get("date"),
        'seat_type': request.POST.get("seat_type"),
        'price': request.POST.get("price"),
        'seat_limit': seat_limit['Seat_SL'],
    }
    return render(request,'./booking/form.html',param)
# class CreateCheckoutSessionView(View):
#     def post(self,request,*args,**kwargs):
#     product_id = self.kwargs['pk']
#     product = Product.objects.get(id=product_id)
#     print(product)
#     checkout_session = stripe.checkout.Session.create(
#         line_items=[
#             {
#                 'price_data': {
#                     'currency': 'inr',
#                     'unit_amount': product.price,
#                     'product_data': {
#                         'name': product.name,
#                     },
#                 },
#                 'quantity': 1,
#             },
#         ],
#         metadata={
#             "product_id": product.id
#         },
#         mode='payment',
#         success_url='http://127.0.0.1:8000/success/',
#         cancel_url='http://127.0.0.1:8000/cancel/',
#     )
#     print(checkout_session.url)
#     return redirect(checkout_session.url, code=303)


