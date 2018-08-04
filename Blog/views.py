from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	ListView,
	DeleteView
	)

# Create your views here.
from .forms import ArticleModelForm
from .models import Article


class ArticleCreateView(CreateView):
	template_name = 'Blog/article_create.html'
	form_class = ArticleModelForm
	queryset=Article.objects.all()

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)




class ArticleListView(ListView):
	template_name ='Blog/article_list.html'
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	template_name = 'Blog/article_detail.html'
	#queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')

		return get_object_or_404(Article,id = id_ )


class ArticleUpdateView(UpdateView):
	template_name = 'Blog/article_create.html'
	form_class = ArticleModelForm
	queryset=Article.objects.all()


	def get_object(self):
		id_ = self.kwargs.get('id')

		return get_object_or_404(Article,id = id_ )

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)


#delete_view


class ArticleDeleteView(DeleteView):
	template_name = 'Blog/article_delete.html'
	#queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')

		return get_object_or_404(Article,id = id_ )		

	def get_success_url(self):
		return reverse('articles:article-list')

