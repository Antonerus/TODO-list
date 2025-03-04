import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
from background.db import get_db

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
	db = get_db()
	items = db.execute(
		'SELECT topic, id, created, completed'
		' FROM item'
		' ORDER BY created DESC'			
	).fetchall()
	finished = db.execute(
		'SELECT completed'
		' FROM counter'
		' WHERE id = ?',
		(1,)
	).fetchone() 
	return render_template('home/index.html', items=items, finished=finished)

@bp.route('/add', methods=["POST"])
def add():
	topic = request.form['topic']
	error = None
	if not topic:
		error = 'Must include what the topic is'
	if error is not None:
		flash(error)
	else:	
		db = get_db()
		db.execute(
			'INSERT INTO item (topic, completed)'
			' VALUES (?, ?)', 
			(topic, "Incomplete")
		)
		db.commit()
	return redirect(url_for('home.index'))

@bp.route('/remove/<int:id>')
def remove(id):
	db = get_db()

	db.execute(
		'DELETE FROM item WHERE id = ?', (id,)
	)	
	db.commit()
	return redirect(url_for('home.index'))

@bp.route('/complete/<int:id>')
def complete(id):
	db = get_db()
	db.execute(
		'UPDATE item SET completed = ?'
		' WHERE id = ?',
		("Finished", id)
	)
	db.execute(
		'UPDATE counter SET completed = completed + 1'
		' WHERE id = ?',
		(1,)
	)	
	db.commit()
	return redirect(url_for('home.index'))

@bp.route('/uncomplete/<int:id>')
def uncomplete(id):
	db = get_db()
	db.execute(
		'UPDATE item SET completed = ?'
		' WHERE id = ?',
		("Incomplete", id)
	)
	#decrement from task completed variable
	db.execute(
		'UPDATE counter SET completed = completed - 1'
		' WHERE id = ?',
		(1,)
	)
	db.commit()
	return redirect(url_for('home.index'))
	
@bp.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
	db = get_db()
	item = db.execute(
		'SELECT id, topic, created, completed' 
		' FROM item' 
		' WHERE id = ?', 
		(id,)
	).fetchone()

	if request.method == 'POST':
		topic = request.form['topic']
		error = None
		if not topic:
			error = 'Task description required.'
		if error is not None:
			flash(error)
		else:
			db.execute(
				'UPDATE item SET topic = ?'
				' WHERE id = ?', 
				(topic, id)
			)
			db.commit()
			return redirect(url_for('home.index'))

	return render_template('home/update.html', item=item)

		
	
	

