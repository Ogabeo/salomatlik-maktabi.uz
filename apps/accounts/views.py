from django.shortcuts import render, redirect
from django.contrib import messages
from apps.accounts.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View
from apps.accounts.forms import UserRegisterForm, UpdatePasswordForm, LoginForm, UpdateUserForm, ResetPasswordForm, CheckVerifyCodeForm
from .models import User, UserResetPasswordCode
from datetime import datetime
# Create your views here.

class UserRegisterView(View):
    form_class = UserRegisterForm
    def get(self, request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request, 'accounts/register.html', context)
    
    def post(self, request):
        user_form = self.form_class(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "tizimdan muvaffaqiyatli ro'yxatdan o'tdingiz...")
            return redirect("accounts:login")
            

        messages.error(request, "Tizimdan ro'yxatdan o'ta olmadingiz...")
        context ={
            "form":user_form,
        }
        return render(request, 'accounts/register.html', context)
    

class LoginView(View):
    form_class = LoginForm
    def get(self, request):
        form = self.form_class()
        context={
            'form':form
        } 
        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        user_form = self.form_class(data = request.POST)
        if user_form.is_valid():
            user = authenticate(request, email = user_form.cleaned_data['email'], password = user_form.cleaned_data['password'])
            if user is not None:
                print(user)
                login(request, user)
                messages.success(request, 'Siz tizimga muvaffaqiyatli kirdingiz...')
                return redirect("home:index")

            messages.error(request, "Login yoki parol noto'g'ri!!!")
            return render(request, "accounts/login.html", {'form': user_form})
        

        messages.error(request, user_form.errors)
        return render(request, "accounts/login.html", {'form': user_form})

class LogOutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Tizimdan muvaffaqiyatli chiqdingiz...')
        return redirect('home:index')

class UpdateUserView(View):
    form_class = UpdateUserForm
    def get(self , request):
        form = self.form_class(instance=request.user)
        context ={
            'form':form
        }
        return render(request, 'accounts/update.html', context )
    def post(self, request):
        user_form = self.form_class(data=request.POST, files=request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Muvaffaqiyatli yangilandi...')
            return redirect('home:index')
        
        messages.error(request, user_form.errors)
        return render(request, 'accounts/update.html', {'form':user_form})
    
class PasswordResetView(View):
    form_class = ResetPasswordForm
    def get(self, request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request, "accounts/password_reset_form.html", context)

class CheckVerifyCodeView(View):
    form_class = CheckVerifyCodeForm
    def get(self, request):
        form=self.form_class()
        context={
            'form':form
        }
        return render(request, 'accounts/password_reset_check_verify_code.html', context)
    def post(self, request, uuid):
        verify_form = self.form_class(request.POST)
        if not verify_form.is_valid():
            messages.error(request, verify_form.errors)
            return render(request, 'accounts/password_reset_check_verify_code.html', {'form':verify_form})
        code = verify_form.cleaned_data.get('code')
        verify_code=UserResetPasswordCode.objects.filter(id=uuid, expiration_time__gte=datetime.now(), is_confirmation = False, code=code).first()
        if not verify_code:
            messages.error(request, 'Kod noto\'g\'ri kiritildi yoki vaqti tugagan qaytadan urinib ko\'ring!!!')
            return render(request, 'accounts/password_reset_check_verify_code.html', {'form':verify_form})
        verify_code.is_confirmation=True
        verify_code.save()
        messages.success(request, 'kod to\'g\'ri kiritildi endi maxfiy kod kiriting:')
        return redirect("accounts:password_reset_confirm", uuid=uuid)
           
        
    