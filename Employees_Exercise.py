
class employee:
    
    def __init__(self, name, position, contract_start_date):
        """
        Inicialización de la clase employee
        
        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        position : TYPE
            DESCRIPTION.
        contract_start_date : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        self.name = name
        self.position = position
        self.contract_start_date = contract_start_date
        
    
    def Name_Position(self):
        """
        Función que muestra el nombre del trabajador y su puesto
        
        Returns
        -------
        None.

        """
        
        print(f"El trabajador se llama {self.name} y su puesto es {self.position}")



class Full_Time(employee):
    
    def __init__(self, name, position, contract_start_date, annual_salary):
        """
        Inicialización de la clase Full_Time la cual heredará de la clase employee

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        position : TYPE
            DESCRIPTION.
        contract_start_date : TYPE
            DESCRIPTION.
        annual_salary : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        super().__init__(name, position, contract_start_date)
        self.annual_salary = annual_salary
        
        
    def Name_Position(self):
        """
        Función que muestra el nombre del trabajador y su puesto

        Returns
        -------
        None.

        """
        
        
        super().Name_Position()
        
        
    def Pay_Salary(self):
        """
        Función que muestra el pago mensual del empleado

        Returns
        -------
        None.

        """
        
        print(f"Al empleado {self.name} se le pagará cada mes {self.annual_salary/12} €")
        
        return self.annual_salary/12


class Part_Time (Full_Time):
    
    def __init__(self, name, position, contract_start_date, weely_hours, annual_salary, annual_hours):
        """
        Inicialización de la clase Part_Time, la cual hereda de la clase Full_Time

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        position : TYPE
            DESCRIPTION.
        contract_start_date : TYPE
            DESCRIPTION.
        weely_hours : TYPE
            DESCRIPTION.
        annual_salary : TYPE
            DESCRIPTION.
        annual_hours : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        
        super().__init__(name, position, contract_start_date, annual_salary)
        self.weely_hours = weely_hours
        self.annual_hours = annual_hours
        
        
    def Name_Position(self):
        """
        Función que muestra el nombre del trabajador y su puesto

        Returns
        -------
        None.

        """
            
        super().Name_Position()
        
        
    def Pay_Salary(self):
        """
        Función que muestra el pago mensual del empleado

        Returns
        -------
        None.

        """
        
        print(f"Al empleado {self.name} se le pagará cada mes {self.annual_salary/12} €")
        
        

class Contractor(employee):
    
    def __init__(self, name, position, contract_start_date, contract_end_date, hourly_salary, total_paid, worked_hours, pending_bill):
        """
        Inicialización de la clase Contractor, la cual hereda de la clase employee

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        position : TYPE
            DESCRIPTION.
        contract_start_date : TYPE
            DESCRIPTION.
        contract_end_date : TYPE
            DESCRIPTION.
        hourly_salary : TYPE
            DESCRIPTION.
        total_paid : TYPE
            DESCRIPTION.
        worked_hours : TYPE
            DESCRIPTION.
        pending_bill : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        
        super().__init__(name, position, contract_start_date)
        self.contract_end_date = contract_end_date
        self.hourly_salary = hourly_salary
        self.total_paid = total_paid
        self.worked_hours = worked_hours
        self.pending_bill = pending_bill
        
        
    def add_hours(self, horas_extra):
        """
        Función que añade el parámetro "horas" a las horas trabajadas y se actualiza
        la factura pendiente

        Parameters
        ----------
        horas_extra : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
          
        self.worked_hours = self.worked_hours + horas_extra
        
        self.pending_bill = self.pending_bill + (self.hourly_salary * horas_extra)
        
        print(f"Las horas trabajadas son {self.worked_hours} y la cuenta pendiente es {self.pending_bill}")
        
        
    def pay(self):
        """
        Función que paga la factura pendiente y actualiza el pago total

        Returns
        -------
        None.

        """
        
        self.total_paid = self.total_paid + self.pending_bill
        print(f"Al trabajador {self.name} se le paga {self.pending_bill}")
        self.pending_bill = 0
        
        
        
        
trabajador = employee("Dani", "Empleado", "19 de enero")
trabajador1 = Full_Time("Dani", "Full-Time", "19 de enero", 30000)
trabajador2 = Part_Time("Dani", "Part-Time", "19 de enero", "40", 24000, "2120")
trabajador3 = Contractor("Dani", "Contractor", "19 de enero", "24 de mayo", 20, 4500, 950, 1500)

#trabajador.Name_Position()
#trabajador1.Name_Position()
#trabajador1.Pay_Salary()
#trabajador2.Name_Position()
#trabajador2.Pay_Salary()
#trabajador2.Name_Position()
#trabajador3.Name_Position()
#trabajador3.add_hours(100)
#trabajador3.pay()
        