package unit1;

import javax.xml.soap.Node;

class ListCell
{ char data;
    ListCell next;

    public ListCell(char x, ListCell c)
    { data = x;
        next = c;
    }
}

class ListException extends RuntimeException
{ public ListException(String s)
{ super(s);
}
}

// interface for exercise 6
interface LListIterator
{ public boolean hasNext();
    public char next();
    public void remove();
}

public class LList
{ private ListCell front;

    public LList()
    { front = null;
    }

    public void addToFront(char x)
    { front = new ListCell(x, front);
    }

    public void addToBack(char x)
    { if (front==null)
        front = new ListCell(x, front);
    else
    { ListCell c = front;
        while (c.next != null)
            c = c.next;
        c.next = new ListCell(x, null);
    }
    }

    public int length() {
        ListCell c  = front ;
        int size = 0 ;
        while(c !=null) {
            c = c.next ;
            size++ ;
        }
        return size ;
    }

    public int occs(char c) {
        ListCell x = front;
        int count = 0;
        while (x != null) {
            if (x.data == c) {
                count++;
            }
            x = x.next;
        }
        return count;
    }



    public void removeFront(){
        ListCell c = front ;
        if(c == null)
            throw new ListException("List is empty ") ;
        while( c!= null ){
            if(c.next != null )
                c.next = front ;
        }

    }



    public char elementAt(int n)
    { ListCell c = front;
        if (n<0)
            throw new ListException("elementAt called with negative argument");
        for (int i = 0; i<n; i++)
        { if (c == null)
            throw new ListException("no element at position "+n);
            c = c.next;
        }
        if (c == null)
            throw new ListException("no element at position "+n);
        return c.data;
    }

    public String toString()
    { StringBuffer sb = new StringBuffer("<");
        ListCell c = front;
        while (c != null)
        { sb.append(c.data);
            c = c.next;
        }
        return(sb+">");
    }

    // main method to test the class - expected list contents shown as comments

    public static void main(String args[])

    { LList myList = new LList();// <>

        System.out.println(myList);
        myList.addToFront('c');     // <c>
        myList.addToFront('b');     // <bc>
        myList.addToFront('a');     // <abc>
        System.out.println(myList);
        myList.addToBack('d');      // <abcd>
        myList.addToBack('e');      // <abcde>
        System.out.println(myList);
        System.out.println( myList.length());
        System.out.println(myList.occs('c'));

        myList.removeFront();
        System.out.println(myList);


        for (int i = -1; i<7; i++)
            try
            { System.out.println(myList.elementAt(i));
            }
            catch (ListException e)
            { System.out.println("ERROR: "+e);
            }

    }
}