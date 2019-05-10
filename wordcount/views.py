from django.shortcuts import render

# Create your views here.

def index(request):
    

    
    return render(request,"index.html")


def result(request):

    text = request.GET['text']
    word_list=text.split(" ")
    word_count={}

    for w in word_list:
        if w in word_count:
            word_count[w]+=1
        else:
            word_count[w]=1

    context={
        "word_count":word_count,
        "text":text,
        "total_word":len(word_list),
        "total_one":len(text),
        "noblank":len([i for i in text if i != ' ']),
    }

    return render(request,"result.html",context)

def about(request):

    return render(request,'about.html')