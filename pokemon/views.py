from django.shortcuts import render, redirect
import pandas as pd
import sqlite3

# Create your views here.
def home(request):
    return render(request, 'home.html')


def pokefeaname(request):
    if request.method == "POST":
        pokemon_name = request.POST.get('pokemon-name')
        pokemon_name = pokemon_name.title()
        # sqlite3 query
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("SELECT * FROM pokemon WHERE Name=?", (pokemon_name,))
        names = c.fetchall()
        conn.commit()
        conn.close()
        
        if len(names) == 0:
            return render(request, "pokemon.html", {"value":0})
        else:
            for name in names:
                dict = {"Name": name[2], "Type1": name[3], "Type2": name[4], "Total": name[5], "HP": name[6], "attack": name[7],
                        "defence": name[8], "S_A": name[9], "S_D": name[10], "speed": name[11], "generation": name[12], "legendary": name[13]}
            return render(request, "pokemon.html", dict)
    return redirect("/")

def pokefea(request):
    if request.method=="POST":
        type=request.POST.get('pokfea')
        type=type.title()
        list=[]
        conn=sqlite3.connect('db.sqlite3')
        c=conn.cursor()
        c.execute("SELECT * FROM pokemon WHERE Type1=?",(type,))
        poke=c.fetchall()
        for i in poke:
            list.append(i[2])
        conn.commit()
        conn.close()
        type=type.upper()
    return render(request,'pokesearch.html',{"type": type,"list":list})



def upload(request):
    conn = sqlite3.connect('db.sqlite3')
    df = pd.read_excel(r"pokemon.csv")
    df.to_sql(con=conn, name='pokemon', if_exists='append')
    conn.commit()
    conn.close()
    return render(request, 'home.html')
