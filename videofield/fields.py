from django.core import checks
from django.db import models
from django.utils.translation import ugettext_lazy as _


class VideoField(models.FileField):
    description = _('Video')

    def __init__(self, *args, **kwargs):
        self.width_field = kwargs.pop('width_field', None)
        self.height_field = kwargs.pop('height_field', None)
        self.duration_field = kwargs.pop('duration_field', None)
        self.size_field = kwargs.pop('size_field', None)

        super(VideoField, self).__init__(*args, **kwargs)

    def check(self, **kwargs):
        errors = super(VideoField, self).check(**kwargs)
        errors.extend(self._check_ffmpeg_installed())

        return errors

    def _check_ffmpeg_installed(self):
        ffmpeg_is_avaliable = False

        if not ffmpeg_is_avaliable:
            return [
                checks.Error(
                    'Cannot use VideoField because ffmpeg is not installed.',
                    hint='Get ffmpeg at https://ffmpeg.org/download.html',
                    obj=self,
                    id='videofield.E001',
                )
            ]

        return []

    def deconstruct(self):
        name, path, args, kwargs = super(VideoField, self).deconstruct()

        if self.width_field:
            kwargs['width_field'] = self.width_field
        if self.height_field:
            kwargs['height_field'] = self.height_field
        if self.duration_field:
            kwargs['duration_field'] = self.duration_field
        if self.size_field:
            kwargs['size_field'] = self.size_field

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        defaults = {'form_class': VideoFormField}
        defaults.update(kwargs)

        return super(VideoField, self).formfield(**defaults)
