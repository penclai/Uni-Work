package unit4;

public class TestBST {

    public static void main (String [] args) {

        BST b = new BST() ;

        b.insert(4);
        b.insert(5);
        b.insert(1);
        b.insert(7);
        b.insert(3);

        System.out.println(b);

    }
}
