from django.db import models

NULLABLE = {"blank": True, "null": True}

class Employees(models.Model):
    """ Модель сотрудников """

    name = models.CharField(max_length=255, verbose_name="ФИО сотрудника")
    specialization = models.CharField(max_length=255, verbose_name="Специальность")
    avatar = models.ImageField(upload_to="evacuator/employees", **NULLABLE)
    comment = models.TextField(verbose_name="Дополинительные сведения", **NULLABLE)

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    """Модель услуг"""
    service_name = models.CharField(max_length=255, verbose_name="Название услуги")
    price = models.CharField(max_length=10, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание услуги", **NULLABLE)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["service_name"]

    def __str__(self):
        return f"{self.service_name} - {self.price} руб."


class Contact(models.Model):
    """Модель обратной связи"""

    submitted_at = models.DateTimeField(
        verbose_name="Дата и время отправки",
        auto_now_add=True,
    )

    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
    )
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        **NULLABLE,
    )

    photo = models.ImageField(upload_to="evacuator/contact", **NULLABLE,)

    message = models.TextField(
        verbose_name="Сообщение",
        null=True,
        blank=True,
        help_text="Если вы хотите получить ответ, оставьте свой номер телефона. Если желаете оставить отзыв, можете не оставлять номер"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

class Static(models.Model):
    """Модель статичной страницы компании"""

    company = models.TextField(verbose_name="О компании")
    about = models.TextField(verbose_name="О нас", **NULLABLE)
    history = models.TextField(verbose_name="История", **NULLABLE)
    values = models.TextField(verbose_name="Ценности", **NULLABLE)
    address = models.TextField(max_length=255, verbose_name="Адрес", **NULLABLE)
    phone = models.CharField(max_length=255, verbose_name="Телефон", **NULLABLE)
    cooperation = models.TextField(verbose_name="Сотрудничество", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Статика"
        verbose_name_plural = "Статика"



class Eva(models.Model):
    """ Модель техники """

    name = models.CharField(max_length=255, verbose_name="название техники")
    Weight = models.CharField(max_length=255, verbose_name="Грузоподьемность")
    avatar = models.ImageField(upload_to="evacuator/eva", **NULLABLE)
    comment = models.TextField(verbose_name="Описание", **NULLABLE)

    class Meta:
        verbose_name = "Техника"
        verbose_name_plural = "Техника"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class FAQ(models.Model):
    """ Модель вопрос-ответ """

    question = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["question"]

    def __str__(self):
        return f"{self.question} - {self.answer}"