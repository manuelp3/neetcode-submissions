#include <vector>
using namespace std;

class ListNode {
    public:
        int val;
        ListNode *next;

        ListNode(int val) {
            this->val = val;
            next = nullptr;
        }

        ListNode(int val, ListNode *next) {
            this->val = val;
            this->next = next;
        }
    };

class LinkedList {
private:
    ListNode *head; 
    ListNode *tail;
public:
    LinkedList() {
        this->head = new ListNode(-1);
        this->tail = head;
    }

    int get(int index) {
        int count = 0;
        for (ListNode *ptr = head->next; ptr != nullptr; ptr = ptr->next) {
            if (count == index) {
                return ptr->val;
            }
            count++;
        }
        return -1;
    }

    void insertHead(int val) {
        ListNode* insert = new ListNode(val, head->next);
        head->next = insert;
        if (insert->next == nullptr) {
            this->tail = insert;
        }
    }
    
    void insertTail(int val) {
        ListNode *tail2 = new ListNode(val, nullptr);
        this->tail->next = tail2;
        this->tail = tail2;
    }

    bool remove(int index) {
        int i = 0;
        ListNode* curr = head;
        while (i < index && curr != nullptr) {
            i++;
            curr = curr->next;
        }

        // Remove the node ahead of curr
        if (curr != nullptr && curr->next != nullptr) {
            if (curr->next == tail) {
                tail = curr;
            }
            ListNode* toDelete = curr->next;
            curr->next = curr->next->next;
            delete toDelete;
            return true;
        }
        return false;

        // int count = 0;
        // ListNode *prev = head;

        // for (ListNode *ptr = head->next; ptr != nullptr; ptr = ptr->next) {
        //     if (count == index) {
        //         if (ptr->next == nullptr) {
        //             ptr = nullptr;
        //             return true;
        //         }
        //         prev->next = ptr->next;
        //         delete ptr;
        //         return true;
        //     }
        //     count++;
        //     prev = ptr;
        // }
        // return false;
    }

    vector<int> getValues() {
        vector<int> vec {};

        for (ListNode *ptr = head->next; ptr != nullptr; ptr = ptr->next) {
            vec.push_back(ptr->val);
        }
        return vec;
    }
};
