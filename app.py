from flask import *
from whitenoise import WhiteNoise 

app = Flask(__name__)  #INSTANTIATE FLASK APP

#for this wsgi static code i didnt download the sample files on repo so it wont work.
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/", prefix="static/", #wsgi is a protocol that's commonly used for different network oriented apps to communicate w each other.
                          index_file="index,htm", autorefresh=True) #route stands for the folder where your stuff lives. prefix stands for the website you can go to access these files,
                                                                    # so you can access by going to 127.0.0.1/static/
                                                                    # index file key says hey if you visit just the static with nothing else after it where should you look to find index. 
                                                                    # And I'm going to put on auto refresh just because I'm lazy. (lol professors words)


#note from prof. you can change the prefix above and get rid of this route if you just want to host static (which begs the question why you don't use smth simpler like github pages)
@app.route('/', methods =['GET'])    #ROUTE THAT SENDS US TO THE FUNCTION BELOW
def hello():
    return make_response("Hello, world!!!!!!!") #response that function outputs

#command line: (for what?)
#  mkdir static 
#   cd static
#@app.route('/data') is one way to help serve statuc files but since we downloaded whitenoise. let's use that for efficinecy. 


#for below code: we need to have this app run through command line, we need this. 
#This is bc we should never run a flask web servor as an actual web server.
#its bad news and not secure- it is not fit to handle all the different jobs of serving a website.
#it is only good at the specific job of running some code behind the scenes and routing.
    
if __name__ == "__main__": 
    app.run(threaded=True, port=5000)

#to check if it works run python app.py in CML. (if it gives warning in red, ignore)
# to see your server. find IP address (mine is 127.0.0.1) and add a colon 5000 after it. 127.0.0.1:5000. search this on google. it should pop up.