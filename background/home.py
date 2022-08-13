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
		'SELECT topic, id, created'
		' FROM item'
		' ORDER BY created DESC'			
	).fetchall()
	
	return render_template('home/index.html', items=items)

@bp.route('/add', methods=["POST"])
def add():
	topic = request.form['topic']
	db = get_db()
	db.execute(
		'INSERT INTO item (topic)'
		' VALUES (?)', 
		(topic,)
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
	
@bp.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
	db = get_db()
	item = db.execute(
		'SELECT id, topic, created' 
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

		
	
	

