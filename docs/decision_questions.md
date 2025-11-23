x# Decision Questions

This document contains the questionnaire used by the system to determine the most suitable data structure for the user's problem.

All questions are based strictly on the content covered in LIS2032:

- Arrays  
- Stacks  
- Queues  
- Linked Lists  
- Trees (BST)  
- Heaps  
- Graphs  

---

## ✅ Questionnaire (7 Questions)

Below are the final 7 questions used in the system.

### **1. Do you need fast access by index (A[i])?**
- If yes → an **Array** is a strong candidate.
- Arrays provide O(1) positional access.

---

### **2. Are your operations mainly LIFO (Last-In First-Out)?**
- If yes → **Stack**.
- Stacks represent undo operations, recursion, call stacks, etc.

---

### **3. Are your operations mainly FIFO (First-In First-Out)?**
- If yes → **Queue**.
- Queues represent scheduling, print jobs, line order, etc.

---

### **4. Will you insert/delete many elements in the middle of the collection?**
- If yes → **Linked List**.
- Linked lists allow O(1) insert/delete when the pointer is known.

---

### **5. Do you need the data to remain sorted at all times?**
- If yes → **Binary Search Tree (BST)**.
- BSTs allow ordered traversal and maintain sorted structure.

---

### **6. Do you need to manage priorities (always extract max/min first)?**
- If yes → **Heap**.
- Heaps provide O(log n) insertion and priority extraction.

---

### **7. Does your problem involve nodes connected as a network?**
- If yes → **Graph**.
- Used for routes, maps, social networks, and connection modeling.

---

## 📌 Final Note
These questions map directly to deterministic decision rules stored in `decision_rules.md`.

