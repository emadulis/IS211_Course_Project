#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a book catalogue application"""

from flask import Flask, render_template, request, redirect, session, g, flash, url_for
import sqlite3
import validators
import os
import requests

app = Flask(__name__)


app.config.update(
    database=os.path.join(app.root_path, 'booklibrary.db'),
    SECRET_KEY='secret key'

)


def connectdb():
    sql = sqlite3.connect(app.config['database'])
    sql.row_factory = sqlite3.Row
    return sql


def loaddb():
    if not hasattr(g, 'sqlitedb'):
        g.sqlitedb = connectdb()
    return g.sqlitedb


@app.route('/')
def dashboard():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = loaddb()
        conn = db.execute('select id from users where username=? and password=?', [
            request.form['username'], request.form['password']])
        validUser = conn.fetchone()
        if validUser:
            session['logged_in'] = True
            session['userid'] = validUser[0]
            flash('You are logged in')
            return redirect(url_for('getbook'))
        else:
            session['logged_in'] = False
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


@app.route('/booklist', methods=['GET'])
def getbook():
    if not session.get('logged_in'):
        redirect(url_for('login'))
    db = loaddb()
    conn = db.execute('select userid, title, author, pagecount, averagerating, thumbnail from booklibrary where userid=?', [
        session['userid']])
    books = conn.fetchall()
    return render_template('booklist.html', books=books)


@app.route('/search', methods=['GET', 'POST'])
def search_books():
    if not session.get('logged_in'):
        redirect(url_for('login'))
    error = None
    if request.method == 'POST':
        req = requests.get(
            'https://www.googleapis.com/books/v1/volumes?q=isbn:' + request.form['isbnnumber'])
        json = req.json()
        quaried = []
        for item in json['items']:
            quary = {}
            quary['title'] = item['volumeInfo']['title']
            if 'authors' in item['volumeInfo'].keys():
                quary['author'] = item['volumeInfo']['authors'][0]
            else:
                quary['author'] = 'Author not found'
            if 'pageCount' in item['volumeInfo'].keys():
                quary['pageCount'] = item['volumeInfo']['pageCount']
            else:
                quary['pageCount'] = 'Page count not found'
            if 'averageRating' in item['volumeInfo'].keys():
                quary['averageRating'] = item['volumeInfo']['averageRating']
            else:
                quary['averageRating'] = 'Average rating not found'
            if 'imageLinks' in item['volumeInfo'].keys():
                quary['thumbnail'] = item['volumeInfo']['imageLinks']['thumbnail']
            else:
                quary['thumbnail'] = 'Thumbnail not found'
            quaried.append(quary)
        return render_template('search.html', quaried=quaried)
    return render_template('search.html')


@app.route('/searchbytitle', methods=['POST'])
def quary_byTitle():
    if not session.get('logged_in'):
        redirect(url_for('login'))
    error = None
    req = requests.get(
        'https://www.googleapis.com/books/v1/volumes?q=intitle:' + request.form['searchtitle'])
    json = req.json()
    quaried = []
    for item in json['items']:
        quary = {}
        quary['title'] = item['volumeInfo']['title']
        if 'authors' in item['volumeInfo'].keys():
            quary['author'] = item['volumeInfo']['authors'][0]
        else:
            quary['author'] = 'Author not found'
        if 'pageCount' in item['volumeInfo'].keys():
            quary['pageCount'] = item['volumeInfo']['pageCount']
        else:
            quary['pageCount'] = 'Page count not found'
        if 'averageRating' in item['volumeInfo'].keys():
            quary['averageRating'] = item['volumeInfo']['averageRating']
        else:
            quary['averageRating'] = 'Average rating not found'
        if 'imageLinks' in item['volumeInfo'].keys():
            quary['thumbnail'] = item['volumeInfo']['imageLinks']['thumbnail']
        else:
            quary['thumbnail'] = 'Thumbnail not found'
        quaried.append(quary)
    return render_template('search.html', quaried=quaried)


@app.route('/add_book', methods=['GET'])
def add_book():
    if not session.get('logged_in'):
        redirect(url_for('login'))
    error = None
    db = loaddb()
    conn = db.execute('insert into booklibrary (userid, title, author, pagecount, averagerating, thumbnail) values (?, ?, ?, ?, ?, ?)', [
        session['userid'], request.args['title'], request.args['author'], request.args['pageCount'], request.args['averageRating'], request.args['thumbnail']])
    db.commit()
    return redirect(url_for('getbook'))


@app.route('/delete_book', methods=['GET'])
def delete_book():
    if not session.get('logged_in'):
        redirect(url_for('login'))
    error = None
    db = loaddb()
    conn = db.execute('delete from booklibrary where userid=? and title=? and author=? and pagecount=? and averagerating=? and thumbnail=?', [
        session['userid'], request.args['title'], request.args['author'], request.args['pageCount'], request.args['averageRating'], request.args['thumbnail']])
    db.commit()
    return redirect(url_for('getbook'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run()
