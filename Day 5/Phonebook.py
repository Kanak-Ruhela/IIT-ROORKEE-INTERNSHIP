phonebook = {"Father":"8946583857","Mother":"3757362940"}
new_phonebook={"Brother":"5674836577"}
phonebook.update(new_phonebook)
print(phonebook.get("Father"))
del phonebook["Mother"]
print(phonebook)
