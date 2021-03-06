# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('place', self.gf('events.fields.LocationField')(max_length=255)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('vacants', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('events', ['Event'])


    def backwards(self, orm):
        
        # Deleting model 'Event'
        db.delete_table('events_event')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('events.fields.LocationField', [], {'max_length': '255'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'vacants': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['events']
