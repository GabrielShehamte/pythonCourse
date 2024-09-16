const express = require('express');
const path = require('path');
const fs = require('fs')
const app = express()

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');


app.use(express.urlencoded({ extended: true}));
app.use(express.json());
app.use(express.static(path.join(__dirname, 'views')));

app.get('/', (req, res)=>{
    fs.readFile(path.join(__dirname, 'todos.txt'), 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Error reading file');
        }
        const todos = data.split('\n').filter(Boolean);
        res.render('index', {todos});
    });
});

// add a new todo
app.post('/add', (req, res) => {
    const newTodo = req.body.todo;
    fs.appendFile('todos.txt', newTodo + '\n', (err) => {
        if (err) {
            return res.status(500).send('Error saving todo');
        }
        res.redirect('/');
    });
});

//complete a todo
app.post('/complete', (req, res) => {
    const index = parseInt(req.body.index);
    fs.readFile('todos.txt', 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Error reading file');
        }
        const todos = data.split('\n').filter(Boolean);
        todos.splice(index, 1);
        fs.writeFile('todos.txt', todos.join('\n') + '\n', (err) => {
            if (err) {
                return res.status(500).send('Error updating file');
            }
            res.redirect('/');
        });
    });
});

// Update a todo
app.post('/update', (req, res) => {
    const index = parseInt(req.body.index);
    const newTodo = req.body.todo;
    fs.readFile('todos.txt', 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Error reading file');
        }
        const todos = data.split('\n').filter(Boolean);
        if (index >= 0 && index < todos.length) {
            todos[index] = newTodo;
            fs.writeFile('todos.txt', todos.join('\n') + '\n', (err) => {
                if (err) {
                    return res.status(500).send('Error updating file');
                }
                res.redirect('/');
            });
        } else {
            res.status(400).send('Invalid index');
        }
    });
});

app.listen(3000, () => {
    console.log(`App running on local port`);
});