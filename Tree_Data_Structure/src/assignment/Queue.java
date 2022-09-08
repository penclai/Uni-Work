package assignment;

public interface Queue<T> {
    public void createpq() ;
    public void addtopq(String o , int priority);
    public T front() ;
    public boolean isEmpty() ;
    public void deleteFront() ;
    public void frontpri() ;
}
class QueueException extends RuntimeException{
    QueueException(String s) {
        super("tried to apply" + s + "empty queue");
    }
}
