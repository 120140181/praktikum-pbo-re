import random

class Father:
    def __init__(self, blood_types):
        self.blood_types = blood_types  # contoh: ['A', 'O']

class Mother:
    def __init__(self, blood_types):
        self.blood_types = blood_types  # contoh: ['B', 'O']

class Child:
    def __init__(self, father, mother):
        self.father_allele = random.choice(father.blood_types)
        self.mother_allele = random.choice(mother.blood_types)
        self.blood_types = [self.father_allele, self.mother_allele]
        self.blood_group = self.determine_blood_group()

    def determine_blood_group(self):
        alleles = sorted(self.blood_types)
        if alleles == ['A', 'B']:
            return 'AB'
        elif 'A' in alleles:
            return 'A'
        elif 'B' in alleles:
            return 'B'
        else:
            return 'O'

    def __str__(self):
        return f"Golongan darah anak: {self.blood_group} (dari {self.blood_types})"


# Contoh penggunaan
ayah = Father(['A', 'O'])
ibu = Mother(['B', 'O'])
anak = Child(ayah, ibu)
print(anak)
