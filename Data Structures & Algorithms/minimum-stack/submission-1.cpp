class MinStack {
private: 
    stack<int> s;
    stack<int> m;
public:
    MinStack() {
    }
    
    void push(int val) {
        s.push(val);
        if (m.empty()){
            m.push(val);
        }
        else if (val <= m.top()){
            m.push(s.top());
        }
    }
    
    void pop() {
        if(s.top() == m.top()){
            m.pop();
        }
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return m.top();
    }
};
