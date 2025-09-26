from django.shortcuts import render

from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list.html', context)

def post_detail(request,post_id):
    print("화면에서 전달 받은 상세 페이지 게시글 번호 post_id :", post_id)
    post = Post.objects.get(id=post_id)
    print(post)
    context = {
        # "post_id": post_id,
        "post": post
    }
    return render(request, 'post_detail.html',context)

# 1) 글 작성 화면,GET 2) 글 로직 처리,POST
def post_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        print(title)
        print(content)
    else:
        print("method GET")
    return render(request, 'post_add.html')






