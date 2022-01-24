import csv
from flask import Flask, render_template, request

app = Flask(__name__)

DATA_FILE = 'data.csv'
FIELDNAMES = ['id', 'name', 'artist', 'year']


albums = []
    
def load_data_file():
  with open(DATA_FILE) as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
      albums.append(row)

def append_data_file(new_row):
  with open(DATA_FILE, 'a', newline='') as data_file:
    writer = csv.DictWriter(data_file, FIELDNAMES)
    writer.writerow(new_row)    

def dump_data_file():
  with open(DATA_FILE, 'w', newline='') as data_file:
    writer = csv.DictWriter(data_file, FIELDNAMES)
    writer.writeheader()
    for album in albums:
      writer.writerow(album)      

@app.route('/albums')
def albums_index():
  return render_template('index.html', albums = albums)

@app.route('/albums/<id>')
def albums_show(id):
  for album in albums:
    if album['id'] == id:
      return render_template('show.html', name=album['name'], artist=album['artist'], year=album['year'])

@app.route('/albums', methods=['POST'])
def albums_create():
  new_album = request.get_json()
  
  albums.append(new_album)
  append_data_file(new_album)
  return { 'message': 'Album created successfully' }, 201  

@app.route('/albums/<id>', methods=['PATCH'])
def album_update(id):
  updated_album = request.get_json()
  print(updated_album)

  for album in albums:
    if album ['id'] == id:
      album.update(updated_album)
      dump_data_file()
      return { 'message': 'Album updated succesffully' }, 201
  
  return { 'error': 'Not Found' }, 404

@app.route('/albums/<id>', methods=['DELETE'])
def albums_delete(id):
  found_idx = None

  for i in range(len(albums)):
    if albums[i]['id'] == id:
      found_idx = i
      break

  if found_idx != None:
    albums.pop(found_idx)
    dump_data_file()
    return { 'message': 'Album deleted succesffully' }, 201
    
  return { 'error': 'Not Found' }, 404

   
load_data_file()
app.run()