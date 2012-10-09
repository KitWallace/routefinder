from xml.dom.minidom import parse
import presenter
import xmlutils

class Menu(object) :
    """ a menu represents a menu and its current status 
     
     attributes
       name - the name of the menu
       root  - the base of the menu
       current  - the current item in the menu  

    """
    
    def __init__(self,name) :
        """ create a menu object from an XML   file 

        file is the name of an XML file which conforms to the schema: 

        DOM parse  is used to parse the XML and build the tree of XML objects. 
        whitespace text nodes are deleted 
  
        """
        self.name = name
        self.doc = parse("menu/"+name +".xml")
        self.root = self.doc.firstChild  #  menu 
        xmlutils.remove_whitespace_nodes(self.root)  
        xmlutils.mark_ids(self.doc)
        self.current = self.root

    def move (self,action) :
        """Using action, move the current position in the menu left ,right, up or down the tree
 
        left and right wrap round
        down goes down a level if there are sub item or is ignored
        up goes up a level until the containing Document is reached, when None is returned

        """
        if self.current is None :
            pass
        elif action == "left" : # previous item
            sib = self.current.previousSibling
            if sib is None :
                self.current= self.current.parentNode.lastChild
            else :
                self.current = sib
        elif action =="down" :  # down one level if there are children
            if self.current.hasChildNodes() :
                self.current = self.current.firstChild
            else :
                pass
        elif action == "right" : # next item 
            sib = self.current.nextSibling
            if sib is None :
                self.current = self.current.parentNode.firstChild
            else :
                self.current = sib
        elif action == "up" : # back up one level
            parent = self.current.parentNode 
            if parent is self.root.ownerDocument :
                self.current = None
            else :
                self.current = parent
              
        else :
            """ invalid action """
            print (action + " not recognised ")
            self.current = None

    def goto (self,id) :
        item = self.doc.getElementById(id)
        if item is not None :
            self.current = item

    def run(self, visit) :
        """ run walks through the menu using the keys, executing the supplied visit function as each item is visited

        the visit function will return a Item DOM object

        """
        visit(self.current)
        keypress = presenter.keypress()
        for key in keypress :
            self.move(key)
            if self.current is None :
                keypress.close()
                exit()
            else :
                visit(self.current)
                next = self.current.getAttribute("next")
                if next != "" :
                    self.goto(next)
