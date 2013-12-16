from flask import render_template, request, make_response
from app import app
import random

r = 0
red = 0
a = []

@app.route('/')
@app.route('/index')
def index(): 
    Secret = request.cookies.get('Secret')
    if Secret == None:
        print "none"
        Secret = []
        for i in range(1, 5):
            Secret.append(random.randrange(1, 9, 1))
        respEntry = make_response('boo')
        respEntry.set_cookie('Secret', str(Secret))
        print str(Secret)
        return respEntry, str(Secret), render_template("index.html",
        title = 'Home',
        )
    print str(Secret)
    print "YET"
    return render_template("index.html",
        title = 'Home',
        ), str(Secret)

    

def process_form()      
    Guess = request.form['Guess']
    Secret = request.cookies.get('Secret')
    print Secret
    print Guess
    red = 0
    white = 0
    r = 0
    red_place = [0,1,2,3] 
    white_place = [0,1,2,3] 
    
    guess = [int(c) for c in Guess]
    Secret2 = [int(Secret[1]),int(Secret[4]),int(Secret[7]),int(Secret[10])]
    a.append (guess)
  
    print guess
    # checking for the reds
    for i in range(0, 4):  
        print "vous"
        print guess[i]
        print Secret2[i]
        print a
        if guess[i] == Secret2[i]:
            print "yeah"
            print guess[i]
            print Secret2[i]
            red_place.remove(i)    
            white_place.remove(i)
            red = red + 1 
            print red
        if red == 4:
            respExit = make_response(render_template("index.html",
            title = 'Beanmind', first = " Yeah you're so good!"))
            respExit.set_cookie('Secret','', expires=0)
            return respExit
            print "toi"
                
    # checking for whites   
    for j in red_place:
        print "lui"
        for h in white_place:
            print"elle"
            print guess[j]
            print Secret2[h]
            if guess[j] == Secret2[h]: 
                white_place.remove(h)
                white = white + 1
                print"nous"
                break
            
    # result
    print red
    print white
    r = r + 1
    if red == 0 and white == 0:   
        return render_template("index.html",
        title = 'Beanmind', gu1= guess, red_num = red, white_num = white, first = " Ca m'est saucisson mais quand meme, t'es trop nul! You've got nothing. Try again"  )
    elif red == 0 and white == 1 or red==0 and white == 2:
        return render_template("index.html",
        title = 'Beanmind', first = " Das Leben ist kein Ponyhof, you've got",red_number = red, second ='red and',white_number = white, third = 'white', gu = guess )        
    elif red == 2:
        return render_template("index.html",
        title = 'Beanmind', first = " Getting better! You've got",red_number = red, second ='red and',white_number = white, third = 'white', gu = guess)
    elif red == 3:
        return render_template("index.html",
        title = 'Beanmind', first = " Almost. ALMOST! You've got",red_number = red, second ='red and',white_number = white,third ='white!', gu = guess)
    else:
        return render_template("index.html",
        title = 'Beanmind', first = " You've got",red_number = red,second ='red and',white_number = white,third ='white', gu = guess)
    