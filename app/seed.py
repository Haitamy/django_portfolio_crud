from django_seed import Seed
from .models import *

def runAbout():
	seeder = Seed.seeder()
	data = [
		{
      "desc1": "je suis une description",
      "desc2":"je suis une description",
      "bday": '27/07/2001', 
      "web": 'je suis un site web',
      'phone': 'je suis un numéro de tel',
      'city':'je suis une ville',
      'age':21,
      'deg':"je suis un niveau d'études",
      'mail':"je suis un mail",
      'dispo':"je suis dispo",
      "desc3":"je suis une description"
      },
	]
	for d in data:
		seeder.add_entity(About, 1, d)
	print(seeder.execute())
def runSkills():
	seeder = Seed.seeder()
	data = [
		{
      "name":'css',
      "level":100
      },{
      "name":'html',
      "level":100
      },{
      "name":'js',
      "level":20
      },
	]
	for d in data:
		seeder.add_entity(Skills, 1, d)
	print(seeder.execute())
def runServices():
	seeder = Seed.seeder()
	data = [
		{
      "titre":'css',
      "desc":'sdbjcmkjsdnblmj',
      'icon':'bi-briefcase'
      },{
      "titre":'html',
      "desc":'sdbjcmkjsdnblmj',
      'icon':'bi-card-checklist'
      },{
      "titre":'js',
      "desc":'sdbjcmkjsdnblmj',
      'icon':'bi-bar-chart'
      },
	]
	for d in data:
		seeder.add_entity(Services, 1, d)
	print(seeder.execute())
def runTesti():
	seeder = Seed.seeder()
	data = [
		{
      "name":'css',
      "job":'dev junior',
      'desc':'sdbjcmkjsdnblmj',
      'img':'testimonials-1.jpg'
      },{
      "name":'html',
      "job":'dev medior',
      'desc':'sdbjcmkjsdnblmj',
      'img':'testimonials-2.jpg'
      },{
      "name":'js',
      "job":'dev senior',
      'desc':'sdbjcmkjsdnblmj',
      'img':'testimonials-3.jpg'
      },
	]
	for d in data:
		seeder.add_entity(Testi, 1, d)
	print(seeder.execute())
def runCont():
	seeder = Seed.seeder()
	data = [
		{
      "loc":'place de la minoterie',
      'mail':'example@gmail.com',
      'phone':'0485 31 32 33'
      }
	]
	for d in data:
		seeder.add_entity(Cont, 1, d)
	print(seeder.execute())
def runFiltre():
	seeder = Seed.seeder()
	data = [
		{
      "filtre": 'filtreA'
      },
      {
      "filtre": 'filtreB'}
	]
	for d in data:
		seeder.add_entity(Filtre, 1, d)
	print(seeder.execute())
def runPorto():
	seeder = Seed.seeder()
	data = [
		{
      'img':'portfolio-1.jpg',
      "filtre": 'filtreA'
      },
      {
      'img':'portfolio-2.jpg',
      "filtre": 'filtreB'
      }
	]
	for d in data:
		seeder.add_entity(Porto, 1, d)
	print(seeder.execute())