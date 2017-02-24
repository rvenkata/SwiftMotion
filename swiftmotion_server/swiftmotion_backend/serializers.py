from rest_framework import serializers
from .models import RecordID, BackInjury, SensorEntry


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordID
        fields = ('company', 'job_name', 'last_name', 'first_name', 'date',
                  'number', 'task_name', 'trial_number')
        exclude = ('id',)


class BackInjurySerializer(serializers.ModelSerializer):
    class Meta:
        models = BackInjury
        fields = ('load_weight', 'lift_rate', 'freq', 'ma_origin', 'ma_dest')
        exclude = ('id',)


class SensorSerialzier(serializers.ModelSerializer):
    class Meta:
        models = SensorEntry
        fields = ('timestamp, qx_sensor1, qy_sensor1, qz_sensor1', 'qw_sensor1',
                  'head_sensor1', 'pitch_sensor1', 'roll_sensor1', 'qx_sensor2',
                  'qy_sensor2', 'qz_sensor1', 'qw_sensor2', 'head_sensor2',
                  'pitch_sensor2', 'roll_sensor2', 'delta_heading', 'delta_pitch',
                  'delta_roll', 'vel_heading', 'acc_heading', 'acc_pitch', 'record')
        exclude = ('id',)
