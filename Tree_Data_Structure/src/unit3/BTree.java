package unit3;
public class BTree<T>
{ private BTNode<T> root;

    public BTree()
    { root = null;
    }

    public BTree(T o, BTree<T> l, BTree<T> r)
    { root = new BTNode<T>(o, l.root, r.root);
    }

    private BTree(BTNode<T> n)
    { root = n;
    }

    public boolean isEmpty()
    { return root==null;
    }

    public T value()
    { if (root==null)
        throw new TreeException("value");
    else
        return root.data;
    }

    public BTree<T> leftChild()
    { if (root==null)
        throw new TreeException("leftChild");
    else
        return new BTree<T>(root.left);
    }

    public BTree<T> rightChild()
    { if (root==null)
        throw new TreeException("rightChild");
    else
        return new BTree<T>(root.right);
    }

    public String toString()
    { return getString(root);
    }

    private static <T> String getString(BTNode<T> n)
    { if (n==null)
        return("");
    else
    { String s1 = getString(n.left);
        String s2 = getString(n.right);
        return s1+" "+n.data+" "+s2;
    }
    }
}

class BTNode<T>
{ T data;
    BTNode<T> left, right;

    BTNode(T i)
    { data = i;
        left = null;
        right = null;
    }

    BTNode(T o, BTNode<T> l, BTNode<T> r)
    { data = o;
        left = l;
        right = r;
    }
}

class TreeException extends RuntimeException
{ public TreeException(String s)
{ super("Tried to apply "+s+" to empty tree");
}
}

