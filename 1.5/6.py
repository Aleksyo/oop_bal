# здесь пишите программу
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *memory):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = memory[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память:' + ';'.join([f' {el.name} - {el.volume}' for el in self.mem_slots])]


mb = MotherBoard('AORUS', CPU('Ryzen', 3700), Memory('Kingstone', 8000), Memory('Kingstone', 8000))
