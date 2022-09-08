package unit2;

public class StackTest
{ public static void main(String[] args)
{ Stack<Integer> myStack = new ArrayStack<Integer>();
    System.out.println("Stack contents:" + myStack);
    try
    { System.out.println("top is "+myStack.top());
    }
    catch (StackException e)
    { System.out.println("EXCEPTION: " + e.toString());
    }
    myStack.push(5);
    System.out.println("Stack contents:" + myStack);
    try
    { System.out.println("top is "+myStack.top());
    }
    catch (StackException e)
    { System.out.println("EXCEPTION: " + e.toString());
    }
}
}