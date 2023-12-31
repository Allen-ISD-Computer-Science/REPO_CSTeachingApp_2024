###                                                                                                                        
###               :        :                                   ------                                                      
###               --       -:                                  --                                                          
###               --      --                                  :-                                                           
###                --     --                                  --                                                           
###                --     -.   -----    -------     ------  :--------    -----    -:    --   .-----                        
###                --    --   --   --   ---   --   :-:  .--   --   --   --   --   -:    --   --   --                       
###                 --   --  :-     -:  --    .-.  --    --   --   --  --     --  -:    --   -                             
###                 --  .-   --     --  --     -:  -:    .-   --   --  --         -:    --   --.                           
###                 --  --   ---------  --     --  --------   --   --  --         -:    --    -----                        
###                  -- --   --         --     --  -:         --   --  --         -:    --       ---                       
###                  --:-    --         --     --  --         --   --  --     --  --    --        --                       
###                  :---     --   :-.  --     --  --    --   --   --   --   --   --   .--  --    --  --                   
###                   ---     .------   --     --   ------    --   --   -------    -------   ------:  --.                  
###                             :-:                   --                  :-:       :-:        --:                                                                                                                                   

from flask_login import login_required, current_user, UserMixin, LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask import *
import subprocess
import markdown
import random
import json
import yaml
import time
import sys
import os

# MISC = 0
# ARRAY = 1
# LOOP = 2
# TYPE = 3
# OOP = 4

### This will be called Veneficus with Merlin Logo - Slgoan: Become a programming wizz
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO' # os.urandom(12)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

webpage_title = "Veneficus - The best coding platform."

'''LOGIN CODE'''
# https://exploreflask.com/en/latest/blueprints.html#how-do-you-use-them

# READ
# 1. https://stackoverflow.com/questions/6699360/flask-sqlalchemy-update-a-rows-information
# 2. https://flowbite.com/docs/components/dropdowns/#:~:text=If%20you%20want%20to%20show,of%20the%20dropdown%20menu%20element.

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    # picture = db.Column(db.String(500)) # URL
    # time = db.Column(db.Time)
    # friends = db.Column()

db.init_app(app)

with app.app_context(): db.create_all()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login')
def login():
    return render_template('login.html', title = webpage_title)

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))
    login_user(user, remember=remember)
    return redirect(url_for('index'))

