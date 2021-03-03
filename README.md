# flask-chat-app-v1
Basic Socketio app using flask


## Part1:

- ## Setting up the virtual environment

        $ python3 -m venv venv

- ## Activating the virtual environment

        $ source venv/bin/activate

- ## Now we have to install the flask inside the venv

        (venv) $ pip install flask

- ## Checking the packages installed using
        (venv) $ pip freeze
        click==7.1.2
        Flask==1.1.2
        itsdangerous==1.1.0
        Jinja2==2.11.3
        MarkupSafe==1.1.1
        Werkzeug==1.0.1


<br>
<br>

The very first basic structure of flask app

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'



if __name__== '__main__':
    app.run(debug = True)
```


## install the flask socketio using pip
    
    pip install flask-socketio

## note

I have installed Flask-SocketIO version 5, so you need version 3 of the JavaScript client, so ...

I will use this CDN URL  version 3.0.5: https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.5/socket.io.min.js 


```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.5/socket.io.min.js"></script>
<script type="text/javascript" charset="utf-8">
        var socket = io.connect("http://127.0.0.1:5000");

        socket.on('connect', function () {
            socket.emit("join_room", {
                username: "{{ username }}",
                room: "{{ room }}"
            })

        })
</script>
```


<br>




    