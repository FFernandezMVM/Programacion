from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, matricula, model, kms_inicials):
        self.matricula = matricula
        self._model = model       # Protegit (un guió)
        self.__kms = kms_inicials # Privat (dos guions)
    
    # TASCA: Fes el Getter per llegir els kms (ja que és privat)
    def llegir_kms(self):
        return self.__kms
        pass

    # TASCA: Fes el Setter amb seguretat anti-frau
    def actualitzar_kms(self, nous_kms): 
        if nous_kms < self.__kms:
            return False
        else:
            self.__kms = nous_kms   
            return True
        # Si nous_kms és més petit que self.__kms, retorna False.
        # Si és correcte, actualitza i retorna True.
        pass
    @abstractmethod
    def calcular_preu(self, dies):
        pass

class Esportiu(Vehicle):
    def __init__(self, matricula, model, kms_inicials):
                self.matricula = matricula
                self._model = model       # Protegit (un guió)
                self.__kms = kms_inicials # Privat (dos guions)

    def calcular_preu(self, dies):
         preu_esportiu = 100
         return dies * preu_esportiu
        

class Camio(Vehicle):
    def __init__(self, matricula, model, kms_inicials, tones):
            self.matricula = matricula
            self._model = model       # Protegit (un guió)
            self.__kms = kms_inicials # Privat (dos guions)
            self.tones = tones

    def calcular_preu(self, dies):
        preu_base = 50
        preu_per_tona = 20
        return (dies * preu_base) + (self.tones * preu_per_tona)
        pass    
