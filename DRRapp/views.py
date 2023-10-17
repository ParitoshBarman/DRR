from django.shortcuts import render, redirect, HttpResponse
from DRRapp.models import DRRdb
from json import dumps

# Create your views here.
def index(request):
    if request.method == 'POST':
        showAmount = request.POST.get('showAmount')
        fromEntry = request.POST.get('fromEntry')
        toEntry = request.POST.get('toEntry')

        newfromEntry = toEntry
        newtoEntry = toEntry+showAmount

        sendData = {
            'DRRdb' : DRRdb.objects.all()[newfromEntry:newtoEntry],
            'totalEntries' : len(DRRdb.objects.all()),
            'fromEntry' : newfromEntry,
            'toEntry' : newtoEntry
            }

    sendData = {
            'DRRdb' : DRRdb.objects.all()[0:9],
            'totalEntries' : len(DRRdb.objects.all()),
            'fromEntry' : 1,
            'toEntry' : 1+len(DRRdb.objects.all()[0:9])-1
            }
    print()
    return render(request, 'drr.html', sendData)
    

def savedata(request):
    if request.method == 'POST':
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        month_year = request.POST.get('month_year')
        datesExcluded = request.POST.get('datesExcluded')
        numberOfDays = request.POST.get('numberOfDays')
        leadCount = request.POST.get('leadCount')
        expectedDrr = request.POST.get('expectedDrr')
        dbDataSave = DRRdb(action="N/A",startDate=startDate, endDate=endDate, month_year=month_year, datesExcluded=datesExcluded, numberOfDays=numberOfDays, leadCount=leadCount, expectedDrr=expectedDrr)
        dbDataSave.save()
        return redirect("/")

def nextPage(request, showAmount, fromEntry, toEntry):
    if toEntry<0:
        toEntry = 10
    newfromEntry = toEntry
    newtoEntry = toEntry+showAmount

    sendData = {
        'DRRdb' : DRRdb.objects.all()[newfromEntry:newtoEntry],
        'totalEntries' : len(DRRdb.objects.all()),
        'fromEntry' : newfromEntry,
        'toEntry' : newfromEntry+len(DRRdb.objects.all()[newfromEntry:newtoEntry])-1
        }
    return render(request, 'drr.html', sendData)

def previusPage(request, showAmount, fromEntry, toEntry):
    newfromEntry = fromEntry-showAmount
    if newfromEntry<0:
        newfromEntry=0
    newtoEntry = fromEntry

    sendData = {
        'DRRdb' : DRRdb.objects.all()[newfromEntry:newtoEntry],
        'totalEntries' : len(DRRdb.objects.all()),
        'fromEntry' : newfromEntry,
        'toEntry' : newfromEntry+len(DRRdb.objects.all()[newfromEntry:newtoEntry])-1
        }
    return render(request, 'drr.html', sendData)

def deletdata(request, slID):
    findData = DRRdb.objects.get(slID=slID)
    findData.delete()
    return redirect("/")