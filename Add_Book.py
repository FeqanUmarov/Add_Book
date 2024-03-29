books=[]
def help():
    while True:
        print("--------------------------------------------------------")
        print("""Kitab elave etmek:1 Melumatlari goster: 2""")


        process = int(input("Emeliyyati secin:"))
        print("--------------------------------------------------------")


        run(process)

def kitab_melumatlari():
    info=dict()

    while True:
        book_name = input("Kitabin adini daxil edin:")
        if regular(book_name) and space_name(book_name):
            break
        else:
            print("Siz ancaq string melumat daxil ede bilersiz!")

    while True:
        try:
            price_of_book = int(input("Kitabin qiymetini daxil edin:"))
            break
        except ValueError:
            print("------------------------------------------")
            print("Kitabin qiymetini daxil edin!")
            print("------------------------------------------")

    while True:
        try:
            page_of_book = int(input("Kitabin sehife sayi:"))
            break

        except ValueError:
            print("------------------------------------------")
            print("Kitabin sehifesini daxil edin!")
            print("------------------------------------------")

    while True:
        type_of_book = input("Kitab hansi janrdadi?:")
        if janr_yoxlama(type_of_book):
            break

    info["ad"]=book_name
    info["qiymet"]=price_of_book
    info["sehife"]=page_of_book
    info["janr"]=type_of_book

    melumatlari_yerlesdir(info)

def regular(book_name):
    if book_name.isnumeric():
        return False
    else:
        return True
def space_name(book_name):
    if len(book_name)!=0:
        return True
def janr_yoxlama(type_of_book):
    if type_of_book!="":
        return True
    else:
        print("------------------------------------------")
        print("Kitabin Janirini daxil edin!")
        print("------------------------------------------")

def melumatlari_yerlesdir(info):
    books.append(info)

def melumatari_goster():
    for s in books:
        print("------------------------------------------------")
        for key,value in s.items():

            print(key,value,sep=":",end="\n")

def run(process):
    if process==1:
        kitab_melumatlari()
    if process==2:
        melumatari_goster()

help()

