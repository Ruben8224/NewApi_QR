import graphene
from graphene_django import DjangoObjectType

from .models import Game


class GameType(DjangoObjectType):
    class Meta:
        model = Game


class Query(graphene.ObjectType):
    games = graphene.List(GameType)

    def resolve_games(self, info, **kwargs):
        return Game.objects.all()


class CreateGame(graphene.Mutation):
    id = graphene.String()
    juego = graphene.String()
    fecha_de_lanzamiento = graphene.String()
    descripcion = graphene.String()
    tipo = graphene.String()
    creador = graphene.String()
    personajes = graphene.String()
    enemigos = graphene.String()
    precio = graphene.Int()
    musica = graphene.String()
    version = graphene.String()
    matricula = graphene.String()
    carrera = graphene.String()

    class Arguments:
        juego = graphene.String()
        fecha_de_lanzamiento = graphene.String()
        descripcion = graphene.String()
        tipo = graphene.String()
        creador = graphene.String()
        personajes = graphene.String()
        enemigos = graphene.String()
        precio = graphene.Int()
        musica = graphene.String()
        version = graphene.String()
        matricula = graphene.String()
        carrera = graphene.String()

    # 3
    def mutate(self, info, juego, fecha_de_lanzamiento, descripcion, tipo, creador, personajes, enemigos, precio, musica, version, matricula, carrera):
        game = Game(juego=juego, fecha_de_lanzamiento=fecha_de_lanzamiento,
                    descripcion=descripcion,
                    tipo=tipo,
                    creador=creador,
                    personajes=personajes,
                    enemigos=enemigos,
                    precio=precio,
                    musica=musica,
                    version=version,
                    matricula=matricula,
                    carrera=carrera
                    )
        game.save()  # insert into Game(...) values(...)
        return CreateGame(
            id=game.id,
            juego=game.juego,
            fecha_de_lanzamiento=game.fecha_de_lanzamiento,
            descripcion=game.descripcion,
            tipo=game.tipo,
            creador=game.creador,
            personajes=game.personajes,
            enemigos=game.enemigos,
            precio=game.precio,
            musica=game.musica,
            version=game.version,
            matricula=game.matricula,
            carrera=game.carrera
        )


# 4
class Mutation(graphene.ObjectType):
    create_game = CreateGame.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
