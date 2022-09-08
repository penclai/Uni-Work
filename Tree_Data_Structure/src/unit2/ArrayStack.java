package unit2;

public class ArrayStack<T> implements Stack<T>
{ private T[] arr;
    private int cursor;

    public ArrayStack()
    { arr = (T[])new Object[5];
        cursor = -1;
    }

    public void push(T x)
    { cursor++;
        if (cursor==arr.length)
        { T[] temp = (T[])new Object[arr.length+5];
            for (int i=0; i<arr.length; i++)
                temp[i] = arr[i];
            arr = temp;
            System.out.println("Array size increased to " + arr.length);
        }
        arr[cursor] = x;
    }

    public void pop()
    { if (cursor==-1)
        throw new StackException("pop");
        cursor--;
    }

    public boolean isEmpty()
    { return(cursor==-1);
    }

    public T top()
    { if (cursor==-1)
        throw new StackException("top");
        return(arr[cursor]);
    }

    public String toString()
    { if (cursor==-1) return "<empty>";
    else
    { StringBuffer sb = new StringBuffer();
        for (int i = 0; i<=cursor; i++)
        { sb.append(arr[i]);
            sb.append(',');
        }
        sb.setLength(sb.length()-1); //remove the last comma
        return(sb.toString());
    }
    }
}