from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PrePassangerData,PostPassangerData
from train import models as trainModel
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from railline.settings import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY,STRIPE_WEBHOOK_KEY
import stripe
import json
stripe.api_key = STRIPE_SECRET_KEY

@login_required(login_url='/user/login')
def userBooking(request):
    if request.method != 'POST':
        return HttpResponse("Failed")
    param = {}
    train_id = int(request.POST.get("train-id"))
    seat_limit = list(trainModel.trainRecord.objects.filter(id=train_id).values())
    seat_limit = seat_limit[0]
    param['train_info'] = {
        'train_no': int(request.POST.get("train-no")),
        'train_id': int(request.POST.get("train-id")),
        'destination': request.POST.get("destination"),
        'boarding': request.POST.get("boarding"),
        'date': request.POST.get("date"),
        'seat_type': request.POST.get("seat_type"),
        'seat_price': float(request.POST.get("price")),
        'seat_limit': int(seat_limit['Seat_SL']),
    }
    print(param)
    return render(request,'./booking/form.html',param)


def paymentTest(request):
    if request.method != "POST":
        return render(request,"booking/payment-test.html");
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'unit_amount': 1000,
                    'product_data': {
                        'name':"Famous Product",
                    },
                },
                'quantity': 2,
            },
        ],
        metadata={
            "product_id": 25
        },
        mode='payment',
        success_url='http://127.0.0.1:8000/booking/success',
        cancel_url='http://127.0.0.1:8000/booking/cancel',
    )
    return redirect(checkout_session.url, code=303)


@login_required(login_url='/user/login')
def paymentPreProcess(request):
    if request.method != "POST":
        return HttpResponse("failed Because of not Post Method")
    pre_id = storePrePayment(request)
    if pre_id == -1:
        return HttpResponse("store Pre payment return False")
    try:
        product = PrePassangerData.objects.get(id=pre_id)
    except Exception as e:
        print("this ", e)
        return HttpResponse("failed Because of product fail to fullfill")
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'unit_amount': product.seat_total_count*product.seat_price*100,
                    'product_data': {
                        'name': product.seat_type,
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": product.id
        },
        mode='payment',
        success_url='http://127.0.0.1:8000/booking/success',
        cancel_url='http://127.0.0.1:8000/booking/cancel',
    )
    print(checkout_session.url)
    return redirect(checkout_session.url, code=303)

    
@login_required(login_url='/user/login')
def storePrePayment(request):
    try:
        print(request.POST.get('train_id'),list(request))
        savingData = PrePassangerData(
            user_id=request.user,
            personal_full_name=request.POST.get("full_name"),
            personal_age=int(request.POST.get("age")),
            personal_email=request.POST.get("email"),
            personal_phone_no=int(request.POST.get("phone_no")),
            train_id=int(request.POST.get('train_id')),
            seat_total_count=int(request.POST.get("ticket_no")),
            seat_type=request.POST.get("seat_type"),
            seat_price=float(request.POST.get('seat_price')),
            boarding=request.POST.get("boarding"),
            destination=request.POST.get("destination"),
            date=request.POST.get("date"),
        )
        savingData.save()
        return savingData.pk
    except Exception as e:
        print("error Occur at saving Data",e)
        return -1
    
    
def success(request):
    return render(request,'booking/success.html')

def cancel(request):
    return render(request, 'booking/failed.html')


@csrf_exempt
def stripeWebhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_KEY
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=401)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=402)

  # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        fulfill_order(session)
  # Passed signature verification
    return HttpResponse(status=200)


@login_required(login_url='/user/login')
def fulfill_order(session):
    product_id = session["metadata"]["product_id"]
    post_payment_id = session["payment_intent"]
    try:
        prePaymentInfo = PrePassangerData.objects.get(id=product_id);
    except:
        print("not found pre payment data!")
    try:
        postPaymentModel = PostPassangerData(
            user_id=prePaymentInfo.user_id,
            personal_full_name=prePaymentInfo.personal_full_name,
            personal_age=prePaymentInfo.personal_age,
            personal_email=prePaymentInfo.personal_email,
            personal_phone_no=prePaymentInfo.personal_phone_no,
            payment_id=post_payment_id,
            seat_total_count=prePaymentInfo.seat_total_count,
            seat_type=prePaymentInfo.seat_type,
            seat_price=prePaymentInfo.seat_price,
            train_id=prePaymentInfo.train_id,
            boarding=prePaymentInfo.boarding,
            destination=prePaymentInfo.destination,
            date=prePaymentInfo.date,
        )
        postPaymentModel.save()
    except Exception as e:
        print("error ay storing the postPayment",e)


@login_required(login_url='/user/login')
def userBill(request):
    user_id = request.user
    post_payment_model = PostPassangerData.objects.filter(user_id = user_id).values()
    return HttpResponse(f"{list(post_payment_model)[0]}")
    
