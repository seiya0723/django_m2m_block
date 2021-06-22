from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from .models import Topic
from .forms import TopicForm


#HACK:これはいかがなものかと
#from users.models import BlockUser

class BbsView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        copied          = request.POST.copy()
        copied["user"]  = request.user.id



        form    = TopicForm(copied)
        if form.is_valid():
            print("OK")
            form.save()
        else:
            print("NG")


        return redirect("bbs:index")

index   = BbsView.as_view()

