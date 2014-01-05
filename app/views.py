from flask import render_template, request, make_response
from app import app
import random

#ajouter condition r<9

#def add_two_numbers(a, b):
 #   return a + b
 
      

def string_to_list(Thestring):     
    Thestring = [int(c) for c in Thestring]    
    return Thestring

def list_to_string(Thelist):   
    Thelist = ''.join(map(str,Thelist))
    return Thelist

#def string_to_listOfList(Thelist):
#    Thelist = map(int, (Thelist.replace('[', '').replace(']', '')).split(","))
#   return Thelist

def list_to_string2(Thelist):
    Thelist = ','.join(map(str,Thelist))
    #Thelist = map(str,Thelist)
    return Thelist

def string2_to_list(Thestring2):
    Thestring2 = map(int,Thestring2.split(","))
    return Thestring2
    
@app.route('/')
@app.route('/index', methods = ['POST', 'GET'])
def index(): 
    
    #setting red, white, round r, list_guess and secret
    red = request.cookies.get('red')
    if red == None:
        red = 0
    white = request.cookies.get('white') 
    if white == None:
        white = 0
    list_guess = request.cookies.get('list_guess')
    if list_guess == None:
        #list_guess = ['','','','','','','','','','']
        list_guess = [0,0,0,0,0,0,0,0,0,0]
    r = request.cookies.get('r')
    if r == None:
        r = 0
    print list_guess
    print "boo"
    Secret = request.cookies.get('Secret')
    if Secret == None:
        print "none"
        Secret = []
        for i in range(1, 5):
            Secret.append(random.randrange(1, 9, 1))
        respEntry = make_response(render_template("index.html",
            title = 'Home',
        ))
        
        respEntry.set_cookie('Secret',  list_to_string(Secret))
        respEntry.set_cookie('red', str(red))
        respEntry.set_cookie('white', str(white))
        respEntry.set_cookie('list_guess', list_to_string2(list_guess))
        respEntry.set_cookie('r', str(r))
        print list_to_string(Secret)
        return respEntry
        
    
    print str(red)
    
    print list_guess
    
    print "YET"
    
    
    
    # get cookies
    if request.method =='GET':
        return render_template("index.html",
            title = 'Home',
            )
        #resp = make_response(html)
        #return resp
        #    , str(Secret), str(red), str(white), str(list_guess), str(r)

    # get guess
    guess = request.form['Guess']
    
    print Secret
    print guess
 
    
    red_place = [0,1,2,3] 
    white_place = [0,1,2,3] 
    
            
    # transform format
    guess = string_to_list(guess)
    Secret = string_to_list(Secret)
    list_guess = string2_to_list(list_guess)
    red = int(red)
    white = int(white)
    r = int(r)
    print list_guess[0]
    print list_guess[1]
    print list_guess[2]
    print list_guess[3]
    print Secret
    print guess
    
    
    #list_guess= list_guess.replace(" ", "")
    #list_guess= list_guess.replace('[', '')
    #list_guess= list_guess.replace(']','')
    #list_guess= str(list_guess)
    #list_guess= list_guess.split(',')
    
    
    #list_guess = int(list_guess)
    #list_guess = [int(list_guess[1]), int(list_guess[4]), int(list_guess[7]), int(list_guess[10]), int(list_guess[13]), int(list_guess[16]), int(list_guess[19]), int(list_guess[22]), int(list_guess[25]), int(list_guess[28])]  
    #WORKS: list_guess = [list_guess[1], list_guess[4], list_guess[7], list_guess[10], list_guess[13], list_guess[16], list_guess[19], list_guess[22], list_guess[25], list_guess[28]] 
    #list_guess = [list_guess[1], list_guess[4], list_guess[7], list_guess[10], list_guess[13], list_guess[16], list_guess[19], list_guess[22], list_guess[25], list_guess[28]]    
    
    
    #list_guess= list_guess.split(',')    
    #list_guess= str(list_guess)
    #list_guess= list_guess.replace(" ", "")    
    
    #list_guess= 
    #list_guess= list_guess.split(',')
      
    
    # checking for the reds
    for i in range(0, 4):  
        print "vous"
        print guess[i]
        print Secret[i]
        
        if guess[i] == Secret[i]:
            print "yeah"
            print guess[i]
            print Secret[i]
            red_place.remove(i)    
            white_place.remove(i)
            red = red + 1 
            print red
        if red == 4:
            respExit = make_response(render_template("index.html",
                title = 'Beanmind', first = " Yeah you're so good!"))
            respExit.set_cookie('Secret','', expires=0)
            respExit.set_cookie('red', '', expires=0)
            respExit.set_cookie('white', '', expires=0)
            respExit.set_cookie('list_guess', '', expires=0)
            respExit.set_cookie('r', '', expires=0)
            return respExit
            
                
    # checking for whites   
    for j in red_place:
        print "lui"
        for h in white_place:
            print"elle"
            print guess[j]
            print Secret[h]
            if guess[j] == Secret[h]: 
                white_place.remove(h)
                white = white + 1
                print"nous"
                break
            
    # result
    print red
    print white
    list_guess[r] = int(list_to_string (guess))
    #list_guess[r] = "".join([str(c) for c in Guess])
    r = r + 1     
    print list_guess    
    
    if red == 0 and white == 0:   
        respExit = make_response (render_template("index.html",
        title = 'Beanmind', a1= list_guess[0], a2= list_guess[1], a3= list_guess[2], a4= list_guess[3], a5= list_guess[4], a6= list_guess[5], a7= list_guess[6], a8= list_guess[7], a9= list_guess[8], a10= list_guess[9], red_num = red, white_num = white, first = " Ca m'est saucisson mais quand meme, t'es trop nul! You've got nothing. Try again"  
        ))
        respExit.set_cookie('red', str(red))
        respExit.set_cookie('white', str(white))
        respExit.set_cookie('list_guess', list_to_string2(list_guess))
        respExit.set_cookie('r', str(r))
        return respExit
    elif red == 0 and white == 1 or red==0 and white == 2:
        respExit = make_response ( render_template("index.html",
        title = 'Beanmind', a1= list_guess[0], a2= list_guess[1], a3= list_guess[2], a4= list_guess[3], a5= list_guess[4], a6= list_guess[5], a7= list_guess[6], a8= list_guess[7], a9= list_guess[8], a10= list_guess[9],first = " Das Leben ist kein Ponyhof, you've got", second ='red and', third = 'white'  ))
        respExit.set_cookie('red', str(red))
        respExit.set_cookie('white', str(white))
        respExit.set_cookie('list_guess', list_to_string2(list_guess))
        respExit.set_cookie('r', str(r))
        return respExit
    elif red == 2:
        respExit = make_response ( render_template("index.html",
        title = 'Beanmind', first = " Getting better! You've got", second ='red and', third = 'white', a1= list_guess[0], a2= list_guess[1], a3= list_guess[2], a4= list_guess[3], a5= list_guess[4], a6= list_guess[5], a7= list_guess[6], a8= list_guess[7], a9= list_guess[8], a10= list_guess[9] ))
        respExit.set_cookie('red', str(red))
        respExit.set_cookie('white', str(white))
        respExit.set_cookie('list_guess', list_to_string2(list_guess))
        respExit.set_cookie('r', str(r))
        return respExit
    elif red == 3:        
        respExit = make_response ( render_template("index.html",
        title = 'Beanmind', first = " Almost. ALMOST! You've got", second ='red and',third ='white!' , a1= list_guess[0], a2= list_guess[1], a3= list_guess[2], a4= list_guess[3], a5= list_guess[4], a6= list_guess[5], a7= list_guess[6], a8= list_guess[7], a9= list_guess[8], a10= list_guess[9] ))
        respExit.set_cookie('red', str(red))
        respExit.set_cookie('white', str(white))
        respExit.set_cookie('list_guess', list_to_string2(list_guess))
        respExit.set_cookie('r', str(r))
        return respExit
    else:
        respExit = make_response ( render_template("index.html",
        title = 'Beanmind', first = " You've got",second ='red and',third ='white', a1= list_guess[0], a2= list_guess[1], a3= list_guess[2], a4= list_guess[3], a5= list_guess[4], a6= list_guess[5], a7= list_guess[6], a8= list_guess[7], a9= list_guess[8], a10= list_guess[9] ))
        respExit.set_cookie('red', str(red))
        respExit.set_cookie('white', str(white))
        respExit.set_cookie('list_guess', list_to_string2(list_guess))
        respExit.set_cookie('r', str(r))
        return respExit