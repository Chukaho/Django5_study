from django.http import HttpResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import redirect, render


# Create your views here.

def index(request):
    return render(request, "http.html")


def index0(request):
    return redirect("/static/newpage.html", permanent=True)
    # 重定向响应设置,permanent参数为是否永久，如果使用永久，以后的响应会用新的URL，否则还是沿用旧的。


'''
永久重定向的优点：
SEO优化： 搜索引擎会将永久重定向视为资源已经永久移动到新的位置，搜索引擎会更新索引以反映新的URL。这有助于保持网站的搜索引擎优化（SEO）和排名。
书签和链接： 浏览器会记住永久重定向的新URL，用户的书签和其他站点链接也会被更新，因此用户访问原始URL时会自动重定向到新的URL。
缓存处理： 浏览器和代理服务器会缓存永久重定向的响应，这可以减少对服务器的请求，提高网站性能。

永久重定向的缺点：
不灵活： 一旦设置了永久重定向，浏览器会缓存这个重定向，即使您以后想要更改重定向目标，用户仍然会被强制重定向到原始URL。这可能导致某些用户无法访问新的目标页面。
临时重定向的优点：
灵活性： 临时重定向可以随时更改或移除，因为浏览器不会缓存重定向，用户每次访问时都会发送新的请求并根据服务器返回的重定向响应进行处理。
临时重定向的缺点：
SEO不利： 搜索引擎不会将临时重定向视为资源已经移动，而是视为原始URL仍然有效，并可能在未来返回。这可能会导致搜索引擎排名不稳定或下降。
不利于性能： 由于浏览器不会缓存临时重定向，每次请求都需要从服务器获取重定向响应，这可能会增加服务器负载和页面加载时间。
'''


def index1(request):
    # 从数据库或其他地方获取数据
    my_data = {
        'name': 'John',
        'age': 30,
        'city': 'New York',
    }
    # 将数据存储在context字典中
    context = {
        'data': my_data,
        'message': 'Welcome to our website!!'
    }
    return render(resquest, 'helloworld/index.html', context=context)


'''
在调用render函数时，您可以将要传递给模板文件的数据存储在一个字典中，然后将该字典作为 context 参数传递给 render 函数。
在模板文件中，您可以通过访问字典的键来获取这些数据，并将其用于渲染模板。
'''

'''
return JsonResponse({'foo': 'bar'})             # 返回Json格式响应
return HttpResponseNotFound()                   # 返回404格式响应

html = "<font color='red'>Hello World</font>"   # 返回Http格式响应
return HttpResponse(html)
'''


def blog(request, id):
    if id == 0:
        return redirect("/static/error.html")
    else:
        return HttpResponse("This is " + str(id) + " ID's Blog ")


def blog2(request, year, month, day):
    return HttpResponse(str(year) + "/" + str(month) + "/" + str(day) + " 's Blog'")


file_path = "D:\\Bcut.exe"


def download(request):
    file = open(file_path, "rb")
    response = HttpResponse(file)
    response['Content_Type'] = 'application/octet-stream'
    # 指定文件类型
    '''
    Content-Type： 这个头字段指定了响应主体数据的类型。
    在这段代码中，设置了 Content-Type 为 application/octet-stream。
    这个 MIME 类型是一个通用的二进制流类型，它告诉客户端接收到的数据是二进制数据而非特定格式的文本。
    浏览器通常不会尝试直接展示这样的数据，而是会提示用户下载或者使用相关应用程序打开
    '''

    response['Content-Disposition'] = 'attachment;filename=file.exe'
    # 附件已附件下载并重新命名
    '''
    attachment 表示将文件作为附件下载，而不是在浏览器中直接打开。
    filename=file.exe 则指定了客户端保存文件时的默认文件名为 file.exe。
    '''

    return response


def st_download(request):
    file = open(file_path, "rb")
    response = StreamingHttpResponse(file)
    # Streaming流式文件传输（大文件）
    '''
    StreamingHttpResponse构造函数将文件内容作为可流式传输的内容来处理。
    对于大型文件或者需要逐步生成的内容非常有用，因为它允许服务器在准备数据时就开始向客户端发送数据，而不需要等待整个响应体完全准备好。
    '''
    response['Content_Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=file_st.exe'
    return response


def file_download(request):
    file = open(file_path, "rb")
    response = FileResponse(file)  # 普通文件传输（大文件）
    response['Content_Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=file_File.exe'
    return response


def get_test(request):  # get请求测算
    print(request.method)
    print(request.GET.get("name"))  # 获取页面参数，填写参数的key值
    print(request.GET.get("pwd"))
    print(request.GET.get("aaa", 222))  # 页面没有的参数，默认输入None，第二个参数可以指定默认的参数
    return HttpResponse("http get ok")


def post_test(request):  # get请求测算
    print(request.method)
    print(request.POST.get("name"))  # 获取页面参数，填写参数的key值
    print(request.POST.get("password"))
    print(request.POST.get("aaa", 222))  # 页面没有的参数，默认输入None，第二个参数可以指定默认的参数
    return HttpResponse("http post ok")
