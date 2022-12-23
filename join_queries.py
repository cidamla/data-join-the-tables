import sqlite3

conn = sqlite3.connect('/Users/damlacidamkartal/code/cidamla/data-join-the-tables/data/ecommerce.sqlite')
db = conn.cursor()

def detailed_orders(db):
    query = '''SELECT o.OrderID, c.ContactName, e.FirstName
            FROM Customers AS c
            JOIN Orders AS o ON c.CustomerID = o.CustomerID
            JOIN Employees AS e ON o.EmployeeID = e.EmployeeID '''
    db.execute(query)
    results = db.fetchall()
    return results

def spent_per_customer(db):
    query = '''SELECT c.ContactName, SUM(od.UnitPrice*od.Quantity) AS TotalAmount
            FROM OrderDetails AS od
            JOIN Orders AS o ON o.OrderID = od.OrderID
            JOIN Customers AS c ON  o.CustomerID = c.CustomerID
            GROUP BY o.CustomerID
            ORDER BY TotalAmount ASC'''
    db.execute(query)
    results = db.fetchall()
    return results

'''return the total amount spent per customer ordered by ascending total amount (to 2 decimal places)
Example :
    Jean   |   100
    Marc   |   110
    Simon  |   432
    ...'''


def best_employee(db): ####
    query = '''SELECT e.FirstName, e.LastName, SUM(od.Quantity*od.UnitPrice) as c
            FROM Orders AS o
            JOIN OrderDetails AS od ON o.OrderID = od.OrderID
            JOIN Employees AS e ON  o.EmployeeID = e.EmployeeID
            GROUP BY e.EmployeeID
            ORDER BY c DESC'''
    db.execute(query)
    results = db.fetchall()
    return results[0]

'''Implement the best_employee method to determine who's the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''

def orders_per_customer(db):
    query = '''SELECT c.ContactName,COUNT(o.OrderID) AS total
            FROM Customers AS c
            LEFT JOIN Orders AS o ON c.CustomerID = o.CustomerID
            GROUP BY c.ContactName
            ORDER BY total ASC'''
    db.execute(query)
    results = db.fetchall()
    return results

    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
