from django.shortcuts import render

# Create your views here.

def home(request):
    # service section in the index,html ahmad
    services = [
        {
            'title': 'Web Devlopment',
            'description': 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi',
            'icon_class': 'bi-activity',
            'link': '#',
        },
        {
            'title': 'Sed ut perspici',
            'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore',
            'icon_class': 'bi-bounding-box-circles',
            'link': '#',
        },
        {
            'title': 'Magni Dolores',
            'description': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia',
            'icon_class': 'bi-calendar4-week',
            'link': '#',
        },
        {
            'title': 'Nemo Enim',
            'description': 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis',
            'icon_class': 'bi-broadcast',
            'link': '#',
        },
        
    ]
    
    # skill section in the index.html
    skills = [
        {'name': 'HTML', 'percentage': 100},
        {'name': 'CSS', 'percentage': 90},
        {'name': 'JavaScript', 'percentage': 75},
        {'name': 'Photoshop', 'percentage': 55},
    ]
    return render(request, 'index.html', {'services': services ,'skills' : skills })
