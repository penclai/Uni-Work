package unit2;

public interface Stack<T>
{ public void push(T x);
    public void pop();
    public boolean isEmpty();
    public T top();
}

class StackException extends RuntimeException
{ public StackException(String s)
{ super("tried to apply " + s + "to empty stack");
}
}