### Flask Form

##### Instruction:
Create a form for registration of user including as much information as you can think of. 
Some ideas include: phone number, birthday, email, address, gender, favorite programming language, etc. The link below includes some examples.

##### Solution:
1.Python codes:

-class of the form:
```.py

class ContactForm(FlaskForm):
    username = StringField("Name of student", validators=[DataRequired()])
    phone_number= StringField("Phone", validators=[DataRequired()])
    birthday = StringField("Birthday", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    address = TextAreaField("Address" , validators=[DataRequired()])
    age = IntegerField("age", validators=[DataRequired()])
    favorite_programming_language = SelectField('Languages', choices=[('cpp', 'C++'),('py', 'Python')],validators=[DataRequired()])

    submit = SubmitField("Sign up")

```
-routes to the webpage that use the form:

```.py

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = ContactForm()
    if form.validate_on_submit():
        print(f"Signed up data: {form.username.data}, {form.phone_number.data}, {form.birthday.data}"
              f", {form.email.data}, {form.gender.data}, {form.address.data}"
              f", {form.age.data}, {form.favorite_programming_language.data}")
        return redirect("/welcome")

    return render_template('signup.html', form = form)

```

2.HTML codes for the sign up web page:
```.html

{% extends "base.html" %}

{% block content %}

<h1>Login page</h1>

    <form action="" method="POST">
    {{ form.csrf_token }}
        <p>
    {{ form.username.label }}
    {{ form.username() }}
    </p>

    <p>
        {{ form.phone_number.label }}
        {{ form.phone_number() }}
    </p>

        <p>
        {{ form.birthday.label }}
        {{ form.birthday() }}
    </p>

        <p>
        {{ form.email.label }}
        {{ form.email() }}
    </p>
        <p>
        {{ form.gender.label }}
        {{ form.gender() }}
    </p>
        <p>
        {{ form.address.label }}
        {{ form.address() }}
    </p>
        <p>
        {{ form.age.label }}
        {{ form.age() }}
    </p>
        <p>
        {{ form.favorite_programming_language.label }}
        {{ form.favorite_programming_language() }}
    </p>
    {{ form.submit() }}


    </form>

{% endblock %}

```

##### Evidence of sucess:
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-18%20at%2017.23.49.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-18%20at%2017.23.30.png)
