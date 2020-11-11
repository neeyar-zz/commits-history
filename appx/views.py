from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
import requests
from appx.models import Repository
from appx.models import Commits
from appx.forms import NameForm
from django.contrib.auth.decorators import permission_required


class Home(ListView):
    #showing data from Repository table
    model = Repository
    template_name = 'appx/repository_list.html'
    context_object_name = 'repos'  

#getting value from textarea
#adding repository only through admin
@permission_required('appx.add_repository', 'appx.add_commits', raise_exception=True)
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            repo_url = "https://api.github.com/repos/" + form['add'].value()
            r = requests.get(repo_url)
            com_url = "https://api.github.com/repos/" + form['add'].value() + "/commits"
            com_r = requests.get(com_url)

            if r.status_code == 200: #if page exists
                #saving repository info to Repository table
                repo_info = r.json()
                funa = repo_info.get("full_name")
                dscr = repo_info.get("description")
                date = repo_info.get("created_at")
                own = repo_info.get("owner", {}).get("login")
                urlx = repo_info.get("url")
                fn_for_check = funa


                com_info = com_r.json()
                com_full = com_info


                # doesn't save if entry already exists
                if Repository.objects.filter(full_name=fn_for_check).exists():
                    error = {}
                    error['error'] = "OBJECT ALREADY EXISTS"
                    return render (request, 'appx/repository_adding.html', error    )
                    
                else:
                    #saving repository info to Repository table
                    repo_save = Repository(full_name = funa, description = dscr, created_at = date[:-10], owner_login = own, url = urlx)
                    repo_save.save()

                    #saving commits history to Commits table
                    com_save = Commits(repo_full_name = funa, full = com_full)
                    com_save.save() 

                    #successfully 
                    success = {}
                    success["success"] = "SUCCESSFULLY"
                    success['form'] = form
                    return render (request, 'appx/repository_adding.html', success)
                 
            else: #if page was not found
                err = {}
                err["err"] = "ERROR: PAGE NOT FOUND"
                err['form'] = form
                return render(request, 'appx/repository_adding.html', err)

    else:
        form = NameForm()
    return render(request, 'appx/repository_adding.html', {'form': form})


#showing selected repository and his commits history
def download_view(request, pk: int) -> HttpResponse:
    repo = get_object_or_404(Repository, pk=pk)
    repo_context = {}
    repo_context["repo_context"] = repo
    
    commits = get_object_or_404(Commits, pk=repo.full_name)
    com_context= {} 
    com_context["com_context"] = commits
    
    # 2 in 1
    repo_context.update(com_context)

    return render(request, "appx/repository_download.html", repo_context)
