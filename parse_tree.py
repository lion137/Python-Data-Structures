from binary_trees import BinaryTree, preorder_traversal, postorder_traversal, inorder_traversal

import operator as op



def build_parse_tree(exp):
    exp_list = exp.replace('(', ' ( ').replace(')', ' ) ').split()
    e_tree = BinaryTree('')
    current_tree = e_tree
    for token in exp_list:
        if token == '(':
            current_tree.insertLeft('')
            current_tree = current_tree.getLeftChild()
        elif token in ['+','-','/','*']:
            current_tree.setRootVal(token)
            current_tree.insertRight('')
            current_tree = current_tree.getRightChild()
        elif token not in ['+','-','/','*', '(', ')']:
            current_tree.setRootVal(int(token))
            current_tree = current_tree.getParent()
        elif token == ')':
            current_tree = current_tree.getParent()
        else:
            raise ValueError

    return e_tree

def evaluate_parse_tree(tree):
    opers = {'+': op.add, '-':op.sub, '*':op.mul, '/':op.truediv}

    leftT = tree.getLeftChild()
    rightT = tree.getRightChild()

    if leftT and rightT:
        fn = opers[tree.getRootVal()]
        return fn(evaluate_parse_tree(leftT), evaluate_parse_tree(rightT))
    else:
        return tree.getRootVal()


pt = BinaryTree('')
pt = build_parse_tree("((34 * 5)+(3 + 5))")
print("pt->root", pt.getRootVal())
print("pt->root->right->right <-parent: rootVal", pt.getRightChild().getRightChild().getParent().getRootVal())
pt.preorder()
print("--------------------------------------")
postorder_traversal(pt)
print(evaluate_parse_tree(pt))
inorder_traversal(pt)
print("--------------------------------------")

print(evaluate_parse_tree(pt))