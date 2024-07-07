from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import wikipedia
if __name__ == '__main__':
    print(f'Текущая дата и время {datetime.now()}')
    calculate_salary()
    get_employees()
    print(wikipedia.search('Python'))   #Поиск в Википедии