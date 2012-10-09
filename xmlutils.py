def remove_whitespace_nodes(node, unlink=False):
    """Removes all of the whitespace-only text decendants of a DOM node.
    
    When creating a DOM from an XML source, XML parsers are required to
    consider several conditions when deciding whether to include
    whitespace-only text nodes. This function ignores all of those
    conditions and removes all whitespace-only text decendants of the
    specified node. If the unlink flag is specified, the removed text
    nodes are unlinked so that their storage can be reclaimed. If the
    specified node is a whitespace-only text node then it is left
    unmodified.
    
    original function by Brian Quinlan http://code.activestate.com/recipes/303061/
    CW - replaced dom.Node.TextNode explicity with 3 - not sure why dom isnt defined
    CW - renamed whilespace to whitespace

    """
    
    remove_list = []
    for child in node.childNodes:
        if child.nodeType == 3 and \
           not child.data.strip():
            remove_list.append(child)
        elif child.hasChildNodes():
            remove_whitespace_nodes(child, unlink)
    for node in remove_list:
        node.parentNode.removeChild(node)
        if unlink:
            node.unlink()

def mark_ids(node) :
   """ mark id attributes as IDs so that getElementById() works 
   
   """
   try:
     node.setIdAttribute("id")
   except:
     pass

   for child in node.childNodes :
       mark_ids(child)


def get_elements(node,tag) :
   return  node.getElementsByTagName(tag)

def get_value(node,tag) :
   return get_elements(node,tag)[0].firstChild.nodeValue