@app.route('/signup')
def signup():
    return render_template('signup.html', title = webpage_title)

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    user_1 = User.query.filter_by(email=email).first()
    user_2 = User.query.filter_by(username=username).first()
    if user_1:
        flash('Email address already exists')
        return redirect(url_for('signup'))
    if user_2:
        flash('Username already exists')
        return redirect(url_for('signup'))
    new_user = User(email=email, name=name, username=username, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

''' END LOGIN CODE '''

def check_for_article(article_name):
    try: os.listdir(f"articles/{article_name}")
    except FileNotFoundError: return False
    return True 

@app.route("/gallery/<article_name>/<asset_name>", methods = ["GET"])
def gallery_query_select(article_name, asset_name):
    if check_for_article(article_name) == False: return "No such article.", 404
    return send_file(f"articles/{article_name}/assets/{asset_name}")

@app.route("/gallery/<article_name>", methods = ["GET"])
def gallery_query_all(article_name):
    if check_for_article(article_name) == False: return "No such article.", 404
    files = os.listdir(f"articles/{article_name}/assets/")
    files = [x for x in files if not x.startswith(".")]
    return str(files)

# Articles (GET)
@app.route("/article/<article_name>/<language>", methods = ["GET"])
@app.route("/article/<article_name>", methods = ["GET"])
def article(article_name, language = "en"):
    if check_for_article(article_name) == False: return "No such article.", 404
    # Load YAML File
    with open(f"articles/{article_name}/config.yaml", 'r') as f: article = yaml.dump(yaml.safe_load(f))
    article = yaml.load(article, Loader=yaml.SafeLoader)
    # Metadata                      
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    article_time = time.localtime(article['published'])
    article_time = f"{months[article_time.tm_mon - 1]} {article_time.tm_mday} {article_time.tm_year}"
    article_author = User.query.get(article['author']).name
    article_title = article['title']
    # Finishing Up
    contents = None
    match language:
        case "en": contents = open(f"articles/{article_name}/contents.md", "r").read()
        case "ru": contents = open(f"articles/{article_name}/languages/russian.md", "r").read()
        case "ar": contents = open(f"articles/{article_name}/languages/arabic.md", "r").read()
    ## if contents == None:
    output = markdown.markdown(contents, extensions=['fenced_code', 'sane_lists', 'nl2br'])
    return render_template('article.html', title = article_title, date = article_time, name = article_author, contents = output, language = language)

testObject = {
    "expect": {
        "name": "add",
        "params": [["x", "Int"], ["y", "Int"]],
        "return": "Int"
    },
    "tests": [
        [{"x": 9, "y": 9}, 18],
        [{"x": 5, "y": 5}, 10],
        [{"x": 4, "y": 7}, 11],
        [{"x": 1, "y": 9}, 10],
        [{"x": 5, "y": 9}, 14],
        [{"x": 3, "y": 9}, 12],
        [{"x": 5, "y": 9}, 14],
        [{"x": 7, "y": 9}, 16],
        [{"x": 8, "y": 9}, 17],
        [{"x": 1, "y": 0}, 1]
    ]
}

def generate_swift_function(m):
    name = m["expect"]["name"]
    params = m["expect"]["params"]
    return_type = m["expect"]["return"]
    param_string = ", ".join([f"{param[0]}: {param[1]}" for param in params])
    swift_code = f"func {name}({param_string}) -> {return_type} {{\n"
    swift_code += f"    // Your code here\n"
    swift_code += "}\n"
    return swift_code

def assemble_function_call(m, param_values):
    function_name = m["expect"]["name"]
    params = m["expect"]["params"]
    if len(param_values) != len(params): raise ValueError("Number of parameter values doesn't match the number of parameters.")
    param_pairs = [f"{param[0]}: {param_values[i]}" for i, param in enumerate(params)]
    param_string = ', '.join(param_pairs)
    swift_call = f"{function_name}({param_string})"
    return swift_call

# print(generate_swift_function(m=m))
# print(assemble_function_call(m=m, param_values=[1, 2]))

@app.route("/experimental")
@login_required
def expr():
    file = generate_swift_function(m=testObject)
    return render_template("code.html", prompt="This should return the sum of <code>x</code> and <code>y</code>.", code=str(file))

@app.route("/stats/json", methods=['GET'])
@login_required
def stats_json():
    x = load_attempts()
    object = {}
    total_questions = len(x[current_user.get_id()])
    for m in x[current_user.get_id()]:
        question = time.localtime(m["date"])
        current = time.localtime(time.time())
        if current.tm_yday - question.tm_yday <= 7:
            try: object[str(current.tm_yday - question.tm_yday)] = object[str(current.tm_yday - question.tm_yday)] + 1
            except KeyError: object[str(current.tm_yday - question.tm_yday)] = 1
    for value in range(7):
        try: object[str(value)]
        except: object[str(value)] = 0
    for value in range(7):
        object[str(value)] /= total_questions
        object[str(value)] *= 100
    return json.dumps(object)

@app.route("/stats")
@login_required
def __stats():
    return render_template("graph.html", title = webpage_title)

@app.route('/user/<username>')
def user(username):
    # FIXME: Check for `AttributeError`
    # print(User.query.all()[0].name)
    user_query = User.query.filter(User.username == username)
    target_user = user_query.first()
    if target_user == None:
        return "No such user.", 404
    return render_template(
        "profile.html", # For You Page (lol) ???
        title=webpage_title,
        name=target_user.name,
        username=target_user.username,
        card = True
    )
    
def question_loader():
    return json.load(open("questions.json", "r"))["questions"]

def get_random_user():
    with app.app_context():
        query = User.query.filter_by().all()
        return random.choice(query)

questions = {}
current_question = {}
completed_questions = {}
correct_questions = {} 

def question_picker(id):
    choice = random.choice(questions[id])
    for question in range(len(questions[id])):
        if questions[id][question]["id"] == choice["id"]:
            questions[id].pop(question)
            break
        else: continue
    return choice

def load_attempts():
    my_json = {}
    try:
        with open('attempts.json') as f: my_json = json.load(f)
    except FileNotFoundError: raise Exception("Could not find file \"attempts.json\"")
    return my_json

def commit_to_db(user, question, choice):
    my_json = load_attempts()
    if str(user) not in my_json: my_json[str(user)] = []
    my_json[str(user)].append({"question": question, "choice": choice, "date": time.time()} )
    with open('attempts.json', 'w+') as f: json.dump(my_json, f)
    return

@app.route('/learn', methods=['GET'])
@login_required
def learn():
    return render_template("learn.html", title = webpage_title, Unit=[['Unit 1: Arrays', ('Introduction to Arrays', 'Array Methods', 'Array Iteration')], ['Unit 2: Functions', ('Parameters', 'Return Values', 'Function Wrap Up')], ['Unit 3: OOP', ('Introduction to OOP', 'Properties', 'Methods')]])

@app.route('/verify/code', methods=['POST'])
@login_required
def recv_code():
    program = request.data.decode('utf-8')
    print(program)
    with open("main.swift", "w") as fp:
        fp.write(program + "\n")
        for test in testObject["tests"]: fp.write("\nprint(" + assemble_function_call(testObject, param_values=[test[0][x] for x in test[0]]) + ")")
    # match os.system("swift main.swift"):
    #     case 0: program = "All Good!"
    #     case 1: program = "Bad Code!"
    #     case _: program = "Unknown!"
    final = subprocess.check_output("swift main.swift", shell=True).decode("utf-8").rsplit('\n')[:-1]
    os.remove("main.swift")
    for test in range(len(testObject["tests"])):
        if testObject["tests"][test - 1][1] != int(final[test - 1]): return "Bad Code!"
    return "All Good!"

@app.route('/verify', methods=['POST'])
@login_required
def parse_data():    
    global correct_questions
    global current_question
    global completed_questions
    if request.method == 'POST':
        ID = current_user.get_id()
        if current_question[ID] == None: return "Invalid Context: Missing `current_question`", 404
        r = request.data.decode('utf-8')
        x = json.loads(r)['option']
        return_value = (json.dumps({'correct': str(x) == str(current_question[ID]["correct"] + 1), "correct_choice": current_question[ID]["correct"] + 1}), False)
        if str(x) == str(current_question[ID]["correct"] + 1): return_value = (json.dumps({'correct': str(x) == str(current_question[ID]["correct"] + 1), "correct_choice": current_question[ID]["correct"] + 1}), True)
        correct_questions[ID] += (1 if return_value[1] == True else 0)
        return_value = return_value[0]
        completed_questions[ID] += 1
        commit_to_db(ID, current_question[ID]["id"], str(x))
        current_question[ID] = question_picker(ID)
        return return_value
    return "USE 'POST'", 405

# This should also serve things from `/experimental`
@app.route('/test')
@login_required
def __test():
    global questions
    global correct_questions
    global current_question
    global completed_questions
    ID = current_user.get_id()
    # Create all Values
    try: questions[ID]
    except: questions[ID] = question_loader()
    try: correct_questions[ID]
    except KeyError: current_question[ID] = question_picker(ID)
    try: correct_questions[ID]
    except KeyError: correct_questions[ID] = 0
    try: completed_questions[ID]
    except KeyError: completed_questions[ID] = 0
    if len(questions[ID]) == 0:
        TotalPercent = (correct_questions[ID]/completed_questions[ID]) * 100
        TemplateRendered = render_template("question.html", title=webpage_title, flash=f"You got {str(TotalPercent)}%")
        questions[ID] = question_loader()
        current_question[ID] = question_picker(ID)
        completed_questions[ID] = 0
        correct_questions[ID] = 0
        return TemplateRendered
    else:
        # Return Template
        return render_template(
            'question.html',
            title=webpage_title,
            prompt=current_question[ID]["question"],
            questions=current_question[ID]["choices"],
        )

@app.route('/')
def index():
    if current_user.is_authenticated: return render_template('home.html', title = webpage_title, ReccomendedUser=get_random_user(), Name=f"{current_user.name.split(' ')[0]} {current_user.name.split(' ')[-1][0]}.")
    else: return render_template('index.html', title = webpage_title)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        with app.app_context():
            db.create_all()
    app.run(
        # host='0.0.0.0',
        port=5000,
        debug=True
    )
    # http://192.168.1.39:5000/