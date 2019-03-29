from tkinter import *
#global description
active_element = ()
tags = {"water":    {"id":0,  "color": "#33E9FF", "recipe": []},
        "fire":     {"id":1,  "color": "#FF3333", "recipe": []},
        "earth":    {"id":2,  "color": "#A47700", "recipe": []},
        "air":      {"id":3,  "color": "#CCF1FF", "recipe": []},
        "steam":    {"id":4,  "color": "#dae4e8", "recipe": [0,1]},
        "lava":     {"id":5,  "color": "#fc8600", "recipe": [1,2]},
        "sand":     {"id":6,  "color": "#ffeb00", "recipe": [2,3]},
        "cloud":    {"id":7,  "color": "#0014ff", "recipe": [3,4]},
        "rock":     {"id":8,  "color": "#717171", "recipe": [2,6]},
        "glass":    {"id":9,  "color": "#34fdf9", "recipe": [1,6]},
        "obsidian": {"id":10, "color": "#c700cc", "recipe": [0,5]},
        "rain":     {"id":11, "color": "#2683a7", "recipe": [0,7]}}
#start main window
root = Tk()
root.geometry("500x500+300+300")

#frames description
side_l = Frame(root, bg="lightgreen", width=100, height=500)
side_r = Canvas(root, bg="white", width=400, height=500)

#global functions
def select_active(event):
    global active_element
    tmp = side_r.find_overlapping(event.x, event.y, event.x, event.y)
    if tmp:
        active_element = side_r.find_overlapping(event.x, event.y, event.x, event.y)[-1]
    else:
        active_element = ()
def del_active(event):
    tmp = side_r.find_overlapping(event.x, event.y, event.x, event.y)
    if tmp:
        side_r.delete(tmp[-1])
def move_object(event):
    global tags, active_element

    recipe = []
    for el in side_r.find_overlapping(event.x, event.y, event.x, event.y):
        tag = side_r.gettags(el)[0]
        recipe.append(tags[tag]["id"])
    recipe.sort()
    for key in tags.keys():
        if recipe == tags[key]["recipe"]:
            tags[key]["recipe"].clear()
            c = tags[key]["color"]
            side_r.create_rectangle(0, 0, 50, 50, outline=c, fill=c, tag=key)
            
    side_r.coords(active_element, event.x-25, event.y - 25, event.x + 25, event.y + 25)

#bind global functions
side_r.bind("<B1-Motion>", move_object)
side_r.bind("<Button-1>", select_active)
side_r.bind("<Button-3>", del_active)

#items function
def add_item(event):
    global side_r, tags
    el = event.widget.cget("text")
    c = tags[el]["color"]
    side_r.create_rectangle(0, 0, 50, 50, outline=c, fill=c, tag=el)

#create buttons
for key in tags.keys():
    butt = Button(side_l, text=key)
    butt.bind("<Button-1>", add_item)
    butt.pack(expand=1, fill=BOTH)

#pack frames
side_l.pack(side=LEFT, fill=BOTH, expand=1)
side_r.pack(side=LEFT)

root.mainloop()
