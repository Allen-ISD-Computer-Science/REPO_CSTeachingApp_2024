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
from xml.etree import ElementTree as ET
from flask_sqlalchemy import SQLAlchemy
from flask import url_for as ufor
from bs4 import BeautifulSoup
from avatars import *
from flask import *
import python_avatars
import subprocess
import markdown
import getpass
import random
import json
import yaml
import time
import enum
import sys
import os

# FIXME: Some Features don't seem to work on CoderMerlin Vapor, Add a fix to make sure they do.
config = {
    "vapor": False,
    "host": '0.0.0.0',
    "port": os.environ.get("PORT"),
    "vapor_username": ''
}

class Topics(enum.Enum):
    MISC = 0
    ARRAY = 1
    LOOP = 2
    TYPE = 3
    OOP = 4

### This will be called Veneficus with Merlin Logo - Slgoan: Become a programming wizz
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO' # os.urandom(12)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
webpage_title = "Veneficus - The best coding platform."

# This is such a nasty hack. I changed flasks native `url_for` to `ufor` and made this the `url_for` function.
def url_for(endpoint, **values): return f"/vapor/{getpass.getuser()}" + ufor(endpoint, **values) if config["vapor"] == True else ufor(endpoint, **values)

app.jinja_env.globals.update(url_for=url_for)

'''LOGIN CODE'''
# https://exploreflask.com/en/latest/blueprints.html#how-do-you-use-them

# READ
# 1. https://stackoverflow.com/questions/6699360/flask-sqlalchemy-update-a-rows-information
# 2. https://flowbite.com/docs/components/dropdowns/#:~:text=If%20you%20want%20to%20show,of%20the%20dropdown%20menu%20element.

db = SQLAlchemy()

# Since SQLAlchemy does not support unsigned 64-bit integers, we are forced to use strings for picture. 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    picture = db.Column(db.String(64)) # db.Column(db.BigInteger)
    # time = db.Column(db.Time)

