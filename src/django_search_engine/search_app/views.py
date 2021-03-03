from .web_search import WebSearch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views import View

# Create your views here.
# def index(request):
#     return render(request, 'search_app/index.html')


# def search(request):
#     search_text = request.GET.get('search_text')
#     websearch = WebSearch(search_text)
#     results = websearch.get_search_result()
#     print(results)
#     context = {
#         'object_list': results,
#     }
#     return render(request, 'search_app/search.html', context)        


class Home(View):
	"""Home View"""
	def get(self, request):

		context = {}

		return render(request, 'search_app/index.html', context)


class Search(View):
	def get(self, request):
		template_name = 'search_app/search.html'
		form_search_text = request.GET.get('search_text', None)
		if form_search_text:
			try:
				""" if request data == session data"""
				request_search_text = request.session['search_text']
				request_search_results = request.session['search_results']
				if(request_search_text==form_search_text):
					context = self.get_paginated_results(request_search_results, request_search_text)
					return render(request, 'search_app/search.html', context)
				else:
					#""" if request data != session data"""
					context =self.get_results(form_search_text)
					return render(request, 'search_app/search.html', context)
                    
			except Exception as AttributeError:
				# on session error, no data in session 
				context = self.get_results(form_search_text)
				return render(request, 'search_app/search.html', context)

		else:
			pass
		return render(request, 'search_app/search.html', {}) 		

	def get_paginated_results(self, data, search_text):
		""" get paginated list from search results"""
		page = self.request.GET.get('page', 1) # get page number
		paginator = Paginator(data, 10) # return 10 results

		try:
			object_list = paginator.page(page)
		except PageNotAnInteger:
			object_list = paginator.page(1)
		except EmptyPage:
			object_list = paginator.page(paginator.num_pages)

		context = {'object_list': object_list, 'search_text': search_text}
		return context


	def get_results(self, form_search_text):
		""" process search"""
		websearch = WebSearch(form_search_text).get_search_result()
		self.request.session['search_results'] = websearch
		self.request.session['search_text'] = form_search_text
		return self.get_paginated_results(websearch, form_search_text)



