import clr
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *


clr.AddReferenceByName("UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
from System.Windows.Automation import *


class App:

    def __init__(self):
        self.application = Application.Launch("C:\\addressbook_exe\\AddressBook.exe")
        self.main_window = self.application.GetWindow("Free Address Book")

    def get_group_list(self):
        main_window = self.main_window
        modal = self.open_group_editor()
        tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        l = [node.Text for node in root.Nodes]
        self.close_group_editor(main_window)
        return l

    def add_new_group(self, name):
        main_window = self.main_window
        modal = self.open_group_editor()
        modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
        Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
        self.close_group_editor(main_window)

    def close_group_editor(self, main_window):
        main_window.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()

    def open_group_editor(self):
        main_window = self.main_window
        main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
        modal = main_window.ModalWindow("Group editor")
        return modal

    def exit(self):
        main_window = self.main_window
        main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()