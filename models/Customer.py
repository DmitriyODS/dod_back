from dataclasses import dataclass


@dataclass
class Customer:
    id: int = 0
    fio: str = ''
    city: str = ''
    class_school: str = ''
    school: str = ''
    email: str = ''
    type_mk: int = 0

    def validate(self):
        if self.fio == '':
            return False, 'ФИО не заполнено'
        if self.email == '':
            return False, 'Email не заполнен'
        if self.class_school == '':
            return False, 'Класс не заполнен'
        if self.school == '':
            return False, 'Школа не заполнена'
        if self.city == '':
            return False, 'Город не заполнен'
        if self.type_mk == 0:
            return False, 'Мастер-класс не заполнен'

        return True, 'ok'

    def parse_from_row(self, row):
        pass

    def placeholder_add(self):
        return self.fio, self.city, self.class_school, self.school, self.email, self.type_mk

    def placeholder_update(self):
        return self.fio, self.city, self.class_school, self.school, self.email, self.type_mk, self.id

    def to_dict(self):
        return {
            'id': self.id,
            'fio': self.fio,
            'email': self.email,
            'school': self.school,
            'class_school': self.class_school,
            'type_mk': self.type_mk,
            'city': self.city
        }
