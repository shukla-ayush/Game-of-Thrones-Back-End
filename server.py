
# pip install flask
# pip install flask-mysql
# pip install flask-cors




from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify
from flask import request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

mysql = MySQL()
 
# MySQL configurations ,change according to  your local configuration
app.config['MYSQL_DATABASE_USER'] = os.environ['DBUSERNAME']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['DBPASSWORD']
app.config['MYSQL_DATABASE_DB'] = os.environ['DBSCHEMA']
app.config['MYSQL_DATABASE_HOST'] = os.environ['DBHOSTNAME']
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
def hello():
    return 'Home Page'
 
 
 
 
############################## 
# Seasons  Tables APIs
##############################

@app.route('/seasons', methods = ['GET'])
def get_seasons():
    seasons = cursor.callproc('read_seasons')
    return jsonify(cursor.fetchall())
    
@app.route('/seasons', methods = ['POST'])
def create_seasons():
    data = request.get_json()
    season_num = int(data[0])
    num_eps = int(data[1])

    try:
        cursor.callproc('create_seasons', (season_num, num_eps))
        conn.commit()
    except:
        return jsonify("duplicate")
    return jsonify([season_num, num_eps])

@app.route('/seasons', methods = ['PUT'])
def update_seasons():
    data = request.get_json()
    season_num = int(data[0])
    num_eps = int(data[1])

    try:
        cursor.callproc('update_seasons', (season_num, num_eps))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([season_num, num_eps])
    
@app.route('/seasons/<season_num>', methods = ['DELETE'])
def delete_seasons(season_num):
    try:
        cursor.callproc('delete_seasons', (int(season_num),))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([season_num,])
    
    
    
#############################
# Kingdom table APIs    
#############################

@app.route('/kingdoms', methods = ['GET'])
def get_knigdoms():
    kingdoms = cursor.callproc('read_kingdoms')
    return jsonify(cursor.fetchall())


@app.route('/kingdoms', methods = ['POST'])
def create_kingdom():
    data = request.get_json()
    try:
        cursor.callproc('create_kingdom', (data[0], data[1], data[2]))
        conn.commit()
    except:
        return jsonify("duplicate")
    return jsonify([cursor.fetchall()])

@app.route('/kingdoms', methods = ['PUT'])
def update_kingdom():
    data = request.get_json()
    try:
        cursor.callproc('update_kingdom', (data[0], data[1], data[2]))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])
    
@app.route('/kingdoms/<name>', methods = ['DELETE'])
def delete_kingdom(name):
    try:
        cursor.callproc('delete_kingdom', (name,))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify(cursor.fetchall())
    

#############################
# House table APIs    
#############################

@app.route('/houses', methods = ['GET'])
def get_houses():
    houses = cursor.callproc('read_houses')
    return jsonify(cursor.fetchall())


@app.route('/houses', methods = ['POST'])
def create_house():
    data = request.get_json()
    try:
        cursor.callproc('create_house', (data[0], data[1], data[2]))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])

@app.route('/houses', methods = ['PUT'])
def update_house():
    data = request.get_json()
    try:
        cursor.callproc('update_house', (data[0], data[1]))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])


@app.route('/houses/<name>', methods = ['DELETE'])
def delete_house(name):
    cursor.callproc('delete_house', (name,))
    conn.commit()
    return jsonify(cursor.fetchall())



#############################
# Character table APIs    
#############################

@app.route('/characters', methods = ['GET'])
def get_characters():
    characters = cursor.callproc('read_characters')
    return jsonify(cursor.fetchall())


@app.route('/characters', methods = ['POST'])
def create_character():
    data = request.get_json()
    try:
        cursor.callproc('create_character', (data[0], data[1], data[2], int(data[3])))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])


@app.route('/characters', methods = ['PUT'])
def update_character():
    data = request.get_json()
    try:
        cursor.callproc('update_character', (data[0], data[1], data[2], int(data[3])))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])

@app.route('/characters/<name>', methods = ['DELETE'])
def delete_character(name):
    cursor.callproc('delete_character', (name,))
    conn.commit()
    return jsonify(cursor.fetchall())


#############################
# Animal table APIs    
#############################

@app.route('/animals', methods = ['GET'])
def get_animals():
    animals = cursor.callproc('read_animals')
    return jsonify(cursor.fetchall())


@app.route('/animals', methods = ['POST'])
def create_animal():
    data = request.get_json()
    try:
        cursor.callproc('create_animal', (data[0], data[1], int(data[2])))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])


@app.route('/animals', methods = ['PUT'])
def update_animal():
    data = request.get_json()
    try:
        cursor.callproc('update_animal', (data[0], data[1], int(data[2])))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])


@app.route('/animals/<name>', methods = ['DELETE'])
def delete_animal(name):
    cursor.callproc('delete_animal', (name,))
    conn.commit()
    return jsonify(cursor.fetchall())


#############################
# Event table APIs    
#############################

