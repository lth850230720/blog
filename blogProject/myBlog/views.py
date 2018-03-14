from django.shortcuts import render
from django.db.models import Max,Min,Count
# Create your views here.
from .models import Author,Tag,Category,BlogBook
from django.core.paginator import Paginator


def index(request,pageId=1):
    blog=BlogBook.objects.all()
    paginator=Paginator(blog,3)
    try:
        page=paginator.page(pageId)
    except:
        return render(request,'404.html')
    else:
        count=len(blog)
        return render(request, 'index.html',{'blogList':page,'item_count':count})

def about(request):
    return render(request,'about.html')

def divide(request):
    CategoryList=[]
    CategoryCloud={}
    CategoryQuery=Category.objects.all()
    for category in CategoryQuery:
        CategoryList.append(category.category_name)
    # print(len(tagList))
    for categoryName in CategoryList:
        CategoryCloud[categoryName]=len(BlogBook.objects.filter(category__category_name__exact=categoryName))
    return render(request,'divide.html',{'category_html':CategoryCloud,'category_count':len(CategoryList)})
    return render(request, 'divide.html')

def divide_blog_menu(request,category,pageId):
    print("1221")
    CategoryQuery=Category.objects.filter(category_name__exact=category)
    print(len(CategoryQuery))
    if(len(CategoryQuery)==0):
        return render(request,'404.html')
    else:
        BlogObjects=BlogBook.objects.filter(category__category_name__exact=category)
        paginator=Paginator(BlogObjects,3)
        page=paginator.page(int(pageId))
        print(page)
        itemCount=len(BlogObjects)
        return render(request,'divide_blog_menu.html',{'category_name':category,'item_count':itemCount,'blogList':page})
def tag(request):
    tagList=[]
    tagCloud={}
    tagQuery=Tag.objects.all()
    for tag in tagQuery:
        tagList.append(tag.tag_name)
    # print(len(tagList))
    for tagName in tagList:
        tagCloud[tagName]=len(BlogBook.objects.filter(tags__tag_name__exact=tagName))
    return render(request,'tag.html',{'tag_html':tagCloud,'tag_count':len(tagList)})
def resume(request):
    return render(request,'resume.html')

def tag_blog_menu(request,tag,pageId):
    tagQuery=Tag.objects.filter(tag_name__exact=tag)
    if(len(tagQuery)==0):
        return render(request,'404.html')
    else:
        BlogObjects=BlogBook.objects.filter(tags__tag_name__exact=tag)
        paginator=Paginator(BlogObjects,3)
        page=paginator.page(int(pageId))
        print(page)
        itemCount=len(BlogObjects)
        return render(request,'tag_blog_menu.html',{'tag_name':tag,'item_count':itemCount,'blogList':page})
    # print("asdasdadad")

def showBlog(request,num):
    blog=BlogBook.objects.get(pk=num)
    # print(blog.blog_body)
    return render(request,'blog.html',{'blog':blog})

def search(request):
    return render(request,'search.html')
#以下为各种测试函数
def a(request):
    return render(request,'a.html')

def test(request):
    return render(request,'test.html')
