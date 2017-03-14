from model.group import Group


def test_add_group(app):
    old_list = app.group.get_group_list()
    group = 'test group'
    app.group.add_new_group(group)
    #app.group.add_new_group('test group2')
    new_list = app.group.get_group_list()
    old_list.append(group)
    print("old_list=", old_list)
    print("new_list=", new_list)
    assert sorted(old_list) == sorted(new_list)
    #app.group.exit()
