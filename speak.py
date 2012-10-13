import subprocess

tracker_substitutes = {
     "W":"West","N":"North","S":"South","E":"East",
     "kph":"kilometers per hour","C":"Celsius","mph":"miles per hours", "kts": "knots",
     "Nm":"Nautical Miles", "m" :"metres", "km": "kilometres",
     "Mon":"Monday", "Tue":"Tuesday", "Wed":"Wednesday", "Thu":"Thursday", 
     "Fri":"Friday", "Sat":"Saturday", "Sun":"Sunday",
     "NNE":"Nor Nor East", "NE":"Nor East","ENE":"East Nor East","ESE":"East Sow East",
     "SE":"Sow East" ,"SSE" :"Sow Sow East", "SSW":"Sow Sow West","SW":"Sow West","WSW":"West Sow West",
     "WNW":"West Nor West","NW":"Nor West","NNW":"Nor Nor West",
     "%":"percent","mb": "millibars"
     }

def say (text,voice="en+m2"):
    command = "echo '" + text + "'| espeak -v " + voice +" -m"
    subprocess.call(command,shell=True)

def play(file) :
    command =  "play " + file
    subprocess.call(command,shell=True)

def escape_XML(str) :
    str.replace('"',"\042")
    str.replace('&',"\046")
    str.replace("'","\047")
    str.replace('<',"\074")
    str.replace('>',"\076")
    return str   

def ssml_break(msec):
    return '<break time="'+str(msec)+'"msec/>'

def ssml_digits(digits):
    return '<say-as interpret-as="tts:digits">'+str(digits)+"</say-as>"

def substitute(word,substitutes) :
    try :
        replacement = substitutes[word]
        return '<sub alias="' + replacement +'">'+word+'</sub>'
    except :
        return word

def expand(text,substitutes) :
    return " ".join([substitute(word,substitutes) for word in text.split(" ")])
   
