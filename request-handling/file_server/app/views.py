import datetime
from os import listdir, stat
from django.shortcuts import render
from django.conf import settings

def createDict(file):
    data = {}
    data["name"] = file
    data["ctime"] = datetime.datetime.fromtimestamp(int(stat(f"{settings.FILES_PATH}/{file}").st_ctime))
    data["mtime"] = datetime.datetime.fromtimestamp(int(stat(f"{settings.FILES_PATH}/{file}").st_mtime))
    return data
 

def file_list(request, date = None):
    template_name = 'index.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    files = listdir(settings.FILES_PATH)
    parsedFiles = []
    if not date:
        for file in files:
            parsedFiles.append(createDict(file))
    else:
        for file in files:
            f_date = str(datetime.datetime.fromtimestamp(int(stat(f"{settings.FILES_PATH}/{file}").st_ctime)).date())
            if f_date == date:
                parsedFiles.append(createDict(file))
    context = {
            'files': parsedFiles,
            'date': date
        }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    files = listdir(settings.FILES_PATH)
    f_content = ""
    with open(f"{settings.FILES_PATH}/{name}", "r") as f:
        for line in f.readlines():
            f_content += line
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': f_content}
    )

