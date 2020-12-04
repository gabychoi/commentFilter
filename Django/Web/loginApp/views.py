from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.storage import FileSystemStorage
from .models import Signup, Photo, Comment_posting
from .forms import PhotoForm

# Create your views here.


def index(request):
    return render(request, 'loginApp/index.html')


def signup(request):
    if request.method == 'POST' :
        input_name        = request.POST['fullname']
        input_email       = request.POST['email']
        input_password    = request.POST['passsword']
        input_re_password = request.POST['re_passsword']

        print(input_re_password)
        print(input_password)

        if input_password != input_re_password:
            error = '비밀번호가 일치하지 않습니다'
            return render(request, "loginApp/index.html", {'error' : error})

        else :
            database = Signup(user_email = input_email, user_pwd = make_password(input_password), user_name = input_name)
            database.save()
            return HttpResponseRedirect(reverse('index'))


def login(request):
    context= {}
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('index'))
    elif request.method == 'POST':
        input_email = request.POST['email']
        input_password = request.POST['pwd']

        if not (input_email and input_password):
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요'
        else :
            user_db = Signup.objects.get(user_email = input_email)
            if check_password(input_password, user_db.user_pwd) :
                request.session['user_name'] = user_db.user_name
                context['name'] = request.session['user_name']
                return redirect('photo_list')
            else :
                context['error'] = '비밀번호를 틀렸습니다.'
                return render(request, 'loginApp/index.html', context)


def posting(request):
    context = {}
    if request.method == 'POST':
        author         = request.session['user_name']
        comment        = request.POST['comment']
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()

        # 이미지 파일의 경로를 저장해줌
        name = fs.save(uploaded_image.name, uploaded_image)
        image_url = fs.url(name)

        Photo.objects.create(
            author=author,
            comment=comment,
            image=image_url
        )

        # DB = Photo(author  = author,
        #            comment = comment,
        #            image   = image_url)
        # DB.save()

        context['image_url'] = image_url
        context['user_name'] = author
        context['comment']   = comment
    return redirect('photo_list')



def photo_list(request):
    photo_lists = Photo.objects.all()[0:5]
    pk_num_list = [post.pk_num for post in photo_lists]

    for a in photo_lists:
        print(type(a))
        print(a)

    comment_list = Comment_posting.objects.all()
    user_name = request.session['user_name']


    for a in comment_list:
        print(a.post)

    context = {
        'user_name'    : user_name,
        'post_lists'   : photo_lists,
        'comment_list' : comment_list,
        'pk_num_list'  : pk_num_list
    }
    return render(request, 'loginApp/home.html', context)



def comment_posting(request):
    if request.method == 'POST':
        pk_num = request.POST['pk_num']
        current_id = request.session['user_name']
        comment_content = request.POST['comment']

    DB = Comment_posting(post       = pk_num,
                         comment_id = current_id,
                         comment    = comment_content)

    DB.save()
    return redirect('photo_list')





def comment_list(request):
    pass

