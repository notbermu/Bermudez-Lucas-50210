from django.shortcuts import render
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from FootballApp.models import *
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from FootballApp.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def HomeView(request):

    return render(request, "home.html")


def AboutView(request):

    return render(request, "about.html")


##Usuario

def SignIn(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
            usuario = authenticate(username=info["username"], password=info["password"])

            if usuario is not None:

                login(request, usuario)

                return render(request, "home.html", {"mensaje":f"Bienvenido {usuario}"})
            

        else:

            return render(request, "home.html", {"mensaje":"Error iniciando sesión"})

    else:

        formulario = AuthenticationForm()

    return render(request, "Usuario/sign_in.html", {"form":formulario})


def SignUp(request):

    if request.method == "POST":

        formulario = RegistroFormulario(request.POST)

        if formulario.is_valid():

            formulario.save()

            return render(request, "home.html", {"mensaje":"El usuario se ha creado exitosamente."})
        
    else:
            
        formulario = RegistroFormulario()


    return render(request, "Usuario/sign_up.html", {"form":formulario})

@login_required
def UserEdit(request):

    usuario = request.user
    
    if request.method == "POST":

        formulario = EditarFormulario(request.POST)
        
        if formulario.is_valid():

            info = formulario.cleaned_data
            
            usuario.username = info["username"]
            usuario.email = info["email"]
            usuario.first_name = info["first_name"]
            
            usuario.save()

            return render(request, "home.html")
        
    else:

        formulario = EditarFormulario(initial={
            "username": usuario.username,
            "email": usuario.email,
            "first_name": usuario.first_name
            })

    return render(request, "Usuario/user_edit.html", {"form":formulario, "usuario":usuario})


def SignOut(request):

    logout(request)

    return render(request, "home.html")


class PassEdit(LoginRequiredMixin, PasswordChangeView):
    form_class = PassForm
    template_name = "Usuario/password_edit.html"
    success_url = reverse_lazy("Home")

@login_required
def AddAvatar(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario_act = User.objects.get(username=request.user)

            new_avatar = Avatar(usuario = usuario_act, imagen = info["imagen"])

            new_avatar.save()

            return render(request, "home.html", {"mensaje": "Se ha creado un avatar"})
        
    else:

        formulario = AvatarFormulario()

    return render(request, "Usuario/new_avatar.html", {"form":formulario})








##Player

class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    template_name = "Players/player_create.html"
    fields = ["nombre", "posicion", "pais", "equipo"]
    success_url = reverse_lazy('ListaJugadores')

class PlayerList(LoginRequiredMixin, ListView):
    model = Player
    context_object_name = "Jugadores"
    template_name = "Players/player_list.html"

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model= Player
    template_name = "Players/player_update.html"
    fields = ["nombre", "posicion", "pais", "equipo"]
    success_url = reverse_lazy('ListaJugadores')


class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    template_name = "Players/player_delete.html"
    success_url = reverse_lazy('ListaJugadores')


class PlayerDetail(LoginRequiredMixin, DetailView):
    model = Player
    template_name = "Players/player_detail.html"



@login_required
def SearchPlayer(request):
    
    if request.GET:

        if request.GET["nombre"] != "":
            nombre = request.GET["nombre"]
            players = Player.objects.filter(nombre__icontains=nombre)
            message = f"Resultados de {nombre}"

            return render(request, "Players/player_search.html", {"players":players, "mensaje":message})
    
        else:
            message = "No buscaste nada"
            return render(request, "Players/player_search.html", {"mensaje":message})          
        
    
    return render(request, "Players/player_search.html")




##Team
    
class TeamList(LoginRequiredMixin, ListView):
    model = Team
    context_object_name = "Equipos"
    template_name = "Teams/team_list.html"

class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    template_name = "Teams/team_create.html"
    fields = ["nombre", "pais", "liga", "division"]
    success_url = reverse_lazy('ListaEquipos')

class TeamDetail(LoginRequiredMixin, DetailView):
    model = Team
    template_name = "Teams/team_detail.html"

class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    template_name = "Teams/team_update.html"
    fields = ["nombre", "pais", "liga", "division"]
    success_url = reverse_lazy('ListaEquipos')

class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    template_name = "Teams/team_delete.html"
    success_url = reverse_lazy('ListaEquipos')



@login_required
def SearchTeam(request):
    
    if request.GET:

        if request.GET["nombre"] != "":
            nombre = request.GET["nombre"]
            teams = Team.objects.filter(nombre__icontains=nombre)
            message = f"Resultados de {nombre}"

            return render(request, "Teams/team_search.html", {"teams":teams, "mensaje":message})
    
        else:
            message = "No buscaste nada"
            return render(request, "Teams/team_search.html", {"mensaje":message})          
        
    
    return render(request, "Teams/team_search.html")







##League
    
class LeagueList(LoginRequiredMixin, ListView):
    model = League
    context_object_name = "Ligas"
    template_name = "Leagues/league_list.html"

class LeagueCreate(LoginRequiredMixin, CreateView):
    model = League
    template_name = "Leagues/league_create.html"
    fields = ["nombre", "pais", "division"]
    success_url = reverse_lazy('ListaLigas')

class LeagueDetail(LoginRequiredMixin, DetailView):
    model = League
    template_name = "Leagues/league_detail.html"

class LeagueUpdate(LoginRequiredMixin, UpdateView):
    model = League
    template_name = "Leagues/league_update.html"
    fields = ["nombre", "pais", "division"]
    success_url = reverse_lazy('ListaLigas')

class LeagueDelete(LoginRequiredMixin, DeleteView):
    model = League
    template_name = "Leagues/league_delete.html"
    success_url = reverse_lazy('ListaLigas')


@login_required
def SearchLeague(request):
    
    if request.GET:

        if request.GET["nombre"] != "":
            nombre = request.GET["nombre"]
            leagues = League.objects.filter(nombre__icontains=nombre)
            message = f"Resultados de {nombre}"

            return render(request, "Leagues/league_search.html", {"leagues":leagues, "mensaje":message})
    
        else:
            message = "No buscaste nada"
            return render(request, "Leagues/league_search.html", {"mensaje":message})          
        
    
    return render(request, "Leagues/league_search.html")






##Tournament
    
class TournList(LoginRequiredMixin, ListView):
    model = Tourn
    context_object_name = "Torneos"
    template_name = "Tourns/tourn_list.html"


class TournCreate(LoginRequiredMixin, CreateView):
    model = Tourn
    template_name = "Tourns/tourn_create.html"
    fields = ["nombre", "equipos"]
    success_url = reverse_lazy('ListaTorneos')

class TournDetail(LoginRequiredMixin, DetailView):
    model = Tourn
    template_name = "Tourns/tourn_detail.html"

class TournUpdate(LoginRequiredMixin, UpdateView):
    model = Tourn
    template_name = "Tourns/tourn_update.html"
    fields = ["nombre", "equipos"]
    success_url = reverse_lazy('ListaTorneos') 

class TournDelete(LoginRequiredMixin, DeleteView):
    model = Tourn
    template_name = "Tourns/tourn_delete.html"
    success_url = reverse_lazy('ListaTorneos')



@login_required
def SearchTourn(request):
    
    if request.GET:

        if request.GET["nombre"] != "":
            nombre = request.GET["nombre"]
            tourns = Tourn.objects.filter(nombre__icontains=nombre)
            message = f"Resultados de {nombre}"

            return render(request, "Tourns/tourn_search.html", {"tourns":tourns, "mensaje":message})
    
        else:
            message = "No buscaste nada"
            return render(request, "Tourns/tourn_search.html", {"mensaje":message})          
        
    
    return render(request, "Tourns/tourn_search.html")