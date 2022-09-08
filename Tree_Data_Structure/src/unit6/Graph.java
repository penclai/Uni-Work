package unit6;

public class Graph
{ private int numNodes;
    // vertices will be called A,B,...

    // adjacency list representation used
    // adjLists[0] will hold a reference to the first cell in a linked list containing
    //       details of the edges from A to all of its neighbours,
    // adjLists[1] will hold details of edges from B to its neighbours etc.

    private ListCell[] adjLists;

    // constructor to create a graph with n vertices and no edges
    public Graph(int n)
    { int i;
        numNodes = n;
        adjLists = new ListCell[n];
        for (i = 0; i<n; i++)
            adjLists[i] = null;
    }


    // try to add an edge (v1,v2) with weight w) - return true if succesful, false otherwise
    public boolean addEdge(char v1, char v2, int w)
    { // convert the vertex names into array positions
        int pos1 = v1-'A';
        int pos2 = v2-'A';

        // check if either of pos1 and pos2 is outside the array index range
        if (pos1<0 || pos1>=numNodes || pos2<0 || pos2>=numNodes)
        {
            System.out.println("WARNING: Invalid vertex - edge not added");
            return false;
        }

    else if (v1==v2)
    {
        System.out.println("WARNING: Invalid edge - not added");
        return false;
    }

    else if (neighbours(v1,v2))
    {
        System.out.println("WARNING: Edge already exist - not added");
        return false;
    }

    else
    { // add a new cell with values (v2,w) to the front of the list adjLists[pos1]
        adjLists[pos1] = new ListCell(v2, w, adjLists[pos1]);
        adjLists[pos2] = new ListCell(v1,w, adjLists[pos2]);
        // also add a new cell with values (v1,w) to the front of the list adjLists[pos2] - need similar line to above
        // added succesfully
        return true;
    }
    }

    public String toString()
    {
        StringBuffer sb = new StringBuffer();
        for(int i =0;i<numNodes;i++) {
            ListCell l = adjLists[i];
            char vertex = (char) ('A' + i);

            while(l!=null){
                //do not print any node twice
                if(vertex<l.vertex)
                    sb.append("("+vertex+","+l.vertex+","+l.weight+"), ");
                l=l.next;
            }
        }
        // should return a string containing all of the edges in the graph with their weights
        sb.setLength(sb.length()-2); // remove trailing ",)"
        return sb.toString();

        // to convert the array position into a vertex name simply use something like
        // char vertex = 'A'+pos;
    }

    public boolean neighbours(char v1, char v2)
    {
        ListCell l = adjLists[v1-'A'];
        while(l!=null)
            if(l.vertex==v2)
                return true;
            else
                l = l.next;

        // should return true if there's an edge from v1 to v2
        // should return false if there's no such edge
        // need to search the linked list ajdLists[v1-'A'] to see if contains a node whose vertex variable is equal to v2
        // code below is supplied just to allow file to compile
        return false;
    }

    public int edgeWeight(char v1, char v2)
    {
        ListCell l = adjLists[v1-'A'];
        while(l!=null)
            if (l.vertex==v2)
                return (l.weight);
        else
            l=l.next;
        // should return the weight of the edge from v1 to v2, or a default value (e.g. -1) if there's no such edge
        // again need to search the linked list ajdLists[v1-'A'] but this time if a node whose vertex is v2 is found have to return its weight
        // code below is supplied just to allow file to compile
        return -1;
    }
    public static void main(String [] args) {
        Graph g = new Graph(6);
        g.addEdge('C','B',6);
        g.addEdge('B','D',4);
        g.addEdge('D','C',5);
        g.addEdge('A','D',3);
        System.out.println(g);
    }
}

// linked list - each cell contains a vertex name, a weight and a reference to the next item in the list
class ListCell
{ char vertex;
    int weight;
    ListCell next;

    ListCell(char v, int w, ListCell nxt)
    { vertex = v;
        weight = w;
        next = nxt;
    }
}




