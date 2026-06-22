class MinStack {

    Stack<Integer> stack;
    Stack<Integer> minimum;

    public MinStack() {
        stack = new Stack<>();
        minimum = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);

        if (!minimum.isEmpty()) {
            minimum.push(Math.min(minimum.peek(), val));
        }
        else {
            minimum.push(val);
        }
    }
    
    public void pop() {
        stack.pop();
        minimum.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minimum.peek();
    }
}
