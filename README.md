# Django Signals & Custom Class Assignment



## Topic: Django Signals

#### Question 1:By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


**Answer:**  
By default, Django signals are executed synchronously**.  

**Code Proof:**  
logged the time before and after the signal fired to show the execution is sequential and blocking.

---

#### Question 2:Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer:**  
Yes, Django signals by default run in the same thread** as the function that triggered them.

**Code Proof:**  
printed the current thread's identity in both the view and signal handler to show both matched.

---

####  Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
**Answer:**  
Yes, if a signal is triggered during a transaction, it runs within the same database transaction

**Code Proof:**  
used `transaction.get_connection().in_atomic_block` to confirm both the view and signal handler shared the same DB transaction state.

---

## Topic: Custom Classes in Python

### Description:


###  Example Usage:

```python
rec = Rectangle(5, 10)

for i in rec:
    print(i)

# Output:
# {'length': 5}
# {'width': 10}
 
