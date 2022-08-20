import pytest
from background.db import get_db

def test_index(client):
	response = client.get('/')
	assert b"TODO-list" in response.data
	assert b"A simple list to help you remember" in response.data 

	assert b"TODO Topic" in response.data
	assert b"Add" in response.data
	assert b"Task" in response.data
	assert b"Status" in response.data
	assert b"Remove" in response.data
	assert b"Update" in response.data
	
	assert b"test topic" in response.data
	assert b"Incomplete" in response.data


def test_add(client, app):
	client.post('/add', data={'topic': 'created'})

	with app.app_context():
		db = get_db()
		num_task = db.execute('SELECT COUNT(id) FROM item').fetchone()[0]
		assert num_task == 2

def test_update(client, app):
	assert client.get('/update/1').status_code == 200
	client.post('/update/1', data={'topic': 'updated'})
	
	with app.app_context():
		db = get_db()
		item = db.execute('SELECT * FROM item WHERE id = 1').fetchone()
		assert item['topic'] == 'updated'		
		
def test_remove(client, app):
	client.get('/remove/1')

	with app.app_context():
		db = get_db()
		item = db.execute('SELECT * FROM item WHERE id = 1').fetchone()
		assert item is None	
		

def test_status(client, app):
	client.get('/complete/1')
	with app.app_context():
		db = get_db()
		item = db.execute('SELECT * FROM item WHERE id = 1').fetchone()
		assert item['completed'] == 'Finished'
		counter = db.execute('SELECT * FROM counter WHERE id = 1').fetchone()
		assert counter['completed'] == 1
		client.get('/uncomplete/1')
		item2 = db.execute('SELECT * FROM item WHERE id = 1').fetchone()
		assert item2['completed'] == 'Incomplete'
		counter2 = db.execute('SELECT * FROM counter WHERE id = 1').fetchone()
		assert counter2['completed'] == 0
	




