package unit2;

import java.util.LinkedList;
import java.util.List;

class ListCell<T>
{ T data;
    ListCell<T> next;

    public ListCell(T x, ListCell<T> c)
    { data = x;
        next = c;
    }
}

class ListException extends RuntimeException
{ public ListException(String s)
{ super(s);
}
}

public class LList<T> {
    private ListCell<T> front;

    public LList() {
        front = null;
    }

    public void addToFront(T x) {
        front = new ListCell<T>(x, front);
    }

    public void addToBack(T x) {
        if (front == null)
            front = new ListCell<T>(x, front);
        else {
            ListCell<T> c = front;
            while (c.next != null)
                c = c.next;
            c.next = new ListCell<T>(x, null);
        }
    }

    public T elementAt(int n) {
        ListCell<T> c = front;
        for (int i = 0; i < n; i++) {
            if (c == null)
                throw new ListException("no element at position " + n);
            c = c.next;
        }
        if (c == null)
            throw new ListException("no element at position " + n);
        return c.data;
    }

    public int length() {
        ListCell<T> c = front;
        int result = 0;
        while (c != null) {
            result++;
            c = c.next;
        }
        return result;
    }

    public String toString() {
        StringBuffer sb = new StringBuffer("<");
        ListCell<T> c = front;
        while (c != null) {
            if (c != null)
                sb.append(c.data).append(", ");
            c = c.next;


        }
        return (sb + ">");
    }

    public int find(T x) {
        int i = 1;
        ListCell<T> c = front;
        while (c.data != x) {
            c = c.next;
            i++;
            if (c.next == null) {
                return -1;
            }
        }
        return i;
    }

    public boolean removeAll(T x) {
        ListCell<T> c = front;
        boolean found = false;
        while (c != null) {
            if (c.data == x) {

                found = true;
            }
        }
        return found ;
    }
}