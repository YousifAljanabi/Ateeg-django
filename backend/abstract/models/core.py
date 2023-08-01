from django.db import models
from django.conf import settings
from django.utils import timezone
from backend.abstract.utils import get_related_objects
import contextlib


class IntEntityQuerySet(models.QuerySet):
    def canceled(self):
        return self.filter(is_canceled=True)

    def preserved(self):
        return self.filter(is_canceled=False)

    def enabled(self):
        return self.filter(is_enabled=True)


class IntEntity(models.Model):
    objects = IntEntityQuerySet.as_manager()
    
    class Meta:
        abstract = True

    is_enabled = models.BooleanField(default=True)
    is_canceled = models.BooleanField(default=False)

    canceled_at = models.DateTimeField(editable=False, null=True, blank=True)
    canceled_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_canceled_by",
    )
    restored_at = models.DateTimeField(editable=False, null=True, blank=True)
    restored_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_restored_by",
    )

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    extra = models.JSONField(null=True, blank=True, default=dict)

    def cancel(self, user):
        to_cancel = get_related_objects(self)

        for obj in to_cancel:
            with contextlib.suppress(Exception):
                obj.cancel(user)

        self.is_canceled = True
        self.canceled_by = user
        self.canceled_at = timezone.now()
        self.save()

    def restore(self, user):
        to_restore = get_related_objects(self)

        for obj in to_restore:
            with contextlib.suppress(Exception):
                obj.restore(user)

        self.is_canceled = False
        self.restored_by = user
        self.restored_at = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if self.is_canceled:
            raise Exception("Cannot save canceled object")

        super().save(*args, **kwargs)
