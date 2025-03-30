def navBarMenu(request):
    menuItems = {'menuItems': [
        {'name': 'Home', 'path': 'home'},
        {'name': 'Projects', 'path': 'projects'},
        # {'name': 'Contact', 'path': 'contact'},
        {'name': 'Test', 'path': 'test'},
    ]}
    return menuItems