class TimeMap {

    Map<String, ArrayList<Pair>> map; 

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!map.containsKey(key)) {
            map.put(key, new ArrayList<Pair>());
        }
        map.get(key).add(new Pair(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if (map.containsKey(key)) {

            ArrayList<Pair> values = map.get(key);
            String solution = "";

            int left = 0;
            int right = values.size() - 1;

            while (left <= right) {
                int mid = (left + right) / 2;

                if (values.get(mid).getTimestamp() <= timestamp) {
                    solution = values.get(mid).getValue();
                    left = mid + 1;
                }
                else {
                    right = mid - 1;
                }
            }

            return solution;
        }
        else {
            return "";
        }
    }
}

class Pair {
    String value;
    int timestamp;

    public Pair(String value, int timestamp) {
        this.value = value;
        this.timestamp = timestamp;
    }

    public String getValue() {
        return this.value;
    }

    public int getTimestamp() {
        return this.timestamp;
    }
}