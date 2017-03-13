

def test_1(app):
    old_list = app.get_group_list()
    app.add_new_group('test group')
    new_list = app.get_group_list()
    old_list.append('test group')
    assert sorted(old_list) == sorted(new_list)
    app.exit()
