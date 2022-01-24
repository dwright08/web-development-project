from flask import Flask, jsonify, request

app = Flask(__name__)

albums = [
    { 'id': '1', 'name': 'Reasonable Doubt', 'artist': 'Jay-Z', 'year': '1996' },
    { 'id': '2', 'name': 'Come Get It!', 'artist': 'Rick James', 'year': '1976' },
    { 'id': '3', 'name': 'Illmatic', 'artist': 'Nas', 'year': '1994' },
    { 'id': '4', 'name': 'Off The Wall', 'artist': 'Michael Jackson', 'year': '1979' },
    { 'id': '5', 'name': 'The College Dropout', 'artist': 'Kanye West', 'year': '2004' }
]

@app.route('/albums')
def albums_index():
  return jsonify(albums)

@app.route('/albums/<id>')
def albums_show(id):
  for album in albums:
    if album['id'] == id:
      return album

  return { 'error': 'Not Found' }, 404

@app.route('/albums', methods=['POST'])
def albums_create():
  new_album = request.get_json()
  albums.append(new_album)
  return { 'message': 'Album created successfully' }, 201  

@app.route('/albums/<id>', methods=['PATCH'])
def album_update(id):
  updated_album = request.get_json()

  for album in albums:
    if album ['id'] == id:
      album.update(updated_album)
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
    return { 'error': 'Not Found' }, 404

app.run()  

    