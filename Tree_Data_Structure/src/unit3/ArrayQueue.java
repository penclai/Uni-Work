package unit3;

// incomplete array-based implementation of queues
public class ArrayQueue<T> implements Queue<T>
{ private T[] arr;
    private int frontPos, backPos;

    public ArrayQueue()
    { arr = (T[])new Object[5];
        backPos = -1;
        frontPos = 0;
    }

    public boolean isEmpty()
    { return frontPos==(backPos+1)%arr.length;
    }

    public T front()
    { if (frontPos==(backPos+1)%arr.length)
        throw new QueueException("front");
        return arr[frontPos];
    }

    public void removeFront()
    { if (frontPos==(backPos+1)%arr.length)
        throw new QueueException("removeFront");
        frontPos = (frontPos+1)%arr.length;
    }

    public String toString()
    { if (frontPos==(backPos+1)%arr.length)
        return "<>";

        StringBuffer sb = new StringBuffer();

        sb.append('<');

        int pos = frontPos;
        while (pos!=backPos)
        { sb.append(arr[pos]);
            sb.append(',');
            pos = (pos+1)%arr.length;
        }

        sb.append(arr[backPos]);
        sb.append('>');

        return(sb.toString());
    }

    public void add(T x)
    {
    }
}