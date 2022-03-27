from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import json
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Auction,Bider
# Create your views here.
def auction(request):
    auctions = Auction.objects.all()
    context = {
        'auctions':auctions,
    }
    return render(request, 'auction/auction.html', context)

@login_required(login_url='/login')
def bid(request,id):
    details = Auction.objects.get(id=id)
    auctions =  Bider.objects.filter(auction=details)
    related_auctions =  Auction.objects.all()[:4]
    highest_bid = max(auctions.values_list('amount', flat=True), default=0)
    latest_bid =  Bider.objects.filter(user=request.user, auction=details).last()
    # if request.method == 'POST':
    #     print(request.POST)
    #     form = bidForm(request.POST)
    #     bider = Bider()
    #     if form.is_valid():
    #         bider.amount= form.cleaned_data['amount']
    #         bider.auction_id = form.cleaned_data['auction']
    #         bider.user = request.user
    #         bider.save()
    #         messages.success(request, "Bid Submitted")
    #         return redirect('bid', id=id)
    
    if request.is_ajax():
        highest_bid_s = round(highest_bid, 1)
        return JsonResponse(highest_bid_s,safe=False)
    data = {       
    'data':details,
    'highest_bid':highest_bid,
    'latest_bid':latest_bid,
    'related_auctions':related_auctions
    }
    return render(request, 'auction/bidding.html',data)


def add_bid(request):
    if request.method == 'POST':
        print(request.POST)
        amount = request.POST.get('the_amount')
        auction = request.POST.get('the_auction')
        response_data = {}

        bid = Bider(amount=amount, auction_id=auction, user=request.user)
        bid.save()

        response_data['result'] = 'BID SUBMITTED'
        response_data['bid_id'] = bid.pk
        response_data['amount'] = bid.amount
        response_data['auction'] = bid.auction_id
        response_data['bider'] = bid.user.username

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"Error":"Failed to submit"}),
            content_type = 'application/json'

        )