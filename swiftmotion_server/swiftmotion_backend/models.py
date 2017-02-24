from django.db import models

gc = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)


class RecordID(models.Model):
    company = models.CharField(max_length=64, verbose_name=('Company Name'))
    job_name = models.CharField(max_length=64, verbose_name=('Job Name'))
    last_name = models.CharField(max_length=64, verbose_name=('Employee Last Name'))
    first_name = models.CharField(max_length=64, verbose_name=('Employee First Name'))
    gender = models.CharField(max_length=2, choices=gc, verbose_name=('Gender'))
    date = models.DateField(verbose_name=('Run date'))
    number = models.IntegerField(verbose_name=('Run number'))
    task_name = models.CharField(max_length=64, verbose_name=('Task Name'))
    trial_number = models.IntegerField(verbose_name=('Trial number'))

    def __str__(self):
        return (self.company + " - " +
                self.task_name + " - " +
                str(self.trial_number))


class BackInjury(models.Model):
    load_weight = models.FloatField(verbose_name=('Load weight'))
    lift_rate = models.FloatField(verbose_name=('LBD Lift Rate'))
    freq = models.FloatField(verbose_name=('Frequency/Min'))
    ma_origin = models.FloatField(verbose_name=('Moment Arm at Origin'))
    ma_dest = models.FloatField(verbose_name=('Moment Arm at Destination'))

    def __str__(self):
        return (str(self.id) + ' - ' + str(self.load_weight))


class SensorEntry(models.Model):
    time_stamp = models.FloatField(verbose_name=('Time Stamp'))
    qx_sensor1 = models.FloatField(verbose_name=('Quaternionx  Sensor 1'))
    qy_sensor1 = models.FloatField(verbose_name=('Quaterniony  Sensor 1'))
    qz_sensor1 = models.FloatField(verbose_name=('Quaternionz  Sensor 1'))
    qw_sensor1 = models.FloatField(verbose_name=('Quaternionw Sensor 1'))
    head_sensor1 = models.FloatField(verbose_name=('Heading Sensor 1'))
    pitch_sensor1 = models.FloatField(verbose_name=('Pitch Sensor 1'))
    roll_sensor1 = models.FloatField(verbose_name=('Roll Sensor 1'))
    qx_sensor2 = models.FloatField(verbose_name=('Quaternionx  Sensor 2'))
    qy_sensor2 = models.FloatField(verbose_name=('Quaterniony  Sensor 2'))
    qz_sensor2 = models.FloatField(verbose_name=('Quaternionz  Sensor 2'))
    qw_sensor2 = models.FloatField(verbose_name=('Quaternionw  Sensor 2'))
    head_sensor2 = models.FloatField(verbose_name=('Heading Sensor 2'))
    pitch_sensor2 = models.FloatField(verbose_name=('Pitch Sensor 2'))
    roll_sensor2 = models.FloatField(verbose_name=('Roll Sensor 2'))
    delta_heading = models.FloatField(verbose_name=('Delta Heading'))
    delta_pitch = models.FloatField(verbose_name=('Delta Pitch'))
    delta_roll = models.FloatField(verbose_name=('Delta Roll'))
    vel_heading = models.FloatField(verbose_name=('Velocity Heading'))
    vel_roll = models.FloatField(verbose_name=('Velocity Roll'))
    acc_heading = models.FloatField(verbose_name=('Acceleration Heading'))
    acc_pitch = models.FloatField(verbose_name=('Acceleration Pitch'))
    record = models.ForeignKey(RecordID, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.time_stamp)

    class Meta:
        ordering = ('time_stamp',)
