from django.db import models

class Gu0(models.Model):
    num = models.IntegerField(primary_key=True)
    gu = models.SmallIntegerField(blank=True, null=True)
    time_difference = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    temp = models.SmallIntegerField(blank=True, null=True)
    day_high_temp = models.SmallIntegerField(blank=True, null=True)
    day_low_temp = models.SmallIntegerField(blank=True, null=True)
    sky_state = models.IntegerField(blank=True, null=True)
    weather_state = models.IntegerField(blank=True, null=True)
    weather_kor = models.CharField(max_length=20, blank=True, null=True)
    rain_persent = models.IntegerField(blank=True, null=True)
    expect_rain_6h = models.FloatField(blank=True, null=True)
    expect_rain_12h = models.FloatField(blank=True, null=True)
    expect_snow_6h = models.FloatField(blank=True, null=True)
    expect_snow_12h = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_way = models.IntegerField(blank=True, null=True)
    wind_text = models.CharField(max_length=4, blank=True, null=True)
    humi = models.IntegerField(blank=True, null=True)
    fine_dust = models.CharField(max_length=10, blank=True, null=True)
    small_fine_dust = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gu_0'


class Gu1(models.Model):
    num = models.IntegerField(primary_key=True)
    gu = models.SmallIntegerField(blank=True, null=True)
    time_difference = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    temp = models.SmallIntegerField(blank=True, null=True)
    day_high_temp = models.SmallIntegerField(blank=True, null=True)
    day_low_temp = models.SmallIntegerField(blank=True, null=True)
    sky_state = models.IntegerField(blank=True, null=True)
    weather_state = models.IntegerField(blank=True, null=True)
    weather_kor = models.CharField(max_length=20, blank=True, null=True)
    rain_persent = models.IntegerField(blank=True, null=True)
    expect_rain_6h = models.FloatField(blank=True, null=True)
    expect_rain_12h = models.FloatField(blank=True, null=True)
    expect_snow_6h = models.FloatField(blank=True, null=True)
    expect_snow_12h = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_way = models.IntegerField(blank=True, null=True)
    wind_text = models.CharField(max_length=4, blank=True, null=True)
    humi = models.IntegerField(blank=True, null=True)
    fine_dust = models.CharField(max_length=10, blank=True, null=True)
    small_fine_dust = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gu_1'


class Gu2(models.Model):
    num = models.IntegerField(primary_key=True)
    gu = models.SmallIntegerField(blank=True, null=True)
    time_difference = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    temp = models.SmallIntegerField(blank=True, null=True)
    day_high_temp = models.SmallIntegerField(blank=True, null=True)
    day_low_temp = models.SmallIntegerField(blank=True, null=True)
    sky_state = models.IntegerField(blank=True, null=True)
    weather_state = models.IntegerField(blank=True, null=True)
    weather_kor = models.CharField(max_length=20, blank=True, null=True)
    rain_persent = models.IntegerField(blank=True, null=True)
    expect_rain_6h = models.FloatField(blank=True, null=True)
    expect_rain_12h = models.FloatField(blank=True, null=True)
    expect_snow_6h = models.FloatField(blank=True, null=True)
    expect_snow_12h = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_way = models.IntegerField(blank=True, null=True)
    wind_text = models.CharField(max_length=4, blank=True, null=True)
    humi = models.IntegerField(blank=True, null=True)
    fine_dust = models.CharField(max_length=10, blank=True, null=True)
    small_fine_dust = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gu_2'


class Gu3(models.Model):
    num = models.IntegerField(primary_key=True)
    gu = models.SmallIntegerField(blank=True, null=True)
    time_difference = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    temp = models.SmallIntegerField(blank=True, null=True)
    day_high_temp = models.SmallIntegerField(blank=True, null=True)
    day_low_temp = models.SmallIntegerField(blank=True, null=True)
    sky_state = models.IntegerField(blank=True, null=True)
    weather_state = models.IntegerField(blank=True, null=True)
    weather_kor = models.CharField(max_length=20, blank=True, null=True)
    rain_persent = models.IntegerField(blank=True, null=True)
    expect_rain_6h = models.FloatField(blank=True, null=True)
    expect_rain_12h = models.FloatField(blank=True, null=True)
    expect_snow_6h = models.FloatField(blank=True, null=True)
    expect_snow_12h = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_way = models.IntegerField(blank=True, null=True)
    wind_text = models.CharField(max_length=4, blank=True, null=True)
    humi = models.IntegerField(blank=True, null=True)
    fine_dust = models.CharField(max_length=10, blank=True, null=True)
    small_fine_dust = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gu_3'


class Gu4(models.Model):
    num = models.IntegerField(primary_key=True)
    gu = models.SmallIntegerField(blank=True, null=True)
    time_difference = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    temp = models.SmallIntegerField(blank=True, null=True)
    day_high_temp = models.SmallIntegerField(blank=True, null=True)
    day_low_temp = models.SmallIntegerField(blank=True, null=True)
    sky_state = models.IntegerField(blank=True, null=True)
    weather_state = models.IntegerField(blank=True, null=True)
    weather_kor = models.CharField(max_length=20, blank=True, null=True)
    rain_persent = models.IntegerField(blank=True, null=True)
    expect_rain_6h = models.FloatField(blank=True, null=True)
    expect_rain_12h = models.FloatField(blank=True, null=True)
    expect_snow_6h = models.FloatField(blank=True, null=True)
    expect_snow_12h = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_way = models.IntegerField(blank=True, null=True)
    wind_text = models.CharField(max_length=4, blank=True, null=True)
    humi = models.IntegerField(blank=True, null=True)
    fine_dust = models.CharField(max_length=10, blank=True, null=True)
    small_fine_dust = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gu_4'


class Header(models.Model):
    num = models.IntegerField(primary_key=True)
    update_year = models.IntegerField(blank=True, null=True)
    update_month = models.IntegerField(blank=True, null=True)
    update_date = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'header'