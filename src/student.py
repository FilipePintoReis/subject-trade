class Student:
    def __init__(self, student_id, subjects_and_classes, subject_targets, subject_give_ins, buddies, alone = True, gave_in = False, target= False ):
        self.student_id = student_id
        self.subjects_and_classes = subjects_and_classes 
        self.subject_targets = subject_targets
        self.subject_give_ins = subject_give_ins
        self.buddies = buddies
        self.gave_in = gave_in 
        self.alone = alone 
        self.target = target 
    
    def add_subject_and_class(self, subject_name, class_number):
        self.subjects_and_classes[subject_name] = class_number

    def add_subject_target(self, subject_name, class_number):
        self.subject_targets[subject_name].append(class_number)

    def remove_subject_target(self,subject_name):
        del self.subject_targets[subject_name]

    def add_subject_give_in(self, subject_name, class_number):
        self.subject_give_ins[subject_name].append(class_number)

    def add_buddies(self, subject_name, buddies_up):
        for buddy in buddies_up:
            if subject_name in self.buddies.keys(): 
                self.buddies[subject_name].append(buddy)
            else: self.buddies[subject_name] = [buddy]

    def get_class_for_subject(self, subject):
        if subject in self.subjects_and_classes :
            return self.subjects_and_classes[subject]
        return None

    def set_class_for_subject(self, subject, subject_class):
        if subject in self.subjects_and_classes:
            self.subjects_and_classes[subject] = subject_class

    def get_targets_for_subject(self, subject):
        if subject in self.subject_targets:
            return self.subject_targets[subject]
        return None

    def __str__(self):
        return "\nID: " + str(self.student_id) + "\nClasses: " + str(self.subjects_and_classes) + "\nTarget Classes: " + str(self.subject_targets) + "\nGive ins" + str(self.subject_give_ins)
         
    def get_giveins_for_subject(self, subject):
        if subject in self.subject_give_ins:
            return self.subject_give_ins[subject]
        return None

    def __eq__(self, x):
        return self.student_id == x.student_id