from django.shortcuts import render

# Create your views here.

def main(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request,'main.html', _context)


# def login(request):
#     return render(request,'login.html')
    
# def register(request):
#     return render(request,'register.html')

def infoWrite(request):
    return render(request, 'infoWrite.html')

def survey(request):
    return render(request, 'survey.html')