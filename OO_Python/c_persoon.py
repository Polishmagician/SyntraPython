class persoon:
    #Constructor met eigenschappen naam, leeftijd, hobby
    def __init__(self,naam,leeftijd,hobby):
        self.naam = naam
        self.leeftijd = leeftijd
        self.hobby = hobby
    def stel_jezelf_voor(self):
        print(f"ik ben {self.naam} en ik ben {self.leeftijd} jaar oud "
              f"en mijn hobby is {self.hobby}")

    def __str__(self):
        return (f"ik ben {self.naam} en ik ben {self.leeftijd} jaar oud "
              f"en mijn hobby is {self.hobby}")


# p = persoon("Bjorn",33,"Piano spelen")
# # p.stel_jezelf_voor()
# print(p)