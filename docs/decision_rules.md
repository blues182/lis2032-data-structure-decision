# Decision Rules

This document defines the deterministic rules that the system uses to recommend a data structure based on the questionnaire.

The rules are aligned with LIS2032 contents and only include structures covered during the course.

---

# ✅ Structures Considered

- Array  
- Linked List  
- Stack  
- Queue  
- Binary Search Tree (BST)  
- Heap (Priority Queue)  
- Graph  

---

# 🎯 Decision Logic (Deterministic)

The rules are evaluated **in this exact order**:

---

## **Rule 1 – LIFO behavior**
If the user answers **YES** to:
> "Are your operations mainly LIFO?"

Then the final recommendation is:

### → **Stack**

---

## **Rule 2 – FIFO behavior**
If the user answers **YES** to:
> "Are your operations mainly FIFO?"

Then:

### → **Queue**

---

## **Rule 3 – Priority handling**
If the user answers **YES** to:
> "Do you need to manage priorities (max/min first)?"

Then:

### → **Heap**

---

## **Rule 4 – Graph modeling**
If the user answers **YES** to:
> "Does your problem involve nodes connected as a network?"

Then:

### → **Graph**

---

## **Rule 5 – Ordered structure required**
If the user answers **YES** to:
> "Do you need the data to remain sorted at all times?"

Then:

### → **Binary Search Tree (BST)**

---

## **Rule 6 – Random access needed**
If the user answers **YES** to:
> "Do you need fast access by index (A[i])?"

Then:

### → **Array**

---

## **Rule 7 – Many middle insertions/deletions**
If the user answers **YES** to:
> "Will you insert/delete many elements in the middle?"

Then:

### → **Linked List**

---

## **Rule 8 – Default Case**
If none of the above rules apply, then:

### → **Array**

This is because arrays provide the simplest and most general-purpose structure.

---

# 📌 End of Rules
These rules are implemented directly in `src/main.c`.
