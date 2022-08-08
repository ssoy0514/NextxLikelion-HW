from unicodedata import category
from urllib import request
from django.shortcuts import render,redirect
from .models import Link, Category
from django.views.generic import CreateView, UpdateView, TemplateView
# from .forms import AddLinkModelForm, AddCategoryForm
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.
def AddCategoryView(request):
    if request.method == 'POST':
        category = Category.objects.create(
            name = request.POST['name']
        )
        return JsonResponse({'msg': "생성완료"})
    
def AddLinkView(request):
    if request.method == 'POST':
        link = Link.objects.create(
            link = request.POST['link'],
            link_name = request.POST['link_name'],
            category = request.POST['category'],
            memo = request.POST['memo'],
        )
        return JsonResponse({'msg': "link 생성완료"})
    
# class AddLinkModelView(CreateView):
#     model = Link
#     form_class = AddLinkModelForm 
#     template_name = 'main.html'
#     success_url = reverse_lazy('LinkTree')
#카테고리 별로 리스트 뽑을 수 있게    
def main(request):
    links = Link.objects.all()
    categories = Category.objects.all()
    return render(request, "main.html", {'links':links, 'categories': categories})

#카테고리 db 저장
# def newcat(request):
#     if request.method == 'POST':
#         category = Category()
#         category.name = request.POST['name']
#         category.save()
#         return redirect('category')
#     else:
#         category = Category.objects.all()
#         return render(request, 'main.html', {'category':category})

#한번에 합쳐주고 싶었는데 실패 form 2개로 나누어야 함
# class MainView(TemplateView):
    
#     def form_save(self, form):
#         obj = form.save()
#         return obj
    
#     form_category = AddCategoryForm
#     form_link = AddLinkModelForm
#     template_name = 'main.html'
    
#     def newpost(self, request):
#         post_data = request.POST or None
#         post_cat = self.form_category(post_data, prefix="category") 
#         post_link = self.form_link(post_data, prefix="link")   
        
#         context = self.get_context_data(post_cat = post_cat,
#                                         post_link = post_link)
        
#         if post_cat.is_valid():
#             self.form_save(post_cat)
#         if post_link.is_valid():
#             self.form_save(post_link)
            
#             return self.render_to_response(context)
        
        
#         def main(request):
#             links = Link.objects.all()
#             categories = Category.objects.all()
#             return render(request, "main.html", {'links':links, 'categories': categories})
    
    
     