class Patient:
    # Every patient object initialized gets name, age and insurance company attributes
    def __init__(self, name, age, insurer):
        self.name = name
        self.age = age
        self.insurer = insurer
        self.allinfo = {'patient_name': name,
                             'patient_age': age,
                             'insurance_company': insurer}
        self.labs = {}

    #Receives new lab value input and appends to patient labs attribute
    def add_lab_values(self):
        new_lab_entry = None
        while new_lab_entry != "done":
            new_lab_entry = input("Enter new labs(Use format PTT = 1.3 when entering values\n "
                                  "Write 'done' when finished.")
            new_entry_list = new_lab_entry.split("=")
            new_lab_name = new_entry_list[0].strip()
            new_lab_value_string = float(new_entry_list[1].strip())
            new_lab_value = int(new_lab_value_string)
            self.labs[new_lab_name] = new_lab_value

# Create gui using tkinter