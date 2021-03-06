from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    text = models.CharField(max_length=128)


    def __unicode__(self):
        return u'<Tag: %s>' % (self.text, )


class Tip(models.Model):

    featured = models.BooleanField(default=False)

    text = models.TextField()
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='tip_images/', blank=True)

    author = models.CharField(max_length=32, blank=True)
    tags = models.ManyToManyField('Tag')
    submit_time = models.DateTimeField(default=now)


    def __unicode__(self):
        return u'<Tip: %s>' % (self.text, )


    def to_json(self, string=False):
        tags = [{'tag_id': tag.pk, 'text': tag.text}
                for tag in self.tags]

        return {
            'featured': self.featured,
            'text': self.text,
            'url': self.url,
            'image': self.image,
            'author': self.author,
            'tags': tags,
            'submit_time': self.submit_time,
        }


    def getVoteCount(self):
        return self.vote_set.count()


class Vote(models.Model):

    tip = models.ForeignKey('Tip')
    submit_time = models.DateTimeField(default=now)
    ip_addr = models.CharField(max_length=15)


    def __unicode__(self):
        return u'<Vote from %s for %s>' % (self.ip_addr, self.tip, )

