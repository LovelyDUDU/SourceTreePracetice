from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def main(request):
    blogs = Blog.objects
    return render(request, 'main.html', {'blogs':blogs})

def result(request):
    full_text = request.GET['totaltext']
    word_num = full_text.split() #안녕안녕
    word_dic = {}
    for word in word_num:
        if word in word_dic:
            word_dic[word] = word_dic[word] + 1 
        else:
            word_dic[word] = 1

    word_list = full_text.split()
    return render(request, 'result.html', {'total_text': full_text, 'total':len(word_list), 'dic' : word_dic.items()})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