class Lesson:

    # class LessonTopics(enum.Enum)

    class LessonStages(enum.Enum):
        Stage_0 = 0 # Not started
        Stage_1 = 1 # Lesson
        Stage_2 = 2 # Quiz
        Stage_3 = 3 # Finished

    associatedQuestionPallet = None
    associatedLessonTopic = None
    assoicatedArticleLink = None

    def __init__(self, topic, article, pallet):
        self.associatedLessonTopic = topic
        self.assoicatedArticleLink = article
        self.associatedQuestionPallet = pallet
        self.algorithmKeyEntry = {}
        # self.reccomendationAlgorithm = Lesson.FindElementWithCondition(self)

    def new_algorithm(self, id):
        self.algorithmKeyEntry[id] = Lesson.FindElementWithCondition(self, id)
        return

    def get_algorithm(self, id):
        if id not in self.algorithmKeyEntry: self.new_algorithm(id)
        return self.algorithmKeyEntry[id]

    class FindElementWithCondition:

        def __init__(self, Lesson, _id):
            lst = Lesson.associatedQuestionPallet
            self.uid = _id
            self.lst = lst
            self.copy_lst = lst
            self.length = self.get_number_of_questions(len(lst))
            self.multi = 0
            self.questions = 0
            self.choices = []
            self.completed = 0

        def rand_bool(self): 
            try: completed_questions[self.uid]
            except KeyError: completed_questions[self.uid] = 0
            x = correct_questions[self.uid] > self.completed
            self.completed += 1
            return x
            # return random.choice([True, False])

        def get_number_of_questions(self, number_of_questions = 33):
            x = 0
            while (((5 * x) - 3) + 1) < number_of_questions: x += 1
            return x

        def find_element_with_condition(self):
            if len(self.choices) >= self.length: return None
            index_middle = (len(self.copy_lst) // 2) + self.multi
            index_left = (index_middle - 1) + self.multi
            index_right = (index_middle + 1) + self.multi
            # Select Question
            choice = random.choice([index_left, index_middle, index_right])
            value = self.lst[choice]
            self.copy_lst.pop(choice)
            self.choices.append(value)
            # Multi update
            cond_X = (len(self.choices) >= self.length - 1)
            cond_Y = (len(self.choices) > 1)
            if cond_X or cond_Y: 
                # print(f"Okay, I am choosing a question. {self.questions}")
                if self.rand_bool() == True: self.multi += 1
                else: self.multi -= 1
            self.questions += 1
            # print(question_loader()[int(self.choices[-1])]['difficulty'])
            return self.choices[-1]

class LessonCatalog:

    def __init__(self):
        array = ['000000002', '000000008', '000000014', '000000016', '000000017', '000000018', '000000001', '000000003', '000000004', '000000005', '000000007', '000000010', '000000012', '000000015', '000000006', '000000013', '000000009', '000000011']
        self.lessonCatalog = {
            "0": Lesson(Topics.ARRAY, "article", array),
            "1": Lesson(Topics.MISC, "types", array)
        }

    # def search(self, topic: Topics): return [lesson for lesson in self.lessonCatalog if lesson.associatedLessonTopic == topic]
    # def search(self, link: str): return [lesson for lesson in self.lessonCatalog if lesson.assoicatedArticleLink == link]
    def search(self, id: int): return self.lessonCatalog[id]    

    def make_user_card(self):
        user_card = {"iscard": True, "lessons": {}}
        for lesson in self.lessonCatalog.keys(): user_card["lessons"][lesson] = Lesson.LessonStages.Stage_0.value
        return user_card

MyLessonCatalog = LessonCatalog()

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
    email = str(request.form.get('email')).lower()
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
    email = str(request.form.get('email')).lower()
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
    new_user = User(email=email, name=name, username=username, picture = bin(0x68e9c001fffe8d2c)[2:], password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

''' END LOGIN CODE '''

def modify_svg_dimensions(svg_string, new_width, new_height):
    root = ET.fromstring(svg_string)
    for elem in root.iter():
        if 'width' in elem.attrib: elem.attrib['width'] = str(new_width)
        if 'height' in elem.attrib: elem.attrib['height'] = str(new_height)
    modified_svg_string = ET.tostring(root, encoding='unicode')    
    return modified_svg_string

@login_required
def set_profile_picture():
    user = User.query.get(current_user.get_id())
    rand = python_avatars.Avatar.random()
    user.picture = bin(avatar_to_int(rand))[2:]
    db.session.commit()

@login_required
def get_profile_picture(w = 96, h = 96):
    picture = eval("0b" + User.query.get(current_user.get_id()).picture)
    new_render = modify_svg_dimensions(extract_bits(picture).render(), w, h)
    return new_render

app.jinja_env.globals.update(get_profile_picture=get_profile_picture)

@app.route('/pages/tos')
def __TOS():
    contents = open("pages/TOS.md", 'r').read()
    output = markdown.markdown(contents) # , extensions=['fenced_code', 'sane_lists', 'nl2br'])
    return render_template("document.html", content=output) # output

@app.route('/pages/privacy')
def __privacy():
    contents = open("pages/privacy.md", 'r').read()
    output = markdown.markdown(contents) # , extensions=['fenced_code', 'sane_lists', 'nl2br'])
    return render_template("document.html", content=output)

@app.route('/pages/about')
def __about():
    contents = open("pages/about.md", 'r').read()
    output = markdown.markdown(contents) # , extensions=['fenced_code', 'sane_lists', 'nl2br'])
    return render_template("document.html", content=output)

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

def treat(html_content, username):
    if config["vapor"] == False: return html_content
    soup = BeautifulSoup(html_content, 'html.parser')
    for img_tag in soup.find_all('img', src=True):
        img_tag['src'] = f"/vapor/{username}{img_tag['src']}"
    modified_html = str(soup)
    return modified_html

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
        case "zh": contents = open(f"articles/{article_name}/languages/chinese.md", "r").read()
    language_list = article['languages']
    ffcheck = check_for_fast_forward(article_name)
    ## if contents == None:
    output = markdown.markdown(contents, extensions=['fenced_code', 'sane_lists', 'nl2br'])
    output = treat(output, config['vapor_username'])
    return render_template('article.html', title = article_title, date = article_time, name = article_author, contents = output, language = language, language_list = language_list, ffcheck = ffcheck)

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

@app.route('/stats/json/categories', methods=['GET'])
@login_required
def stats_json_general():
    x = load_attempts()
    object = {}
    total_questions = len(x[current_user.get_id()])
    questions = question_loader()
    # Total amount of correct questions [0], Total amount of incorrect questions [1]
    for m in x[current_user.get_id()]:
        if int(m['choice']) == questions[int(m['question']) - 1]['correct'] + 1:
            key = questions[int(m['question']) - 1]['category']
            try: object[key][0] = object[key][0] + 1
            except KeyError: object[key] = [1, 0]
        else:
            key = questions[int(m['question']) - 1]['category']
            try: object[key][1] = object[key][1] + 1
            except KeyError: object[key] = [0, 1]
    # Calculate the percentage of correct questions
    for m in object.keys():
        try: object[m] = (object[m][0] / (object[m][0] + object[m][1])) * 100
        except ZeroDivisionError: object[m] = 1
    return json.dumps(object)

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
    '''
    for value in range(7):
        object[str(value)] /= total_questions
        object[str(value)] *= 100
    '''
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

warrent = {}
lessons = {}
questions = {}
attempting = {}
current_question = {}
completed_questions = {}
correct_questions = {} 
count_questions = len(question_loader())

def question_picker(id, _attempting = "test"):
    if _attempting == "quiz" or attempting[id] == "quiz":
        for lessonCurrent in lessons[id]["lessons"].keys(): 
            if lessons[id]["lessons"][lessonCurrent] == Lesson.LessonStages.Stage_3.value: continue
            else: break
        UserReccomendationAlgorithmInstance = MyLessonCatalog.lessonCatalog[lessonCurrent].get_algorithm(id=id)
        try: choice = int(UserReccomendationAlgorithmInstance.find_element_with_condition()) - 1
        except: return None
        try: value = questions[id][choice] 
        except IndexError: print("Index out of range. Probably not enough questions in questions.json.")
        # questions[id].pop(choice) # I think this is the line that is causing the problem.
        return value
    else:
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

@login_required
def get_lesson_state(unit):
    global lessons
    ID = current_user.get_id()
    if lessons == {}: return Lesson.LessonStages.Stage_0.value
    try: return lessons[str(ID)]["lessons"][str(unit - 1)]
    except KeyError: return Lesson.LessonStages.Stage_0.value
    
app.jinja_env.globals.update(get_lesson_state=get_lesson_state)

# TODO: Assign each Lesson and Unit a Unique ID so we can mark each Lesson as done when a user completes it.
@app.route('/learn', methods=['GET'])
@login_required
def learn():
    return render_template("learn.html", title = webpage_title, Unit=[['Unit 1: Arrays', 1], ['Unit 2: Functions', 2], ['Unit 3: OOP', 3]])

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
    if check_if_currently_attempting(ID, "test") == True: return render_template("errors/core/attempting.html", QuizName="Practice")
    # Create all Values
    try: questions[ID]
    except: questions[ID] = question_loader()
    try: current_question[ID]
    except KeyError: current_question[ID] = question_picker(ID)
    try: correct_questions[ID]
    except KeyError: correct_questions[ID] = 0
    try: completed_questions[ID]
    except KeyError: completed_questions[ID] = 0
    try: 
        if attempting[ID] == None: attempting[ID] = "test"
    except: attempting[ID] = "test"
    # if len(questions[ID]) == 0:
    if len(questions[ID]) < count_questions - 7:
        TotalPercent = round(correct_questions[ID]/completed_questions[ID] * 100)
        TemplateRendered = render_template("question.html", title=webpage_title, flash=f"You got {str(TotalPercent)}%", parse_data_func="parse_data", testing_func = "__test")
        questions[ID] = question_loader()
        current_question[ID] = question_picker(ID)
        completed_questions[ID] = 0
        correct_questions[ID] = 0
        attempting[ID] = None
        return TemplateRendered, 202
    else:
        # Return Template
        return render_template(
            'question.html',
            title=webpage_title,
            prompt=current_question[ID]["question"],
            questions=current_question[ID]["choices"],
            parse_data_func="parse_data",
            testing_func = "__test"
        )

# FIXME: Make something simmlar for older articles.
@login_required
def check_for_fast_forward(article):
    global lessons
    ID = current_user.get_id()
    try: lessons[ID]["iscard"]
    except: lessons[ID] = MyLessonCatalog.make_user_card()
    for lessonCurrent in lessons[ID]["lessons"].keys(): 
        if MyLessonCatalog.lessonCatalog[lessonCurrent].assoicatedArticleLink == article:
            if lessons[ID]["lessons"][lessonCurrent] == Lesson.LessonStages.Stage_0.value: return True
            else: return False
        else: continue
    else: return None # Invalid  

def check_if_currently_attempting(ID, access_name):
    global attempting
    try: attempting[ID]
    except: attempting[ID] = None
    if attempting[ID] == None: return False
    elif attempting[ID] == access_name: return False
    else: return True
    # return ((not attempting[ID] == None) or attempting[ID] != access_name)

@login_required
def get_current_lesson():
    global lessons
    ID = current_user.get_id()
    try: lessons[ID]["iscard"]
    except: lessons[ID] = MyLessonCatalog.make_user_card()
    for lessonCurrent in lessons[ID]["lessons"].keys(): 
        if lessons[ID]["lessons"][lessonCurrent] == Lesson.LessonStages.Stage_3.value: continue
        else: break
    return lessonCurrent

@app.route('/mule')
def __mule():
    global lessons
    ID = current_user.get_id()
    try: lessons[ID]["iscard"]
    except: lessons[ID] = MyLessonCatalog.make_user_card()
    for lessonCurrent in lessons[ID]["lessons"].keys(): 
        if lessons[ID]["lessons"][lessonCurrent] == Lesson.LessonStages.Stage_3.value: continue
        else: break
    match lessons[ID]["lessons"][lessonCurrent]:
        case Lesson.LessonStages.Stage_0.value: lessons[ID]["lessons"][lessonCurrent] = Lesson.LessonStages.Stage_1.value
        case Lesson.LessonStages.Stage_1.value: 
            warrent[ID] = True
            lessons[ID]["lessons"][lessonCurrent] = Lesson.LessonStages.Stage_2.value
        case _: ...
    return redirect(url_for("guide"))

# Custom quiz view just for Lesson Quizzes.
@app.route('/quiz')
@login_required
def __quiz():
    global questions
    global correct_questions
    global current_question
    global completed_questions
    ID = current_user.get_id()
    if check_if_currently_attempting(ID, "quiz") == True: return render_template("errors/core/attempting.html", QuizName="Lesson")
    try:
        if warrent[ID] == True: pass
        else: return "No Quiz Warrent", 404
    except: 
        warrent[ID] = False
        return "No Quiz Warrent", 404
    for lessonCurrent in lessons[ID]["lessons"].keys(): 
        if lessons[ID]["lessons"][lessonCurrent] == Lesson.LessonStages.Stage_3.value: continue
        else: break
    try: 
        # This is different from the `__test` route.
        # This is because quiz requires a different algorithm and needs to insure that the prior loaded question has to be from that algorithm.
        # FIXME: This is why it isn't working.
        # TODO: Run a test to make sure that this line `if attempting[ID] == None:` causes the problem.
        if len(MyLessonCatalog.lessonCatalog[lessonCurrent].get_algorithm(id=ID).choices) == 0:
            questions[ID] = question_loader()
            current_question[ID] = question_picker(ID, "quiz")
        else: current_question[ID]
    except KeyError: current_question[ID] = question_picker(ID, "quiz")
    try: questions[ID]
    except: questions[ID] = question_loader()
    try: correct_questions[ID]
    except KeyError: correct_questions[ID] = 0
    try: completed_questions[ID]
    except KeyError: completed_questions[ID] = 0
    try: 
        if attempting[ID] == None: attempting[ID] = "quiz"
    except: attempting[ID] = "quiz"
    if current_question[ID] == None:
        warrent[ID] = False
        lessons[ID]["lessons"][lessonCurrent] = Lesson.LessonStages.Stage_3.value
        TotalPercent = round(correct_questions[ID]/completed_questions[ID] * 100)
        TemplateRendered = render_template("question.html", title=webpage_title, flash=f"You got {str(TotalPercent)}%", parse_data_func="parse_data", testing_func = "__quiz")
        questions[ID] = question_loader()
        # current_question[ID] = question_picker(ID)
        del current_question[ID]
        completed_questions[ID] = 0
        correct_questions[ID] = 0
        attempting[ID] = None
        # FIXME: Indicate that the quiz has been completed.
        return TemplateRendered, 202
    else:
        # Return Template
        return render_template(
            'question.html',
            title=webpage_title,
            prompt=current_question[ID]["question"],
            questions=current_question[ID]["choices"],
            parse_data_func="parse_data",
            testing_func = "__quiz"
        )

# Description: Guide will be the route that returns the next link to the next component of a lesson (if ready and available).
# (1) FIXME: Save the lesson state in a JSON File simmlar to `attempts.json`.
# (2) FIXME: Instead of returning to `__test`, Create a custom quiz view just for Lesson Quizzes.
@app.route('/guide')
@login_required
def guide():
    global lessons
    ID = current_user.get_id()
    try: lessons[ID]["iscard"]
    except: lessons[ID] = MyLessonCatalog.make_user_card()
    for lessonCurrent in lessons[ID]["lessons"].keys(): 
        if lessons[ID]["lessons"][lessonCurrent] == Lesson.LessonStages.Stage_3.value: continue
        else: break
    match lessons[ID]["lessons"][lessonCurrent]:
        case Lesson.LessonStages.Stage_0.value: return redirect(url_for('__mule'))
        case Lesson.LessonStages.Stage_1.value: return redirect(url_for("article", article_name=MyLessonCatalog.lessonCatalog[lessonCurrent].assoicatedArticleLink))
        case Lesson.LessonStages.Stage_2.value: return redirect(url_for("__quiz"))
        case _: 
            for value in lessons[ID]["lessons"].values():
                if value != Lesson.LessonStages.Stage_3.value: return "Unknown Error in guide route. <i>(Hint no context)</i>", 404
            return render_template("congrats.html", title = webpage_title)
            # return "Congratulations! You have completed all the lessons.", 200 # This is a placeholder solution.
        
@app.route('/')
def index():
    if current_user.is_authenticated: return render_template('home.html', title = webpage_title, ReccomendedUser=get_random_user()) # Name=f"{current_user.name.split(' ')[0]} {current_user.name.split(' ')[-1][0]}.")
    else: return render_template('index.html', title = webpage_title), 200

@app.route('/settings')
def settings():
    return render_template('settings.html', title = webpage_title)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.errorhandler(404)
def page_not_found(e):
    # return render_template('errors/404.html', title = webpage_title), 404
    return render_template('errors/http/404.html', title = webpage_title), 404

if __name__ == '__main__':
    if not os.path.exists('attempts.json'):
        with open("attempts.json", "w+") as f: f.write('{}')
    if not os.path.exists('db.sqlite'):
        with app.app_context():
            db.create_all()
    app.run(
        host=config["host"],
        port=config["port"],
        debug=True
    )
    # http://192.168.1.39:5000/
