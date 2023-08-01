from django.db import models


class ProvinceChoices(models.TextChoices):
    BAGHDAD = 'بغداد', 'بغداد'
    BASRA = 'البصرة', 'البصرة'
    NINAWA = 'نينوى', 'نينوى'
    MISAN = 'ميسان', 'ميسان'
    DIKAR = 'ذي قار', 'ذي قار'
    MUTHANA = 'المثنى', 'المثنى'
    KADISIA = 'القادسية', 'القادسية'
    NAJAF = 'النجف', 'النجف'
    KARBALA = 'كربلاء', 'كربلاء'
    WASIT = 'واسط', 'واسط'
    ANBAR = 'الأنبار', 'الأنبار'
    DIYALA = 'ديالى', 'ديالى'
    SALAHDDIN = 'صلاح الدين', 'صلاح الدين'
    SULY = 'السليمانية', 'السليمانية'
    DUHUK = 'دهوك', 'دهوك'
    ERBIL = 'أربيل', 'أربيل'
    BABIL = 'بابل', 'بابل'
    KIRKUK = 'التأميم', 'التأميم'
    OTHER = 'أخرى', 'أخرى'

