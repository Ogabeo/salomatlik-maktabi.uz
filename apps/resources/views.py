from django.shortcuts import render
from apps.resources.models import Category, Resource, ResourceType
from django.views.generic import ListView, DetailView
from django.db.models import Q 
from django.core.paginator import Paginator
# Create your views here.


class ResourceListView(ListView):
    model = Resource
    template_name = 'resources.html'
    context_object_name = 'resources'
    paginate_by = 8
    PAGINATION_URL = ''

    def get_queryset(self):
        queryset = Resource.objects.filter(is_active=True)  # Base queryset

        # Get search query from request.GET (modify as needed)
        search_query = self.request.GET.get('search', '')
        if search_query:
            self.PAGINATION_URL = f'&search={search_query}'  
            queryset = queryset.filter(Q(title__icontains=search_query) | 
                                       Q(description__icontains=search_query) | 
                                       Q(author__icontains=search_query) | 
                                       Q(keywords__icontains=search_query))

        # Add additional filters based on request.GET parameters (modify as needed)
        filter_by_category = self.request.GET.get('category', '')
        if filter_by_category:
            self.PAGINATION_URL += f'&category={filter_by_category}'  
            queryset = queryset.filter(category__slug=filter_by_category)
            
            
        filter_by_type = self.request.GET.get('resourceType', '')
        if filter_by_type:
            self.PAGINATION_URL += f'&resourceType={filter_by_type}'
            queryset = queryset.filter(resource_type=filter_by_type)
            
            
        filter_by_auditoriya = self.request.GET.get('auditoria', '')
        if filter_by_auditoriya:
            self.PAGINATION_URL += f'&auditoria={filter_by_auditoriya}'
            queryset = queryset.filter(auditoria=filter_by_auditoriya)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resourceTypes'] = ResourceType.objects.all()
        context['search_query'] = self.request.GET.get('search', '')  # Pass search query to template
        context['filter_by_category'] = self.request.GET.get('category', '')  # Pass filter value to template
        context['filter_by_type'] = self.request.GET.get('resourceType', '')  
        context['filter_by_auditoriya'] = self.request.GET.get('auditoria', '') 
        context['pagination_url'] = self.PAGINATION_URL
        
        
        # Get paginated queryset
        resources = self.object_list
        paginator = Paginator(resources, self.paginate_by)
        page_number = self.request.GET.get('page', 1)  # Get current page from GET
        page_obj = paginator.get_page(page_number)

        # Update context with pagination information
        context['page_obj'] = page_obj
        context['is_paginated'] = paginator.num_pages > 1

        return context
    
class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'resource_detail.html'
    context_object_name = 'resource'
    lookup_field = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mostResources'] = Resource.objects.filter(category=self.object.category).exclude(id=self.object.id).order_by('?')[:4]
        context['tg_link'] = f"https://t.me/share/url?url={self.request.build_absolute_uri()}&text={self.object.title}"
        context['copy_link'] = f"{self.request.build_absolute_uri()}"
        return context