@app.route('/events', methods = ['GET'])
def get_events():
    events = cursor.callproc('read_events')
    return jsonify(cursor.fetchall())


@app.route('/events', methods = ['POST'])
def create_event():
    data = request.get_json()
    try:
        cursor.callproc('create_event', (data[0], int(data[1]), data[2], data[3]))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])

@app.route('/events', methods = ['PUT'])
def update_event():
    data = request.get_json()
    try:
        cursor.callproc('update_event', (data[0], int(data[1]), data[2], data[3]))
        conn.commit()
    except:
        return jsonify("exception")
    return jsonify([cursor.fetchall()])


@app.route('/events/<name>', methods = ['DELETE'])
def delete_event(name):
    cursor.callproc('delete_event', (name,))
    conn.commit()
    return jsonify(cursor.fetchall())

@app.route('/kingdom_characters', methods = ['GET'])
def characters_in_kingdoms():
    characters_in_kingdom = cursor.callproc('characters_in_kingdoms')
    return jsonify(cursor.fetchall())


############################################
## Filters
############################################

# Filters for houses
@app.route('/kingdom_houses/<kingdom>', methods = ['GET'])
def houses_in_kingdoms(kingdom):
    houses_in_kingdom = cursor.callproc('read_house_for_kingdom',(kingdom,))
    return jsonify(cursor.fetchall())



# Filters for events
@app.route('/kingdom_events/<kingdom>', methods = ['GET'])
def events_in_kingdoms(kingdom):
    events_in_kingdom = cursor.callproc('read_events_for_kingdom',(kingdom,))
    return jsonify(cursor.fetchall())

@app.route('/season_events/<season>', methods = ['GET'])
def events_in_season(season):
    events_in_season = cursor.callproc('read_events_for_season',(season,))
    return jsonify(cursor.fetchall())

@app.route('/kingdom_season_events/<kingdom>/<season>', methods = ['GET'])
def events_in_season_and_kingdom(kingdom, season):
    events_in_season_and_kingdom = cursor.callproc('read_events_for_season_and_kingdom',(kingdom,int(season),))
    return jsonify(cursor.fetchall())

# Filters for animals
@app.route('/animals_for_master/<master>', methods = ['GET'])
def animals_for_master(master):
    animals_for_master = cursor.callproc('read_animals_for_master',(master,))
    return jsonify(cursor.fetchall())

@app.route('/animals_dead_alive/<status>', methods = ['GET'])
def animals_dead_alive(status):
    animals_dead_alive = cursor.callproc('read_animals_dead_alive',(int(status),))
    return jsonify(cursor.fetchall())

@app.route('/animals_for_master_dead_alive/<master>/<status>', methods = ['GET'])
def animals_for_master_dead_alive(master, status):
    animals_for_master_dead_alive = cursor.callproc('read_animals_for_master_dead_alive',(master, int(status),))
    return jsonify(cursor.fetchall())


# filters for characters
@app.route('/characters_for_house/<house>', methods = ['GET'])
def characters_for_house(house):
    characters_for_house = cursor.callproc('read_characters_for_house',(house,))
    return jsonify(cursor.fetchall())

@app.route('/characters_for_kingdom/<kingdom>', methods = ['GET'])
def characters_for_kingdom(kingdom):
    characters_for_kingdom = cursor.callproc('read_characters_for_kingdom',(kingdom,))
    return jsonify(cursor.fetchall())

@app.route('/characters_dead_alive/<status>', methods = ['GET'])
def characters_dead_alive(status):
    characters_dead_alive = cursor.callproc('read_characters_dead_alive',(status,))
    return jsonify(cursor.fetchall())

@app.route('/characters_for_house_for_kingdom/<house>/<kingdom>', methods = ['GET'])
def characters_for_house_for_kingdom(house, kingdom):
    characters_for_house_for_kingdom = cursor.callproc('read_characters_for_house_for_kingdom',(house, kingdom,))
    return jsonify(cursor.fetchall())

@app.route('/characters_for_house_dead_alive/<house>/<status>', methods = ['GET'])
def characters_for_house_dead_alive(house, status):
    characters_for_house_dead_alive = cursor.callproc('read_characters_for_house_dead_alive',(house, status))
    return jsonify(cursor.fetchall())

@app.route('/characters_for_kingdom_dead_alive/<kingdom>/<status>', methods = ['GET'])
def characters_for_kingdom_dead_alive(kingdom, status):
    characters_for_kingdom_dead_alive = cursor.callproc('read_characters_for_kingdom_dead_alive',(kingdom, status))
    return jsonify(cursor.fetchall())

@app.route('/characters_for_house_for_kingdom_dead_alive/<house>/<kingdom>/<status>', methods = ['GET'])
def characters_for_house_for_kingdom_dead_alive(house, kingdom, status):
    characters_for_house_for_kingdom_dead_alive = cursor.callproc('read_characters_for_house_for_kingdom_dead_alive',(house, kingdom, status,))
    return jsonify(cursor.fetchall())



if __name__ == "__main__":
    app.run()