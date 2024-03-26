from django.urls import path
from FootballApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView, name="Home" ),
    path('SobreMi/', AboutView, name="About" ),


    ##Usuario

    path('signin/', SignIn, name="SignIn"),
    path('signup/', SignUp, name="SignUp"),
    path('logout/', SignOut, name="Logout"),
    path('editar/', UserEdit, name="EditarUsuario"),
    path('password/', PassEdit.as_view(), name="CambiarContra"),
    path('image/', AddAvatar, name="AgregarAvatar"),

    
    
    
    ##CRUD Player

    path('VerJugadores/', PlayerList.as_view(), name="ListaJugadores"),
    path('CrearJugador/', PlayerCreate.as_view(), name="CrearJugadores"),
    path('EditarJugador/<int:pk>', PlayerUpdate.as_view(), name="EditarJugadores"),
    path('EliminarJugador/<int:pk>', PlayerDelete.as_view(), name="EliminarJugadores"),
    path('DetalleJugador/<int:pk>', PlayerDetail.as_view(), name="DetalleJugadores"),
    
    path('BuscarJugador/', SearchPlayer, name="BuscarJugador"),



    ##CRUD Team

    path('VerEquipos/', TeamList.as_view(), name="ListaEquipos"),
    path('CrearEquipo/', TeamCreate.as_view(), name="CrearEquipos"),
    path('EditarEquipo/<int:pk>', TeamUpdate.as_view(), name="EditarEquipos"),
    path('EliminarEquipo/<int:pk>', TeamDelete.as_view(), name="EliminarEquipos"),
    path('DetalleEquipo/<int:pk>', TeamDetail.as_view(), name="DetalleEquipo"),

    path('BuscarEquipo/', SearchTeam, name="BuscarEquipo"),



    ##CRUD League

    path('VerLigas/', LeagueList.as_view(), name="ListaLigas"),
    path('CrearLiga/', LeagueCreate.as_view(), name="CrearLigas"),
    path('EditarLiga/<int:pk>', LeagueUpdate.as_view(), name="EditarLigas"),
    path('EliminarLiga/<int:pk>', LeagueDelete.as_view(), name="EliminarLigas"),
    path('DetalleLiga/<int:pk>', LeagueDetail.as_view(), name="DetalleLiga"),

    path('BuscarLiga/', SearchLeague, name="BuscarLiga"),


    ##CRUD Tourn
    path('VerTorneos/', TournList.as_view(), name="ListaTorneos"),
    path('CrearTorneo/', TournCreate.as_view(), name="CrearTorneos"),
    path('EditarTorneo/<int:pk>', TournUpdate.as_view(), name="EditarTorneos"),
    path('EliminarTorneo/<int:pk>', TournDelete.as_view(), name="EliminarTorneos"),
    path('DetalleTorneo/<int:pk>', TournDetail.as_view(), name="DetalleTorneos"),

     path('BuscarTorneo/', SearchTourn, name="BuscarTorneo"),

]
