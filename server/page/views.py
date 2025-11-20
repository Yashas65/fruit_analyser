from django.shortcuts import render
import sys , os , time

def index(request):

    context = {} # to frontend

    return render(request , 'page/index.html',context)

def show_results(request):

    from process.camera import camera
    camera()
 
    from process.model import model
    time.sleep(1)# just in case if pendrive/sdcard is slow
    

    out = model()
    max_out = max(out)
    
    #getting the index to find out what matches the maximum percent
    pos = out.index(max_out)
    
    
    #the given output is in this sequence , and the order is very sensitive
    data_organised = [
        'fresh_apple',
        'fresh_banana',
        'raw_apple',
        'raw_banana',
        'rotten_apple',
        'rotten_banana',
    ]

    # make sure to see if prediction scores are very low then replace this with none or and  error(not raising an error printing it)
    item = data_organised[pos]  
    
    if max_out < 4:   # this means less than 40%
        item = "problem capturing image"        # dear team see this error pls change it if you like
        max_out = 0
    context = {         # this is going to be sent to frontend 
        
        "item":item,
        "percentage": max_out*10
    
    }

    return render(request,'page/results.html',context)
