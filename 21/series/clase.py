import os
import re

class Serie:
    def __init__(self, link, title, runtime_se, certificate, runtime_ep, genre, rating, overview, star,start2,start3,start4, votes):
        self.link = link
        self.title = title
        self.runtime_serie = runtime_se
        self.certificate = certificate
        self.runtime_episode = runtime_ep
        self.genre = genre
        self.rating = rating
        self.overview = overview
        self.star = star
        self.star2 = start2
        self.star3 = start3
        self.star4 = start4
        self.votes = votes
    def __str__(self) -> str:
        return f'Titulo {self.title}, Link {self.link}, años desde-hasta o hasta solo: {self.runtime_serie}, Categoria {self.certificate}, duracion {self.runtime_episode}, Genero {self.genre}, Raiting {self.rating}, Resumen {self.overview}, Votos: {self.votes}'
    def str(self) -> str:
        return f'Titulo {self.title}, Link {self.link}, años desde-hasta o hasta solo: {self.runtime_serie}, Categoria {self.certificate}, duracion {self.runtime_episode}, Genero {self.genre}, Raiting {self.rating}, Resumen {self.overview}, Estrellas N1: {self.star} N2: {self.star2} N3: {self.star3} N4: {self.star4}, Votos: {self.votes}'

