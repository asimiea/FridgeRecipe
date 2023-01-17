import tkinter as tk
from tkinter import ttk
import requests

def get_recipes(ingredients, vegetarian=False):
    # Make API call to a recipe website using the ingredients
    url = 'https://www.recipepuppy.com/api/?i=' + ingredients
    if vegetarian:
        url += '&q=vegetarian'
    response = requests.get(url)
    data = response.json()

    # Extract the list of recipes from the API response
    recipes = data['results']

    # Return the list of recipes
    return recipes

def on_submit():
    ingredients = entry.get()
    recipe_list.delete(0,tk.END)
    if vegetarian_var.get() == 1:
        recipes = get_recipes(ingredients, vegetarian=True)
    else:
        recipes = get_recipes(ingredients)
    for recipe in recipes:
        recipe_list.insert(tk.END, recipe['title'])

root = tk.Tk()
root.title("Recipe Finder")

label = ttk.Label(root, text="Enter ingredients separated by commas:")
label.pack()

entry = ttk.Entry(root)
entry.pack()

vegetarian_var = tk.IntVar()
vegetarian_check = tk.Checkbutton(root, text="Vegetarian", variable=vegetarian_var)
vegetarian_check.pack()

submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

recipe_list = tk.Listbox(root)
recipe_list.pack()

root.mainloop()
