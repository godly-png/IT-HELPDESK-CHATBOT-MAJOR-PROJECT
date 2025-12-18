from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from .forms import RegisterForm, LoginForm
from .models import Ticket
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def chat_history(request):
    return render(request, 'chat_history.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# ---------------- HOME PAGE ----------------
@login_required
def home(request):
    return render(request, 'home.html')


# ---------------- LOGIN ----------------
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("login")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})




# def home(request):
#     if request.method == "POST":
#         subject = request.POST.get("subject")
#         description = request.POST.get("description")
#         if subject and description:
#             Ticket.objects.create(
#                 user=request.user,
#                 subject=subject,
#                 description=description
#             )
#             return redirect('home')  # reload home page after creating ticket

#     # Get all tickets of the logged-in user to show on home page
#     tickets = Ticket.objects.filter(user=request.user)
#     return render(request, "home.html", {"tickets": tickets})



# ---------------- LOGOUT ----------------
def logout_user(request):
    logout(request)
    return redirect("login")


# ---------------- REGISTER ----------------
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        # Check if email exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("register")

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()

        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "register.html")


# ---------------- CHATBOT PAGE ----------------
@login_required
def chatbot_page(request):
    return render(request, "chat.html")


# ---------------- TICKET CREATE ----------------
@login_required
def ticket_create(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        description = request.POST.get("description")
        if subject and description:
            Ticket.objects.create(
                user=request.user,
                subject=subject,
                description=description
            )
            return redirect('ticket_list')
    return render(request, "ticket_create.html")


# ---------------- TICKET LIST ----------------
@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'ticket_list.html', {'tickets': tickets})


# ---------------- TICKET DETAIL ----------------
@login_required
def ticket_detail(request, id):
    ticket = get_object_or_404(Ticket, id=id, user=request.user)
    return render(request, "ticket_detail.html", {"ticket": ticket})


# from django.shortcuts import render

# def chatbot_page(request):
#     response = ""
#     if request.method == "POST":
#         user_input = request.POST.get("user_input")
        
#         # --- Placeholder chatbot logic ---
#         # Replace this with your actual AI/chatbot processing
#         if user_input:
#             response = f"You said: {user_input}"
#         else:
#             response = "Please enter a message."

#     return render(request, 'myapp/chat.html', {'response': response})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def chatbot_page(request):
    response = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            # Placeholder bot logic; replace with real AI logic if needed
            response = f"You said: {user_input}"
        else:
            response = "Please enter a message."

    return render(request, 'myapp/chat.html', {'response': response, 'user_input': user_input})




