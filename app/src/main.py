import database as db

def set_salary():
    name = input("Name here: ")
    salary = int(input("Your salary here: "))

    query = ("INSERT INTO revenue (name, value) VALUES (%s, %s)")
    setRevenues = (name, salary)
    
    db.cursor.execute(query,setRevenues)
    db.connect.commit()

    return salary

def set_expenses():
    
    title = (input("Name the expense: "))
    value = int(input("Value here: "))

    query = "INSERT INTO expenses (name, value) VALUES (%s, %s)" 
    setExpenses = (title, value)
    
    try:
        db.cursor.execute(query, setExpenses)
        db.connect.commit()

    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        operation = int(input("1 para ver seu salario, 2 para adicionar uma nova despesa, 3 para adicionar uma nova receita. 0 para cancelar: "))

        if operation == 1:
            
            db.cursor.execute("SELECT value FROM revenue")
            value = db.cursor.fetchall()

            print(value)

        elif operation == 2:
            set_expenses()
        
        elif operation == 3:
            set_salary()
        
        elif operation == 0:
            print("Saindo...")
            break
        else:
            print("Digite um número válido.")



if __name__ == "__main__":
    main()