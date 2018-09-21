def search_bst(root, val):
    if root:
        if root.val is None:
            return None
        if root.val > val:
            return search_bst(root.left, val)
        elif root.val < val:
            return search_bST(root.right, val)
        else:
            return root
