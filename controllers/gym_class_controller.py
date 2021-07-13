from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes = gym_classes)

# NEW
@gym_classes_blueprint.route("/gym_classes/new", methods = ['GET'])
def new_gym_class():
    return render_template("gym_classes/new.html")


# CREATE
@gym_classes_blueprint.route("/gym_classes", methods=['POST'])
def create_gym_class():
    name = request.form['name']
    new_gym_class = Gym_class(name)
    gym_class_repository.save(new_gym_class)
    return redirect("/gym_classes")


@gym_classes_blueprint.route("/gym_classes/<id>", methods = ['GET'])
def show_gym_classes(id):
    gym_class = gym_class_repository.select(id)
    members = gym_class_repository.members(gym_class)
    return render_template("gym_classes/show.html", gym_class = gym_class, members = members)


# EDIT
@gym_classes_blueprint.route("/gym_classes/<id>/edit", methods = ['GET'])
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template("/gym_classes/edit.html", gym_class = gym_class)

# UPDATE
@gym_classes_blueprint.route("/gym_classes/<id>", methods = ['POST'])
def update_member(id):
    name = request.form['name']
    gym_class = Gym_class(name, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")

@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods = ['POST'])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("/gym_classes")