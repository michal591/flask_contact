from flask import Flask, render_template

app = Flask(__name__)

my_contact = [
    {"name": "michal", "age": 23, "phone": "0583266591", "is_favorite": False},
    {"name": "moti", "age": 25, "phone": "0548562302", "is_favorite": True},
    {"name": "ariel", "age": 2, "phone": "0555676665", "is_favorite": True},
]


@app.route("/")
def list_contact():
    return render_template("contact_list.html", contacts=my_contact)
    """
    final_html_str = ""
    for contact in my_contact:
        final_html_str += f"{contact['name']}-<br> age:{contact['age']}, phone:{contact['phone']}<br><br>"
        return final_html_str
    """


@app.route("/single_contact/<username>")
def single_contact(username):
    return render_template("single_contact.html", contacts=my_contact, name=username)
    """
    for contact in my_contact:
        if contact["name"] == username:
            return f"the user is {contact['name']}-<br> age:{contact['age']}, phone:{contact['phone']}<br><br>"
    """


@app.route("/favorite")
def favorite_contact():
    return render_template("favorite_contact.html", contacts=my_contact)
