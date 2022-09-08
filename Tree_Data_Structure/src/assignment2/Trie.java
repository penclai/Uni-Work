package assignment2;

import java.util.*;

public class Trie {
    public TrieNode root;

    public Trie() {
        root = new TrieNode();

    }

    public static void main(String[] args) {
        Trie t = new Trie();
        t.addWord("car");
        t.addWord("cat");
        t.addWord("dog");
        System.out.println(t.isWord("car"));
        System.out.println(t.isWord("dog"));
        System.out.println(t.isWord("cat"));

        System.out.println(t.getWords('c'));
    }

    public boolean addWord(String word)
    {
        String Word=word.toLowerCase();
        if(isWord(Word))
            return false;
        HashMap<Character, TrieNode> children=root.children;
        for(int i=0; i<Word.length(); i++){
            char c = Word.charAt(i);
            TrieNode t;
            if(children.containsKey(c)){
                t = children.get(c);
            }else{
                t = new TrieNode(""+(c));
                children.put(c, t);
            }

            children = t.children;

        }
        return true;
    }

    public boolean isWord(String s) {
        TrieNode t = searchNode(s.toLowerCase());

        if (t != null && t.isWord)
            return true;
        else
            return false;
    }

    public TrieNode searchNode(String str) {
        HashMap<Character, TrieNode> children = root.children;
        TrieNode t = null;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (children.containsKey(c)) {
                t = children.get(c);
                children = t.children;
            } else {
                return null;
            }
        }

        return t;
    }

    public List<String> getWords(char c) {
        String str = " ";
        List<String> list = new ArrayList<>();
        HashMap<Character, TrieNode> children = root.children;
        if(children.containsKey(c)) {
            System.out.println(children.keySet());
        }
        return list;
    }

}


class TrieNode {
    HashMap <Character,TrieNode> children;
    private String text;
    boolean isWord;


    public TrieNode() {
        children = new HashMap<>();
        text = "" ;
        isWord = false;


    }
    public TrieNode (String text) {
        this.text = text;
    }
    public TrieNode getChild(Character c)
    {
        return children.get(c);
    }
    public TrieNode insert(Character c)
    {
        if (children.containsKey(c)) {
            return null;
        }

        TrieNode next = new TrieNode(text + c.toString());
        children.put(c, next);
        return next;
    }
    public String getText()
    {
        return text;
    }
    public void setEndsWord(boolean b)
    {
        isWord = b;
    }
    public boolean endsWord()
    {
        return isWord;
    }
    public Set<Character> getValidNextCharacters()
    {
        return children.keySet();
    }

}