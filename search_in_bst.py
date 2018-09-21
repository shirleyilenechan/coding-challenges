def search_bst(root, val):
    if root: 
        if root.val > val:
            return searchBST(root.left, val)
        elif root.val < val:
            return searchBST(root.right, val)
        else:
            return root