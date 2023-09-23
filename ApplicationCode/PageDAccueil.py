from tkinter import ttk
import frontEnd as fe


def HomePage(root, user_name, admin_name):
    # creating home page frame
    home = ttk.Frame(root)

    # creating the command to the buttons
    def go_to():  # create a function to create a frame
        # creating the form page
        frame = ttk.Frame(root)
        # hiding the home page which is the current page
        home.pack_forget()
        return frame

    def AddAFarmer():
        form = go_to()
        # calling the function FormPage from the file formPage
        import formPage as fp
        fp.Form_Page(form, root, home)

    def ViewSubscriberList():
        view = go_to()
        # calling the function ViewSubscriberPage from the file viewSubscriberPage
        import viewSubscribrPage as vp
        vp.SubscriberPage(view, home)

    def deleteASubscriber():
        delete = go_to()
        # calling the function ViewSubscriberPage from the file viewSubscriberPage
        import SubscriberDeletionPage as sp
        sp.SubscriberDeletion(delete, home, root)

    def addNewUser():
        add_user = go_to()
        import AddUserPage as addUser
        addUser.addingNewUser(add_user, home, root)

    # Place buttons in the home page
    if user_name == admin_name:  # adding the deletion function for only admin user
        fe.addLabel(home,'\n',1)
        fe.addBttn(home,AddAFarmer,"إضافة مشترك جديد ",2)
        fe.addLabel(home, '\n', 3)
        fe.addBttn(home,ViewSubscriberList,"عرض قائمة المشتركين",4)
        fe.addLabel(home, '\n', 5)
        fe.addBttn(home, deleteASubscriber, "حذف مشترك ", 6)
        fe.addLabel(home, '\n', 7)
        fe.addBttn(home, addNewUser, " إضافة حساب جديد ", 8)

    else:
        for i in range(3):
            fe.addLabel(home, '\n', i)
        fe.addBttn(home, AddAFarmer, "إضافة مشترك جديد ", 4)
        fe.addLabel(home, '\n', 5)
        fe.addBttn(home, ViewSubscriberList, "عرض قائمة المشتركين", 6)
        fe.addLabel(home, '\n', 7)

    # showing the home page
    home.pack()
