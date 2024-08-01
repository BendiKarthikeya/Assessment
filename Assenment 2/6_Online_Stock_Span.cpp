class StockSpanner {
public:
    stack<pair<int,int>> s;
    StockSpanner() {}
    
    int next(int price) {
        long long int count=1;
        while(s.size()!=0 && s.top().first<=price){
            count=count+s.top().second;
            s.pop();
        }
        s.push({price,count});
        return count;
    }
};