from frames.utility.direction import Direction

def generate_directions(lines, root, controller, parent_frame):
    views = []
    for line in lines:
        _from = line[1]
        _to = line[2]
        view = Direction(root, controller)
        view.create_widgets(controller, parent_frame=parent_frame)
        view.label = _from + " - " + _to
        views.append(view)
    return views
