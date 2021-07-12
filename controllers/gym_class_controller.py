from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes = gym_classes)