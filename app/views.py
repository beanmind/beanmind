from flask import render_template, request, make_response
from app import app
import random

#ajouter condition r<9


 
      

def string_to_list(Thestring):     
    Thestring = [int(c) for c in Thestring]    
    return Thestring

def list_to_string(Thelist):   
    Thelist = ''.join(map(str,Thelist))
    return Thelist

def list_to_string2(Thelist):
    Thelist = ','.join(map(str,Thelist))
    #Thelist = map(str,Thelist)
    return Thelist

def string2_to_list(Thestring2):
    Thestring2 = map(int,Thestring2.split(","))
    return Thestring2

#def display_list_guess(list_guess):
#   a1= list_guess[0], a2= list_guess[1], a3= list_guess[2], a4= list_guess[3], a5= list_guess[4], a6= list_guess[5], a7= list_guess[6], a8= list_guess[7], a9= list_guess[8], a10= list_guess[9]
    
def set_cookies(respExit, r, list_guess, list_red, list_white):
    respExit.set_cookie('red', '', expires=0)
    respExit.set_cookie('white', '', expires=0)
    respExit.set_cookie('list_guess', list_to_string2(list_guess))
    respExit.set_cookie('list_red', list_to_string2(list_red))
    respExit.set_cookie('list_white', list_to_string2(list_white))
    respExit.set_cookie('r', str(r))
    
@app.route('/')
@app.route('/index', methods = ['POST', 'GET'])
def index(): 
    
    #setting red, white, round r, list_guess, list_red, list_white and secret
    red = request.cookies.get('red')
    if red == None:
        red = 0
    white = request.cookies.get('white') 
    if white == None:
        white = 0
    list_guess = request.cookies.get('list_guess')
    if list_guess == None:
        list_guess = [0,0,0,0,0,0,0,0,0,0]
    list_red = request.cookies.get('list_red')
    if list_red == None:
        list_red = [0,0,0,0,0,0,0,0,0,0]
    list_white = request.cookies.get('list_white')
    if list_white == None:
        list_white = [0,0,0,0,0,0,0,0,0,0]
    r = request.cookies.get('r')
    if r == None:
        r = 0
    print list_guess
    print list_red
    print list_white
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
        
        respEntry.set_cookie('Secret', list_to_string(Secret))
        respEntry.set_cookie('red', str(red))
        respEntry.set_cookie('white', str(white))
        respEntry.set_cookie('list_guess', list_to_string2(list_guess))
        respEntry.set_cookie('list_red', list_to_string2(list_red))
        respEntry.set_cookie('list_white', list_to_string2(list_white))
        respEntry.set_cookie('r', str(r))
        print list_to_string(Secret)
        return respEntry    
    
    print str(red)    
    print list_guess 
    print list_red
    print list_white
    
    print "YET"      
    
    # get cookies
    if request.method =='GET':
        return render_template("index.html",
            title = 'Home',
            )
        
    # get guess
    guess = request.form['Guess']
    if not guess.isdigit():
        return render_template("index.html",
        title = 'Home', check_guess = "Please read carefully! I said:"
        )
    if guess.isdigit() and int(guess) <1111 or int(guess) >= 8888:
        return render_template("index.html",
        title = 'Home', check_guess = "Please read carefully! I said"
        )
    
    
    print Secret
    print guess
     
    red_place = [0,1,2,3] 
    white_place = [0,1,2,3] 
                
    # transform format
    guess = string_to_list(guess)
    Secret = string_to_list(Secret)
    list_guess = string2_to_list(list_guess)
    list_red = string2_to_list(list_red)
    list_white = string2_to_list(list_white)
    red = int(red)
    white = int(white)
    r = int(r)
    
    print Secret
    print guess
    
    
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
            respExit.set_cookie('list_red', '', expires=0)
            respExit.set_cookie('list_white', '', expires=0)
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
    list_red[r] = red
    list_white[r] = white
    r = r + 1     
    print list_guess
    print list_red
    print list_white
    
    attempt_number = range(1,11)
    attempt_num = range(0,10)
    print attempt_number
    generalist = []
    for i in range(0,10):
        generalist.append([attempt_number[i], list_guess[i], list_red[i], list_white[i]])
        print generalist   
    
    if red == 0 and white == 0:   
        respExit = make_response(render_template("index.html",
        title = 'Beanmind',attempt_number = attempt_num, generalist = generalist, first = " Ca m'est saucisson mais quand meme, t'es trop nul! You've got nothing. Try again"  
        ))
        set_cookies(respExit, r, list_guess,list_red, list_white)
        return respExit
    elif red == 0 and white == 1 or red==0 and white == 2:
        respExit = make_response( render_template("index.html",
        title = 'Beanmind', attempt_number = attempt_num, generalist = generalist, first = " Das Leben ist kein Ponyhof, you've got", red_number = red, second ='red and', white_number = white, third = 'white.'  
        ))
        set_cookies(respExit, r, list_guess,list_red, list_white)
        return respExit
    elif red == 2:
        respExit = make_response ( render_template("index.html",
        title = 'Beanmind', attempt_number = attempt_num, generalist = generalist, first = " Getting better! You've got", red_number = red, second ='red and', white_number = white, third = 'white.'
        ))
        set_cookies(respExit, r, list_guess,list_red, list_white)
        return respExit
    elif red == 3:        
        respExit = make_response ( render_template("index.html",
        title = 'Beanmind', attempt_number = attempt_num, generalist = generalist, first = " Almost. ALMOST! You've got", red_number = red, second ='red and', white_number = white, third ='white!'        
        ))
        set_cookies(respExit, r, list_guess,list_red, list_white)
        return respExit
    else:
        respExit = make_response ( render_template("index.html",
        title = 'Beanmind', attempt_number = attempt_num, generalist = generalist, first = " You've got", red_number = red, second ='red and', white_number = white, third ='white.'
        ))
        set_cookies(respExit, r, list_guess,list_red, list_white)
        return respExit