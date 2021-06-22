from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlockUser
from .forms import BlockUserForm

from django.views import View

class UserBlockView(LoginRequiredMixin,View):

    def post(self,request,pk,*args,**kwargs):

        blockusers  = BlockUser.objects.filter(from_user=request.user.id,to_user=pk)

        #すでにある場合は該当レコードを削除、無い場合は挿入
        #TIPS:↑メソッドやビュークラスを切り分けてしまうと、多重に中間テーブルへブロックのレコードが挿入されてしまう可能性があるため1つのメソッド内で分岐するやり方が無難。
        if blockusers:
            print("ある")
            blockusers.delete()

            return redirect("/")

        else:
            print("無い")

        data    = { "from_user":request.user.id,"to_user":pk }
        form    = BlockUserForm(data)

        if form.is_valid():
            print("ブロックOK")
            form.save()

        else:
            print("ブロックNG")

        return redirect("/")


block   = UserBlockView.as_view()


