from django.test import TestCase
from django.template.defaultfilters import stringfilter 
from apps.administrar_nomina.models import Cargo

class ModelsTestCase(TestCase):
    def test_Cargo_has_Charfield(self):
        Cargo= Cargo.object.create(Nombre="Contador")
        Cargo.Nombre = "Contador"
        Cargo.save()
        self.assertEqual(Cargo.CharField, stringfilter(Cargo.Nombre))
