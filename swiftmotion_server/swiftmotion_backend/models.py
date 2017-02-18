from django.db import models


class SensorEntry(models.Model):
    time_stamp = models.FloatField(verbose_name=('Time Stamp'))
    qx_sensor1 = models.FloatField(verbose_name=('Qx Sensor 1'))
    qy_sensor1 = models.FloatField(verbose_name=('Qy Sensor 1'))
    qz_sensor1 = models.FloatField(verbose_name=('Qz Sensor 1'))
    qw_sensor1 = models.FloatField(verbose_name=('Qw Sensor 1'))
    head_sensor1 = models.FloatField(verbose_name=('Heading Sensor 1'))
    pitch_sensor1 = models.FloatField(verbose_name=('Pitch Sensor 1'))
    roll_sensor1 = models.FloatField(verbose_name=('Roll Sensor 1'))
    qx_sensor2 = models.FloatField(verbose_name=('Qx Sensor 2'))
    qy_sensor2 = models.FloatField(verbose_name=('Qy Sensor 2'))
    qz_sensor2 = models.FloatField(verbose_name=('Qz Sensor 2'))
    qw_sensor2 = models.FloatField(verbose_name=('Qw Sensor 2'))
    head_sensor2 = models.FloatField(verbose_name=('Heading Sensor 2'))
    pitch_sensor2 = models.FloatField(verbose_name=('Pitch Sensor 2'))
    roll_sensor2 = models.FloatField(verbose_name=('Roll Sensor 2'))
    lat_pos = models.FloatField(verbose_name=('Lateral Position'))
    lat_bend = models.FloatField(verbose_name=('Lateral Bending'))
    lat_twist = models.FloatField(verbose_name=('Lateral Twist'))
    lat_vel = models.FloatField(verbose_name=('Lateral Velocity'))
    bend_vel = models.FloatField(verbose_name=('Bending Velocity'))
    twist_vel = models.FloatField(verbose_name=('Twist Velocity'))
    lat_acc = models.FloatField(verbose_name=('Lateral Acceleration'))
    bend_acc = models.FloatField(verbose_name=('Bending Acceleration'))
    twist_acc = models.FloatField(verbose_name=('Twist Acceleration'))
    vbat = models.FloatField(verbose_name=('Battery Voltage'))
