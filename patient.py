class Patient:
    # Every patient object initialized has name and age
    def __init__(self,name, age):
        self.demographics = {'patient_name': name,
                             'patient_age': age}
        self.labs = {}
    def add_lab_values(self):
        new_lab_entry = None
        while new_lab_entry != "done":
            new_lab_entry = input("Which lab has new values? (Use format PTT = 1.3 when entering values\n Write 'done' when finished.")
            new_entry_list = new_lab_entry.split("=")
            new_lab_name = new_entry_list[0].strip()
            new_lab_value = float(new_entry_list[1].strip())
            self.labs[new_lab_name] = new_lab_value



