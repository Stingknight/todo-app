from Todo_list import app,db
from Todo_list.model import Todo
from flask import render_template,request,flash,redirect,url_for

@app.route('/')
@app.route('/home')
def home():
    todo_data=Todo.query.order_by(Todo.datetime_data)
    return render_template('base.html',todo_data=todo_data)

@app.route('/create_todo',methods=['GET','POST'])
def create_todo():
    if request.method=='POST':
        todo_data=request.form['todo']

        if todo_data:
            
            todo=Todo(text=todo_data)
            db.session.add(todo)
            db.session.commit()
            flash('Created sucessfully!! ')
            return redirect('home')

    return render_template('createtodo.html')


@app.route('/update_todo/<int:id>',methods=['GET','POST'])
def update_todo(id):
    update_data=Todo.query.get(id)

    if request.method=='POST':

        update_data=Todo.query.get(id)
        data=request.form['todo1']
        update_data.text=data
        if data:
            db.session.add(update_data)
            db.session.commit()
            flash('updated sucessfully !!')
            return redirect(url_for('home'))
    return render_template('update.html',update_data=update_data)

@app.route('/delete_todo<int:id>')
def delete_todo(id):

    data=Todo.query.get(id)
    db.session.delete(data)
    db.session.commit()
    flash('Deleted sucessfully ')
    return redirect(url_for('home'))