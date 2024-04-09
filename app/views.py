from django.shortcuts import render
from .models import Profile,Skill,About,Service,Project,Category,Blog
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.order_by('order')
    about = About.objects.last()
    offers = Service.objects.all()
    projects = Project.objects.all()
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    


    return render(request, 'index.html',
                   {"profile":profile,
                     'skills':skills,
                     'about': about,
                     'offers': offers,
                     'projects': projects,
                     'categories': categories,
                     'blogs': blogs
                     })

def portfolio_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    return render(request, "portfolio-details.html", {
       'project': project
       })


def single_blog_uchun(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    profile = Profile.objects.first()
    popular_posts = Blog.objects.order_by('-view_count')[:4]


    
    if request.method == 'POST':
        search = request.POST.get('search')
        blogs = blogs.filter(title__icontains= search)
        

    p = Paginator(blogs, 3)
    page_num = request.GET.get('page')
    try:
      blogs = p.get_page(page_num)
    except PageNotAnInteger:
      blogs = p.page(1)
    except EmptyPage:
      blogs = p.page(p.num_pages)

    return render(request, "single-blog.html", 
                  {'blog': blog,
                   "profile":profile,
                   'popular_posts': popular_posts
                   })



def blog(request):
    blogs = Blog.objects.all()

    popular_posts = Blog.objects.order_by('-view_count')[:4]



    if request.method == 'POST':
        search = request.POST.get('search')
        blogs = blogs.filter(title__icontains= search)
        

    p = Paginator(blogs, 3)
    page_num = request.GET.get('page')
    try:
      blogs = p.get_page(page_num)
    except PageNotAnInteger:
      blogs = p.page(1)
    except EmptyPage:
      blogs = p.page(p.num_pages)

    return render(request, 'blog.html',
                   {
                     'blogs': blogs,
                     'popular_posts': popular_posts

                     })


def about_me(request):
    about = About.objects.last()
    offers = Service.objects.all()
    skills = Skill.objects.order_by('order')

    return render(request, 'about-us.html',
                   {
                     'about': about,
                     'skills':skills,
                     'offers': offers
                     })

def portfolio(request):
    portfolio = Profile.objects.all()
    categories = Category.objects.all()

    return render(request, 'portfolio.html',
                   {
                     'portfolio': portfolio,
                     'categories': categories
                     })
