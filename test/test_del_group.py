import random
from model.group import Group


def test_del_group_new(app):
    old_list = app.group.get_group_list()
    group = 'group1'
    if len(old_list) < 2:
        app.group.add_new_group(group)
    old_list[0:1] = []
    group_to_del = random.choice(old_list)
    #old_list[0:1] = []
    app.group.delete_group(group_to_del)
    new_list = app.group.get_group_list()
    new_list[0:1] = []
    old_list.remove(group_to_del)
    print("old_list=", old_list)
    print("new_list=", new_list)
    print("group_to_del", group_to_del)
    assert sorted(old_list) == sorted(new_list)
    #app.group.exit()