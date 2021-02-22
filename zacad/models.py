# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ImAdminGroup(models.Model):
    group_key = models.AutoField(db_column='GROUP_KEY', primary_key=True)  # Field name made lowercase.
    group_type = models.IntegerField(db_column='GROUP_TYPE', blank=True, null=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='GROUP_NAME', max_length=45)  # Field name made lowercase.
    campus_name = models.CharField(db_column='CAMPUS_NAME', max_length=45)  # Field name made lowercase.
    school_code = models.IntegerField(db_column='SCHOOL_CODE')  # Field name made lowercase.
    school_type = models.CharField(db_column='SCHOOL_TYPE', max_length=45)  # Field name made lowercase.
    school_gubun = models.CharField(db_column='SCHOOL_GUBUN', max_length=45)  # Field name made lowercase.
    est_type = models.CharField(db_column='EST_TYPE', max_length=45)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=45)  # Field name made lowercase.
    link = models.CharField(db_column='LINK', max_length=250)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    group_no = models.CharField(db_column='GROUP_NO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ADMIN_GROUP'


class ImAdminGroupInterview(models.Model):
    gi_key = models.AutoField(db_column='GI_KEY', primary_key=True)  # Field name made lowercase.
    gi_state = models.CharField(db_column='GI_STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    group_key = models.IntegerField(db_column='GROUP_KEY')  # Field name made lowercase.
    gi_code = models.IntegerField(db_column='GI_CODE', blank=True, null=True)  # Field name made lowercase.
    gi_name = models.CharField(db_column='GI_NAME', max_length=45)  # Field name made lowercase.
    gi_email = models.CharField(db_column='GI_EMAIL', max_length=45)  # Field name made lowercase.
    gi_subject = models.CharField(db_column='GI_SUBJECT', max_length=100)  # Field name made lowercase.
    gi_job_family = models.CharField(db_column='GI_JOB_FAMILY', max_length=100)  # Field name made lowercase.
    gi_job_sub = models.CharField(db_column='GI_JOB_SUB', max_length=100)  # Field name made lowercase.
    gi_start_date = models.CharField(db_column='GI_START_DATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gi_start_time = models.CharField(db_column='GI_START_TIME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gi_end_date = models.CharField(db_column='GI_END_DATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gi_end_time = models.CharField(db_column='GI_END_TIME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gi_1_tts = models.CharField(db_column='GI_1_TTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    gi_2_tts = models.CharField(db_column='GI_2_TTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    gi_3_tts = models.CharField(db_column='GI_3_TTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ADMIN_GROUP_INTERVIEW'


class ImAdminGroupInterviewData(models.Model):
    gd_key = models.AutoField(db_column='GD_KEY', primary_key=True)  # Field name made lowercase.
    gi_code = models.CharField(db_column='GI_CODE', max_length=100)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY')  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ADMIN_GROUP_INTERVIEW_DATA'


class ImAdminUserEtc(models.Model):
    class_code = models.IntegerField(db_column='CLASS_CODE')  # Field name made lowercase.
    class_name = models.CharField(db_column='CLASS_NAME', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ADMIN_USER_ETC'


class ImAdvice(models.Model):
    advice_key = models.AutoField(db_column='ADVICE_KEY', primary_key=True)  # Field name made lowercase.
    advice_top = models.IntegerField(db_column='ADVICE_TOP')  # Field name made lowercase.
    advice_writer = models.CharField(db_column='ADVICE_WRITER', max_length=45)  # Field name made lowercase.
    advice_title = models.CharField(db_column='ADVICE_TITLE', max_length=100)  # Field name made lowercase.
    advice_text = models.CharField(db_column='ADVICE_TEXT', max_length=2000)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ADVICE'


class ImAdviceFile(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    file_fk = models.IntegerField(db_column='FILE_FK', unique=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_origin = models.CharField(db_column='FILE_ORIGIN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_folder = models.CharField(db_column='FILE_FOLDER', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_size = models.IntegerField(db_column='FILE_SIZE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ADVICE_FILE'


class ImAdUser(models.Model):
    user_key = models.AutoField(db_column='USER_KEY', primary_key=True)  # Field name made lowercase.
    user_type = models.IntegerField(db_column='USER_TYPE', blank=True, null=True)  # Field name made lowercase.
    user_group = models.IntegerField(db_column='USER_GROUP', blank=True, null=True)  # Field name made lowercase.
    user_class = models.IntegerField(db_column='USER_CLASS', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_pwd = models.CharField(db_column='USER_PWD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_phone = models.CharField(db_column='USER_PHONE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_AD_USER'


class ImApiKey(models.Model):
    ak_pk = models.AutoField(db_column='AK_PK', primary_key=True)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=50)  # Field name made lowercase.
    secretkey = models.CharField(db_column='SECRETKEY', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_API_KEY'


class ImAppPush(models.Model):
    push_key = models.AutoField(db_column='PUSH_KEY', primary_key=True)  # Field name made lowercase.
    push_user = models.CharField(db_column='PUSH_USER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    push_type = models.CharField(db_column='PUSH_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    push_addr = models.CharField(db_column='PUSH_ADDR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    push_text = models.CharField(db_column='PUSH_TEXT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_APP_PUSH'


class ImAppPushType(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    push_type = models.CharField(db_column='PUSH_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    push_name = models.CharField(db_column='PUSH_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_APP_PUSH_TYPE'


class ImCode(models.Model):
    code_key = models.IntegerField(db_column='CODE_KEY', unique=True, blank=True, null=True)  # Field name made lowercase.
    code_name = models.CharField(db_column='CODE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_CODE'


class ImEwhaAdminUser(models.Model):
    user_key = models.AutoField(db_column='USER_KEY', primary_key=True)  # Field name made lowercase.
    group_code = models.IntegerField(db_column='GROUP_CODE', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_pwd = models.CharField(db_column='USER_PWD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_EWHA_ADMIN_USER'


class ImEwhaGroup(models.Model):
    group_code = models.AutoField(db_column='GROUP_CODE', primary_key=True)  # Field name made lowercase.
    group_dvsn = models.CharField(db_column='GROUP_DVSN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='GROUP_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_intro = models.CharField(db_column='GROUP_INTRO', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_EWHA_GROUP'


class ImEwhaQuery(models.Model):
    group_code = models.IntegerField(db_column='GROUP_CODE')  # Field name made lowercase.
    qz_tts = models.CharField(db_column='QZ_TTS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    qz_time = models.CharField(db_column='QZ_TIME', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_EWHA_QUERY'


class ImFaq(models.Model):
    faq_key = models.AutoField(db_column='FAQ_KEY', primary_key=True)  # Field name made lowercase.
    faq_title = models.CharField(db_column='FAQ_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    faq_text = models.CharField(db_column='FAQ_TEXT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_FAQ'


class ImFile(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', unique=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_origin = models.CharField(db_column='FILE_ORIGIN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_folder = models.CharField(db_column='FILE_FOLDER', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_size = models.IntegerField(db_column='FILE_SIZE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_FILE'


class ImFixTts(models.Model):
    fi_pk = models.AutoField(db_column='FI_PK', primary_key=True)  # Field name made lowercase.
    fi_tts = models.CharField(db_column='FI_TTS', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_FIX_TTS'


class ImGroupCount(models.Model):
    gc_pk = models.AutoField(db_column='GC_PK', primary_key=True)  # Field name made lowercase.
    group_key = models.IntegerField(db_column='GROUP_KEY')  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GROUP_COUNT'


class ImGroupCoupon(models.Model):
    group_key = models.IntegerField(db_column='GROUP_KEY', unique=True)  # Field name made lowercase.
    writer_key = models.IntegerField(db_column='WRITER_KEY', blank=True, null=True)  # Field name made lowercase.
    coupon_type = models.CharField(db_column='COUPON_TYPE', max_length=1)  # Field name made lowercase.
    group_coupon = models.IntegerField(db_column='GROUP_COUPON')  # Field name made lowercase.
    group_count = models.IntegerField(db_column='GROUP_COUNT')  # Field name made lowercase.
    date_type = models.CharField(db_column='DATE_TYPE', max_length=1)  # Field name made lowercase.
    start_date = models.CharField(db_column='START_DATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='END_DATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    limit_type = models.CharField(db_column='LIMIT_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    limit_coupon = models.IntegerField(db_column='LIMIT_COUPON', blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GROUP_COUPON'


class ImGwagiFile(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rtsp_url = models.CharField(db_column='RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_express = models.CharField(db_column='JSON_EXPRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_action = models.CharField(db_column='JSON_ACTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GWAGI_FILE'


class ImGwagiFileSave(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rtsp_url = models.CharField(db_column='RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_express = models.CharField(db_column='JSON_EXPRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_action = models.CharField(db_column='JSON_ACTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GWAGI_FILE_SAVE'


class ImGwagiFileSave2(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rtsp_url = models.CharField(db_column='RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_express = models.CharField(db_column='JSON_EXPRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_action = models.CharField(db_column='JSON_ACTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GWAGI_FILE_SAVE_2'


class ImGwagiFileSave3(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rtsp_url = models.CharField(db_column='RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_express = models.CharField(db_column='JSON_EXPRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_action = models.CharField(db_column='JSON_ACTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GWAGI_FILE_SAVE_3'


class ImGwagiFileSave5(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rtsp_url = models.CharField(db_column='RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_express = models.CharField(db_column='JSON_EXPRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_action = models.CharField(db_column='JSON_ACTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GWAGI_FILE_SAVE_5'


class ImGwagiFileSave6(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rtsp_url = models.CharField(db_column='RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_express = models.CharField(db_column='JSON_EXPRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_action = models.CharField(db_column='JSON_ACTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GWAGI_FILE_SAVE_6'


class ImGwagiList(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    file_type = models.CharField(db_column='FILE_TYPE', max_length=1)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_time = models.IntegerField(db_column='FILE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GWAGI_LIST'


class ImGwagiList0126(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    file_type = models.CharField(db_column='FILE_TYPE', max_length=1)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_time = models.IntegerField(db_column='FILE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_GWAGI_LIST_01_26'


class ImIapApple(models.Model):
    apple_key = models.AutoField(db_column='APPLE_KEY', primary_key=True)  # Field name made lowercase.
    receipt_type = models.CharField(db_column='RECEIPT_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    product_id = models.CharField(db_column='PRODUCT_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    transaction_id = models.CharField(db_column='TRANSACTION_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    original_transaction_id = models.CharField(db_column='ORIGINAL_TRANSACTION_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    purchase_data = models.CharField(db_column='PURCHASE_DATA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    purchase_data_ms = models.CharField(db_column='PURCHASE_DATA_MS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    purchase_date_pst = models.CharField(db_column='PURCHASE_DATE_PST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_at = models.DateTimeField(db_column='CREATE_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_IAP_APPLE'


class ImIapProduct(models.Model):
    product_key = models.AutoField(db_column='PRODUCT_KEY', primary_key=True)  # Field name made lowercase.
    product_id = models.CharField(db_column='PRODUCT_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    product_price = models.IntegerField(db_column='PRODUCT_PRICE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_IAP_PRODUCT'


class ImIapSubscribe(models.Model):
    is_pk = models.AutoField(db_column='IS_PK', primary_key=True)  # Field name made lowercase.
    is_state = models.CharField(db_column='IS_STATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY')  # Field name made lowercase.
    expiration_date = models.CharField(db_column='EXPIRATION_DATE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_IAP_SUBSCRIBE'


class ImKcpResult(models.Model):
    kcp_key = models.AutoField(db_column='KCP_KEY', primary_key=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_KCP_RESULT'


class ImLogoFile(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    file_fk = models.IntegerField(db_column='FILE_FK', unique=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_origin = models.CharField(db_column='FILE_ORIGIN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_folder = models.CharField(db_column='FILE_FOLDER', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_size = models.IntegerField(db_column='FILE_SIZE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_LOGO_FILE'


class ImMtbi(models.Model):
    mt_pk = models.AutoField(db_column='MT_PK', primary_key=True)  # Field name made lowercase.
    mt_page = models.IntegerField(db_column='MT_PAGE', blank=True, null=True)  # Field name made lowercase.
    mk_pk = models.IntegerField(db_column='MK_PK', blank=True, null=True)  # Field name made lowercase.
    mt_text = models.CharField(db_column='MT_TEXT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI'


class ImMtbiBkData(models.Model):
    md_pk = models.AutoField(db_column='MD_PK', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    qz_data = models.CharField(db_column='QZ_DATA', max_length=10000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI_BK_DATA'


class ImMtbiData(models.Model):
    md_pk = models.AutoField(db_column='MD_PK', primary_key=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    mk_pk = models.IntegerField(db_column='MK_PK', blank=True, null=True)  # Field name made lowercase.
    mt_pick = models.IntegerField(db_column='MT_PICK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI_DATA'


class ImMtbiDataBk(models.Model):
    md_pk = models.AutoField(db_column='MD_PK', primary_key=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    mk_pk = models.IntegerField(db_column='MK_PK', blank=True, null=True)  # Field name made lowercase.
    mt_pick = models.IntegerField(db_column='MT_PICK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI_DATA_BK'


class ImMtbiJob(models.Model):
    mj_pk = models.AutoField(db_column='MJ_PK', primary_key=True)  # Field name made lowercase.
    mj_type = models.IntegerField(db_column='MJ_TYPE', blank=True, null=True)  # Field name made lowercase.
    mk_pk = models.IntegerField(db_column='MK_PK', blank=True, null=True)  # Field name made lowercase.
    mj_score = models.IntegerField(db_column='MJ_SCORE', blank=True, null=True)  # Field name made lowercase.
    mj_job = models.CharField(db_column='MJ_JOB', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI_JOB'


class ImMtbiJobEtc(models.Model):
    mt_sheet = models.PositiveIntegerField(db_column='MT_SHEET')  # Field name made lowercase.
    mj_job = models.CharField(db_column='MJ_JOB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mj_job_sub = models.CharField(db_column='MJ_JOB_SUB', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI_JOB_ETC'


class ImMtbiKeyword(models.Model):
    mk_pk = models.AutoField(db_column='MK_PK', primary_key=True)  # Field name made lowercase.
    mk_keyword = models.CharField(db_column='MK_KEYWORD', max_length=50)  # Field name made lowercase.
    op_pk = models.IntegerField(db_column='OP_PK', blank=True, null=True)  # Field name made lowercase.
    op_keyword = models.CharField(db_column='OP_KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI_KEYWORD'


class ImMtbiKpcTts(models.Model):
    mt_pk = models.AutoField(db_column='MT_PK', primary_key=True)  # Field name made lowercase.
    mt_sheet = models.IntegerField(db_column='MT_SHEET')  # Field name made lowercase.
    mt_type = models.CharField(db_column='MT_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mt_tts = models.CharField(db_column='MT_TTS', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI_KPC_TTS'


class ImMtbiTts(models.Model):
    mt_pk = models.AutoField(db_column='MT_PK', primary_key=True)  # Field name made lowercase.
    mt_sheet = models.IntegerField(db_column='MT_SHEET')  # Field name made lowercase.
    mt_type = models.CharField(db_column='MT_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mt_tts = models.CharField(db_column='MT_TTS', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_MTBI_TTS'


class ImNews(models.Model):
    news_key = models.AutoField(db_column='NEWS_KEY', primary_key=True)  # Field name made lowercase.
    news_top = models.IntegerField(db_column='NEWS_TOP')  # Field name made lowercase.
    news_writer = models.CharField(db_column='NEWS_WRITER', max_length=45)  # Field name made lowercase.
    news_title = models.CharField(db_column='NEWS_TITLE', max_length=100)  # Field name made lowercase.
    news_text = models.CharField(db_column='NEWS_TEXT', max_length=2000)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_NEWS'


class ImNewsFile(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    file_fk = models.IntegerField(db_column='FILE_FK', unique=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_origin = models.CharField(db_column='FILE_ORIGIN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_folder = models.CharField(db_column='FILE_FOLDER', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_size = models.IntegerField(db_column='FILE_SIZE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_NEWS_FILE'


class ImNotice(models.Model):
    noti_key = models.AutoField(db_column='NOTI_KEY', primary_key=True)  # Field name made lowercase.
    noti_title = models.CharField(db_column='NOTI_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    noti_text = models.CharField(db_column='NOTI_TEXT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_NOTICE'


class ImPcError(models.Model):
    error_key = models.AutoField(db_column='ERROR_KEY', primary_key=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='MESSAGE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_PC_ERROR'


class ImPiData(models.Model):
    pi_key = models.AutoField(db_column='PI_KEY', primary_key=True)  # Field name made lowercase.
    file_key = models.IntegerField(db_column='FILE_KEY', blank=True, null=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    avg_angry = models.IntegerField(db_column='AVG_ANGRY', blank=True, null=True)  # Field name made lowercase.
    avg_happy = models.IntegerField(db_column='AVG_HAPPY', blank=True, null=True)  # Field name made lowercase.
    avg_normal = models.IntegerField(db_column='AVG_NORMAL', blank=True, null=True)  # Field name made lowercase.
    avg_sadness = models.IntegerField(db_column='AVG_SADNESS', blank=True, null=True)  # Field name made lowercase.
    avg_surprise = models.IntegerField(db_column='AVG_SURPRISE', blank=True, null=True)  # Field name made lowercase.
    avg_body = models.IntegerField(db_column='AVG_BODY', blank=True, null=True)  # Field name made lowercase.
    cnt_hand = models.IntegerField(db_column='CNT_HAND', blank=True, null=True)  # Field name made lowercase.
    avg_geze_pitch = models.FloatField(db_column='AVG_GEZE_PITCH', blank=True, null=True)  # Field name made lowercase.
    avg_geze_yaw = models.FloatField(db_column='AVG_GEZE_YAW', blank=True, null=True)  # Field name made lowercase.
    avg_geze_pitch_1 = models.FloatField(db_column='AVG_GEZE_PITCH_1', blank=True, null=True)  # Field name made lowercase.
    avg_geze_yaw_1 = models.FloatField(db_column='AVG_GEZE_YAW_1', blank=True, null=True)  # Field name made lowercase.
    avg_geze_pitch_2 = models.FloatField(db_column='AVG_GEZE_PITCH_2', blank=True, null=True)  # Field name made lowercase.
    avg_geze_yaw_2 = models.FloatField(db_column='AVG_GEZE_YAW_2', blank=True, null=True)  # Field name made lowercase.
    avg_geze_pitch_3 = models.FloatField(db_column='AVG_GEZE_PITCH_3', blank=True, null=True)  # Field name made lowercase.
    avg_geze_yaw_3 = models.FloatField(db_column='AVG_GEZE_YAW_3', blank=True, null=True)  # Field name made lowercase.
    avg_db = models.IntegerField(db_column='AVG_DB', blank=True, null=True)  # Field name made lowercase.
    avg_tone = models.IntegerField(db_column='AVG_TONE', blank=True, null=True)  # Field name made lowercase.
    avg_speed = models.FloatField(db_column='AVG_SPEED', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    magnitude = models.FloatField(db_column='MAGNITUDE', blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='STR', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    qz_tts = models.CharField(db_column='QZ_TTS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_PI_DATA'


class ImPiDataBk(models.Model):
    pi_key = models.AutoField(db_column='PI_KEY', primary_key=True)  # Field name made lowercase.
    file_key = models.IntegerField(db_column='FILE_KEY', blank=True, null=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    avg_angry = models.IntegerField(db_column='AVG_ANGRY', blank=True, null=True)  # Field name made lowercase.
    avg_happy = models.IntegerField(db_column='AVG_HAPPY', blank=True, null=True)  # Field name made lowercase.
    avg_normal = models.IntegerField(db_column='AVG_NORMAL', blank=True, null=True)  # Field name made lowercase.
    avg_sadness = models.IntegerField(db_column='AVG_SADNESS', blank=True, null=True)  # Field name made lowercase.
    avg_surprise = models.IntegerField(db_column='AVG_SURPRISE', blank=True, null=True)  # Field name made lowercase.
    avg_body = models.IntegerField(db_column='AVG_BODY', blank=True, null=True)  # Field name made lowercase.
    cnt_hand = models.IntegerField(db_column='CNT_HAND', blank=True, null=True)  # Field name made lowercase.
    avg_geze_pitch = models.FloatField(db_column='AVG_GEZE_PITCH', blank=True, null=True)  # Field name made lowercase.
    avg_geze_yaw = models.FloatField(db_column='AVG_GEZE_YAW', blank=True, null=True)  # Field name made lowercase.
    avg_geze_pitch_1 = models.FloatField(db_column='AVG_GEZE_PITCH_1', blank=True, null=True)  # Field name made lowercase.
    avg_geze_yaw_1 = models.FloatField(db_column='AVG_GEZE_YAW_1', blank=True, null=True)  # Field name made lowercase.
    avg_geze_pitch_2 = models.FloatField(db_column='AVG_GEZE_PITCH_2', blank=True, null=True)  # Field name made lowercase.
    avg_geze_yaw_2 = models.FloatField(db_column='AVG_GEZE_YAW_2', blank=True, null=True)  # Field name made lowercase.
    avg_geze_pitch_3 = models.FloatField(db_column='AVG_GEZE_PITCH_3', blank=True, null=True)  # Field name made lowercase.
    avg_geze_yaw_3 = models.FloatField(db_column='AVG_GEZE_YAW_3', blank=True, null=True)  # Field name made lowercase.
    avg_db = models.IntegerField(db_column='AVG_DB', blank=True, null=True)  # Field name made lowercase.
    avg_tone = models.IntegerField(db_column='AVG_TONE', blank=True, null=True)  # Field name made lowercase.
    avg_speed = models.FloatField(db_column='AVG_SPEED', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    magnitude = models.FloatField(db_column='MAGNITUDE', blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='STR', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    qz_tts = models.CharField(db_column='QZ_TTS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_PI_DATA_BK'


class ImPopData(models.Model):
    pop_key = models.AutoField(db_column='POP_KEY', primary_key=True)  # Field name made lowercase.
    group_key = models.IntegerField(db_column='GROUP_KEY', unique=True)  # Field name made lowercase.
    pop_type = models.CharField(db_column='POP_TYPE', max_length=1)  # Field name made lowercase.
    pop_user = models.CharField(db_column='POP_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_date = models.CharField(db_column='START_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='END_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_POP_DATA'


class ImPopFile(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    file_fk = models.IntegerField(db_column='FILE_FK', unique=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_origin = models.CharField(db_column='FILE_ORIGIN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_folder = models.CharField(db_column='FILE_FOLDER', max_length=250, blank=True, null=True)  # Field name made lowercase.
    file_size = models.IntegerField(db_column='FILE_SIZE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_POP_FILE'


class ImPracticeTts(models.Model):
    pr_pk = models.AutoField(db_column='PR_PK', primary_key=True)  # Field name made lowercase.
    pr_tts = models.CharField(db_column='PR_TTS', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_PRACTICE_TTS'


class ImQuiry(models.Model):
    quiry_seq = models.AutoField(db_column='QUIRY_SEQ', primary_key=True)  # Field name made lowercase.
    quiry_key = models.IntegerField(db_column='QUIRY_KEY', blank=True, null=True)  # Field name made lowercase.
    quiry_title = models.CharField(db_column='QUIRY_TITLE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    quiry_text = models.CharField(db_column='QUIRY_TEXT', max_length=2000)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ans_name = models.CharField(db_column='ANS_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ans_text = models.CharField(db_column='ANS_TEXT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    ans_type = models.CharField(db_column='ANS_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ansdate = models.CharField(db_column='ANSDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QUIRY'


class ImQzBasic(models.Model):
    qz_code = models.AutoField(db_column='QZ_CODE', primary_key=True)  # Field name made lowercase.
    qz_tts = models.CharField(db_column='QZ_TTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    qz_time = models.CharField(db_column='QZ_TIME', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_BASIC'


class ImQzChoice(models.Model):
    qz_code = models.IntegerField(db_column='QZ_CODE')  # Field name made lowercase.
    qz_def = models.IntegerField(db_column='QZ_DEF')  # Field name made lowercase.
    qz_title = models.CharField(db_column='QZ_TITLE', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_CHOICE'


class ImQzDepth(models.Model):
    qz_code = models.AutoField(db_column='QZ_CODE', primary_key=True)  # Field name made lowercase.
    qz_num = models.CharField(db_column='QZ_NUM', max_length=45)  # Field name made lowercase.
    qz_tts = models.CharField(db_column='QZ_TTS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    qz_time = models.CharField(db_column='QZ_TIME', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_DEPTH'


class ImQzFile(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    qz_platform = models.IntegerField(db_column='QZ_PLATFORM', blank=True, null=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    qz_num = models.IntegerField(db_column='QZ_NUM', blank=True, null=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    group_code = models.IntegerField(db_column='GROUP_CODE', blank=True, null=True)  # Field name made lowercase.
    rtsp_url = models.CharField(db_column='RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_express = models.CharField(db_column='JSON_EXPRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_action = models.CharField(db_column='JSON_ACTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_tone = models.CharField(db_column='JSON_TONE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_db = models.CharField(db_column='JSON_DB', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_speed = models.CharField(db_column='JSON_SPEED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    thum_url = models.CharField(db_column='THUM_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    qz_org_tts = models.CharField(db_column='QZ_ORG_TTS', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_FILE'


class ImQzFileBk(models.Model):
    file_key = models.AutoField(db_column='FILE_KEY', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    qz_platform = models.IntegerField(db_column='QZ_PLATFORM', blank=True, null=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY', blank=True, null=True)  # Field name made lowercase.
    qz_num = models.IntegerField(db_column='QZ_NUM', blank=True, null=True)  # Field name made lowercase.
    qz_type = models.CharField(db_column='QZ_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    group_code = models.IntegerField(db_column='GROUP_CODE', blank=True, null=True)  # Field name made lowercase.
    rtsp_url = models.CharField(db_column='RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_express = models.CharField(db_column='JSON_EXPRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_action = models.CharField(db_column='JSON_ACTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_tone = models.CharField(db_column='JSON_TONE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_db = models.CharField(db_column='JSON_DB', max_length=500, blank=True, null=True)  # Field name made lowercase.
    json_speed = models.CharField(db_column='JSON_SPEED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    thum_url = models.CharField(db_column='THUM_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    qz_org_tts = models.CharField(db_column='QZ_ORG_TTS', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_FILE_BK'


class ImQzFitness(models.Model):
    qz_group = models.IntegerField(db_column='QZ_GROUP', unique=True, blank=True, null=True)  # Field name made lowercase.
    qz_fitness = models.CharField(db_column='QZ_FITNESS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_FITNESS'


class ImQzGroup(models.Model):
    qz_group = models.AutoField(db_column='QZ_GROUP', primary_key=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY')  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_GROUP'


class ImQzGroupEtc(models.Model):
    qz_group = models.IntegerField(db_column='QZ_GROUP', unique=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY')  # Field name made lowercase.
    origin_job_family = models.CharField(db_column='ORIGIN_JOB_FAMILY', max_length=45)  # Field name made lowercase.
    origin_job_sub = models.CharField(db_column='ORIGIN_JOB_SUB', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_GROUP_ETC'


class ImQzKeyword(models.Model):
    qz_code = models.IntegerField(db_column='QZ_CODE', unique=True, blank=True, null=True)  # Field name made lowercase.
    qz_eye = models.CharField(db_column='QZ_EYE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_body = models.CharField(db_column='QZ_BODY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_face = models.CharField(db_column='QZ_FACE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_db = models.CharField(db_column='QZ_DB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_tone = models.CharField(db_column='QZ_TONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_speed = models.CharField(db_column='QZ_SPEED', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_KEYWORD'


class ImQzKeywordSub(models.Model):
    qz_code = models.IntegerField(db_column='QZ_CODE', unique=True, blank=True, null=True)  # Field name made lowercase.
    qz_keyword = models.CharField(db_column='QZ_KEYWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_KEYWORD_SUB'


class ImQzKeywordText(models.Model):
    qz_code = models.IntegerField(db_column='QZ_CODE', unique=True, blank=True, null=True)  # Field name made lowercase.
    qz_eye = models.CharField(db_column='QZ_EYE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_body = models.CharField(db_column='QZ_BODY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_face = models.CharField(db_column='QZ_FACE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_db = models.CharField(db_column='QZ_DB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_tone = models.CharField(db_column='QZ_TONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_speed = models.CharField(db_column='QZ_SPEED', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_KEYWORD_TEXT'


class ImQzMatter(models.Model):
    qz_code = models.AutoField(db_column='QZ_CODE', primary_key=True)  # Field name made lowercase.
    qz_num = models.CharField(db_column='QZ_NUM', max_length=45)  # Field name made lowercase.
    qz_tts = models.CharField(db_column='QZ_TTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    qz_time = models.CharField(db_column='QZ_TIME', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_MATTER'


class ImQzMtbiData(models.Model):
    no = models.AutoField(primary_key=True)
    qz_group = models.IntegerField(db_column='QZ_GROUP', unique=True, blank=True, null=True)  # Field name made lowercase.
    qz_1st = models.CharField(db_column='QZ_1ST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_1st_score = models.IntegerField(db_column='QZ_1ST_SCORE', blank=True, null=True)  # Field name made lowercase.
    qz_2nd = models.CharField(db_column='QZ_2ND', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qz_2nd_score = models.IntegerField(db_column='QZ_2ND_SCORE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_MTBI_DATA'


class ImQzName(models.Model):
    qz_num = models.IntegerField(db_column='QZ_NUM', unique=True, blank=True, null=True)  # Field name made lowercase.
    qz_name = models.CharField(db_column='QZ_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_NAME'


class ImQzQu(models.Model):
    qz_code = models.IntegerField(db_column='QZ_CODE', blank=True, null=True)  # Field name made lowercase.
    qz_name = models.CharField(db_column='QZ_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_QU'


class ImQzTitle(models.Model):
    qz_code = models.IntegerField(db_column='QZ_CODE', unique=True, blank=True, null=True)  # Field name made lowercase.
    qz_title = models.CharField(db_column='QZ_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_TITLE'


class ImQzTts(models.Model):
    qz_code = models.AutoField(db_column='QZ_CODE', primary_key=True)  # Field name made lowercase.
    qz_def = models.CharField(db_column='QZ_DEF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qz_tts = models.CharField(db_column='QZ_TTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tts_url = models.CharField(db_column='TTS_URL', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_TTS'


class ImQzTtsCsv(models.Model):
    qz_code = models.AutoField(db_column='QZ_CODE', primary_key=True)  # Field name made lowercase.
    qz_tts = models.CharField(db_column='QZ_TTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    qz_time = models.CharField(db_column='QZ_TIME', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_TTS_CSV'


class ImQzWord(models.Model):
    qz_code = models.IntegerField(db_column='QZ_CODE', unique=True, blank=True, null=True)  # Field name made lowercase.
    qz_text = models.CharField(db_column='QZ_TEXT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_WORD'


class ImQzZacad(models.Model):
    za_key = models.AutoField(db_column='ZA_KEY', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', unique=True)  # Field name made lowercase.
    za_tts2 = models.CharField(db_column='ZA_TTS2', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    za_datetime = models.DateTimeField(db_column='ZA_DATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_ZACAD'


class ImQzZacadTts2(models.Model):
    qz_code = models.AutoField(db_column='QZ_CODE', primary_key=True)  # Field name made lowercase.
    za_code = models.IntegerField(db_column='ZA_CODE')  # Field name made lowercase.
    za_tts2 = models.CharField(db_column='ZA_TTS2', max_length=250)  # Field name made lowercase.
    za_tts3 = models.CharField(db_column='ZA_TTS3', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_QZ_ZACAD_TTS2'


class ImTestData(models.Model):
    data_key = models.AutoField(db_column='DATA_KEY', primary_key=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emotion = models.CharField(db_column='EMOTION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_TEST_DATA'


class ImUnvi(models.Model):
    unvi_key = models.AutoField(db_column='UNVI_KEY', primary_key=True)  # Field name made lowercase.
    unvi_name = models.CharField(db_column='UNVI_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_UNVI'


class ImUnviStudent(models.Model):
    student_key = models.AutoField(db_column='STUDENT_KEY', primary_key=True)  # Field name made lowercase.
    user_group = models.IntegerField(db_column='USER_GROUP', blank=True, null=True)  # Field name made lowercase.
    school_code = models.IntegerField(db_column='SCHOOL_CODE', blank=True, null=True)  # Field name made lowercase.
    student_class = models.CharField(db_column='STUDENT_CLASS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    student_name = models.CharField(db_column='STUDENT_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    student_id = models.CharField(db_column='STUDENT_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_UNVI_STUDENT'


class ImUnviStudy(models.Model):
    unvi_fk = models.IntegerField(db_column='UNVI_FK', blank=True, null=True)  # Field name made lowercase.
    unvi_study = models.CharField(db_column='UNVI_STUDY', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_UNVI_STUDY'


class ImUser(models.Model):
    user_key = models.AutoField(db_column='USER_KEY', primary_key=True)  # Field name made lowercase.
    user_code = models.IntegerField(db_column='USER_CODE', blank=True, null=True)  # Field name made lowercase.
    user_group = models.IntegerField(db_column='USER_GROUP', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    user_coupon = models.IntegerField(db_column='USER_COUPON', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=250)  # Field name made lowercase.
    user_pwd = models.CharField(db_column='USER_PWD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_age = models.CharField(db_column='USER_AGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_sex = models.CharField(db_column='USER_SEX', max_length=100, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zg_id = models.CharField(db_column='ZG_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    user_uuid = models.CharField(db_column='USER_UUID', unique=True, max_length=250, blank=True, null=True)  # Field name made lowercase.
    push_key = models.CharField(db_column='PUSH_KEY', max_length=250, blank=True, null=True)  # Field name made lowercase.
    temp_id = models.CharField(db_column='TEMP_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recomm_id = models.CharField(db_column='RECOMM_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    large_scale = models.CharField(db_column='LARGE_SCALE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    medium_scale = models.CharField(db_column='MEDIUM_SCALE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    student_id = models.CharField(db_column='STUDENT_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    job_family = models.CharField(db_column='JOB_FAMILY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    job_sub = models.CharField(db_column='JOB_SUB', max_length=45, blank=True, null=True)  # Field name made lowercase.
    kpc_id = models.CharField(db_column='KPC_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    biz_group = models.IntegerField(db_column='BIZ_GROUP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_USER'


class ImUserBiz(models.Model):
    kpc_key = models.AutoField(db_column='KPC_KEY', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    kpc_id = models.CharField(db_column='KPC_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_USER_BIZ'


class ImUserCouponPay(models.Model):
    user_key = models.IntegerField(db_column='USER_KEY')  # Field name made lowercase.
    user_coupon = models.IntegerField(db_column='USER_COUPON')  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_USER_COUPON_PAY'


class ImUserKpcData(models.Model):
    kpc_key = models.AutoField(db_column='KPC_KEY', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    kpc_id = models.CharField(db_column='KPC_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    job_sub = models.CharField(db_column='JOB_SUB', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_age = models.CharField(db_column='USER_AGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_sex = models.CharField(db_column='USER_SEX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_USER_KPC_DATA'


class ImUserKpcData2Nd(models.Model):
    kpc_key = models.AutoField(db_column='KPC_KEY', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    kpc_id = models.CharField(db_column='KPC_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    job_sub = models.CharField(db_column='JOB_SUB', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_age = models.CharField(db_column='USER_AGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_sex = models.CharField(db_column='USER_SEX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_USER_KPC_DATA_2ND'


class ImUserKpcData3Nd(models.Model):
    kpc_key = models.AutoField(db_column='KPC_KEY', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP', blank=True, null=True)  # Field name made lowercase.
    kpc_id = models.CharField(db_column='KPC_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    job_sub = models.CharField(db_column='JOB_SUB', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_age = models.CharField(db_column='USER_AGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_sex = models.CharField(db_column='USER_SEX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_USER_KPC_DATA_3ND'


class ImUserKpcDay(models.Model):
    day_key = models.AutoField(db_column='DAY_KEY', primary_key=True)  # Field name made lowercase.
    start_date = models.CharField(db_column='START_DATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_USER_KPC_DAY'


class ImUserKpcType(models.Model):
    kpc_pk = models.AutoField(db_column='KPC_PK', primary_key=True)  # Field name made lowercase.
    kpc_type = models.CharField(db_column='KPC_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_USER_KPC_TYPE'


class ImVersion(models.Model):
    app_key = models.AutoField(db_column='APP_KEY', primary_key=True)  # Field name made lowercase.
    app_type = models.IntegerField(db_column='APP_TYPE')  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='STR', max_length=500, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_VERSION'


class ImZacadQ1Bk(models.Model):
    zq_pk = models.AutoField(db_column='ZQ_PK', primary_key=True)  # Field name made lowercase.
    zq_code = models.IntegerField(db_column='ZQ_CODE', blank=True, null=True)  # Field name made lowercase.
    zq_q1 = models.CharField(db_column='ZQ_Q1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    zq_a1 = models.CharField(db_column='ZQ_A1', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'IM_ZACAD_Q1_BK'

    #def __str__(self):
    #    return self.zq_q1


class ImZacadQ2Bk(models.Model):
    zq_pk = models.AutoField(db_column='ZQ_PK', primary_key=True)  # Field name made lowercase.
    zq_q2 = models.CharField(db_column='ZQ_Q2', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'IM_ZACAD_Q2_BK'


class ImZgData(models.Model):
    zg_key = models.AutoField(db_column='ZG_KEY', primary_key=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY')  # Field name made lowercase.
    zg_type = models.CharField(db_column='ZG_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    zg_rtsp_url = models.CharField(db_column='ZG_RTSP_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    zg_file_url = models.CharField(db_column='ZG_FILE_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    zg_angry = models.IntegerField(db_column='ZG_ANGRY', blank=True, null=True)  # Field name made lowercase.
    zg_happy = models.IntegerField(db_column='ZG_HAPPY', blank=True, null=True)  # Field name made lowercase.
    zg_normal = models.IntegerField(db_column='ZG_NORMAL', blank=True, null=True)  # Field name made lowercase.
    zg_sadness = models.IntegerField(db_column='ZG_SADNESS', blank=True, null=True)  # Field name made lowercase.
    zg_surprise = models.IntegerField(db_column='ZG_SURPRISE', blank=True, null=True)  # Field name made lowercase.
    zg_geze_pitch = models.FloatField(db_column='ZG_GEZE_PITCH', blank=True, null=True)  # Field name made lowercase.
    zg_geze_yaw = models.FloatField(db_column='ZG_GEZE_YAW', blank=True, null=True)  # Field name made lowercase.
    zg_body = models.IntegerField(db_column='ZG_BODY', blank=True, null=True)  # Field name made lowercase.
    zg_hand = models.IntegerField(db_column='ZG_HAND', blank=True, null=True)  # Field name made lowercase.
    zg_db = models.IntegerField(db_column='ZG_DB', blank=True, null=True)  # Field name made lowercase.
    zg_tone = models.IntegerField(db_column='ZG_TONE', blank=True, null=True)  # Field name made lowercase.
    zg_speed = models.FloatField(db_column='ZG_SPEED', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    magnitude = models.FloatField(db_column='MAGNITUDE', blank=True, null=True)  # Field name made lowercase.
    str = models.CharField(db_column='STR', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ZG_DATA'


class ImZgGroup(models.Model):
    zg_group = models.AutoField(db_column='ZG_GROUP', primary_key=True)  # Field name made lowercase.
    user_key = models.IntegerField(db_column='USER_KEY')  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ZG_GROUP'


class ImZgJobFair(models.Model):
    job_pk = models.AutoField(db_column='JOB_PK', primary_key=True)  # Field name made lowercase.
    qz_group = models.IntegerField(db_column='QZ_GROUP')  # Field name made lowercase.
    job_fair = models.CharField(db_column='JOB_FAIR', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ZG_JOB_FAIR'


class ImZgUser(models.Model):
    user_key = models.AutoField(db_column='USER_KEY', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', unique=True, max_length=100)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=50)  # Field name made lowercase.
    user_age = models.CharField(db_column='USER_AGE', max_length=50)  # Field name made lowercase.
    user_sex = models.CharField(db_column='USER_SEX', max_length=50)  # Field name made lowercase.
    job_family = models.CharField(db_column='JOB_FAMILY', max_length=50)  # Field name made lowercase.
    job_sub = models.CharField(db_column='JOB_SUB', max_length=50)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=45)  # Field name made lowercase.
    user_edu = models.CharField(db_column='USER_EDU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_crr = models.CharField(db_column='USER_CRR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_anl = models.CharField(db_column='USER_ANL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_crt = models.CharField(db_column='USER_CRT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    user_lng = models.CharField(db_column='USER_LNG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_dty = models.CharField(db_column='USER_DTY', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    user_loc = models.CharField(db_column='USER_LOC', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ZG_USER'


class ImZgUserEtc(models.Model):
    user_key = models.IntegerField(db_column='USER_KEY', unique=True)  # Field name made lowercase.
    job_fair = models.CharField(db_column='JOB_FAIR', max_length=100)  # Field name made lowercase.
    user_edu = models.CharField(db_column='USER_EDU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_crr = models.CharField(db_column='USER_CRR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_anl = models.CharField(db_column='USER_ANL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_crt = models.CharField(db_column='USER_CRT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    user_lng = models.CharField(db_column='USER_LNG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_dty = models.CharField(db_column='USER_DTY', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    user_loc = models.CharField(db_column='USER_LOC', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IM_ZG_USER_ETC'


class JbTest(models.Model):
    user_key = models.AutoField(db_column='USER_KEY', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JB_TEST'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class G5Auth(models.Model):
    mb_id = models.CharField(primary_key=True, max_length=20)
    au_menu = models.CharField(max_length=20)
    au_auth = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'g5_auth'
        unique_together = (('mb_id', 'au_menu'),)


class G5Autosave(models.Model):
    as_id = models.AutoField(primary_key=True)
    mb_id = models.CharField(max_length=20)
    as_uid = models.PositiveBigIntegerField(unique=True)
    as_subject = models.CharField(max_length=255)
    as_content = models.TextField()
    as_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'g5_autosave'


class G5Board(models.Model):
    bo_table = models.CharField(primary_key=True, max_length=20)
    gr_id = models.CharField(max_length=255)
    bo_subject = models.CharField(max_length=255)
    bo_mobile_subject = models.CharField(max_length=255)
    bo_device = models.CharField(max_length=6)
    bo_admin = models.CharField(max_length=255)
    bo_list_level = models.IntegerField()
    bo_read_level = models.IntegerField()
    bo_write_level = models.IntegerField()
    bo_reply_level = models.IntegerField()
    bo_comment_level = models.IntegerField()
    bo_upload_level = models.IntegerField()
    bo_download_level = models.IntegerField()
    bo_html_level = models.IntegerField()
    bo_link_level = models.IntegerField()
    bo_count_delete = models.IntegerField()
    bo_count_modify = models.IntegerField()
    bo_read_point = models.IntegerField()
    bo_write_point = models.IntegerField()
    bo_comment_point = models.IntegerField()
    bo_download_point = models.IntegerField()
    bo_use_category = models.IntegerField()
    bo_category_list = models.TextField()
    bo_use_sideview = models.IntegerField()
    bo_use_file_content = models.IntegerField()
    bo_use_secret = models.IntegerField()
    bo_use_dhtml_editor = models.IntegerField()
    bo_use_rss_view = models.IntegerField()
    bo_use_good = models.IntegerField()
    bo_use_nogood = models.IntegerField()
    bo_use_name = models.IntegerField()
    bo_use_signature = models.IntegerField()
    bo_use_ip_view = models.IntegerField()
    bo_use_list_view = models.IntegerField()
    bo_use_list_file = models.IntegerField()
    bo_use_list_content = models.IntegerField()
    bo_table_width = models.IntegerField()
    bo_subject_len = models.IntegerField()
    bo_mobile_subject_len = models.IntegerField()
    bo_page_rows = models.IntegerField()
    bo_mobile_page_rows = models.IntegerField()
    bo_new = models.IntegerField()
    bo_hot = models.IntegerField()
    bo_image_width = models.IntegerField()
    bo_skin = models.CharField(max_length=255)
    bo_mobile_skin = models.CharField(max_length=255)
    bo_include_head = models.CharField(max_length=255)
    bo_include_tail = models.CharField(max_length=255)
    bo_content_head = models.TextField()
    bo_mobile_content_head = models.TextField()
    bo_content_tail = models.TextField()
    bo_mobile_content_tail = models.TextField()
    bo_insert_content = models.TextField()
    bo_gallery_cols = models.IntegerField()
    bo_gallery_width = models.IntegerField()
    bo_gallery_height = models.IntegerField()
    bo_mobile_gallery_width = models.IntegerField()
    bo_mobile_gallery_height = models.IntegerField()
    bo_upload_size = models.IntegerField()
    bo_reply_order = models.IntegerField()
    bo_use_search = models.IntegerField()
    bo_order = models.IntegerField()
    bo_count_write = models.IntegerField()
    bo_count_comment = models.IntegerField()
    bo_write_min = models.IntegerField()
    bo_write_max = models.IntegerField()
    bo_comment_min = models.IntegerField()
    bo_comment_max = models.IntegerField()
    bo_notice = models.TextField()
    bo_upload_count = models.IntegerField()
    bo_use_email = models.IntegerField()
    bo_use_cert = models.CharField(max_length=8)
    bo_use_sns = models.IntegerField()
    bo_use_captcha = models.IntegerField()
    bo_sort_field = models.CharField(max_length=255)
    bo_1_subj = models.CharField(max_length=255)
    bo_2_subj = models.CharField(max_length=255)
    bo_3_subj = models.CharField(max_length=255)
    bo_4_subj = models.CharField(max_length=255)
    bo_5_subj = models.CharField(max_length=255)
    bo_6_subj = models.CharField(max_length=255)
    bo_7_subj = models.CharField(max_length=255)
    bo_8_subj = models.CharField(max_length=255)
    bo_9_subj = models.CharField(max_length=255)
    bo_10_subj = models.CharField(max_length=255)
    bo_1 = models.CharField(max_length=255)
    bo_2 = models.CharField(max_length=255)
    bo_3 = models.CharField(max_length=255)
    bo_4 = models.CharField(max_length=255)
    bo_5 = models.CharField(max_length=255)
    bo_6 = models.CharField(max_length=255)
    bo_7 = models.CharField(max_length=255)
    bo_8 = models.CharField(max_length=255)
    bo_9 = models.CharField(max_length=255)
    bo_10 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_board'


class G5BoardFile(models.Model):
    bo_table = models.CharField(primary_key=True, max_length=20)
    wr_id = models.IntegerField()
    bf_no = models.IntegerField()
    bf_source = models.CharField(max_length=255)
    bf_file = models.CharField(max_length=255)
    bf_download = models.IntegerField()
    bf_content = models.TextField()
    bf_filesize = models.IntegerField()
    bf_width = models.IntegerField()
    bf_height = models.SmallIntegerField()
    bf_type = models.IntegerField()
    bf_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'g5_board_file'
        unique_together = (('bo_table', 'wr_id', 'bf_no'),)


class G5BoardGood(models.Model):
    bg_id = models.AutoField(primary_key=True)
    bo_table = models.CharField(max_length=20)
    wr_id = models.IntegerField()
    mb_id = models.CharField(max_length=20)
    bg_flag = models.CharField(max_length=255)
    bg_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'g5_board_good'
        unique_together = (('bo_table', 'wr_id', 'mb_id'),)


class G5BoardNew(models.Model):
    bn_id = models.AutoField(primary_key=True)
    bo_table = models.CharField(max_length=20)
    wr_id = models.IntegerField()
    wr_parent = models.IntegerField()
    bn_datetime = models.DateTimeField()
    mb_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'g5_board_new'


class G5CertHistory(models.Model):
    cr_id = models.AutoField(primary_key=True)
    mb_id = models.CharField(max_length=20)
    cr_company = models.CharField(max_length=255)
    cr_method = models.CharField(max_length=255)
    cr_ip = models.CharField(max_length=255)
    cr_date = models.DateField()
    cr_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'g5_cert_history'


class G5Config(models.Model):
    cf_title = models.CharField(max_length=255)
    cf_theme = models.CharField(max_length=255)
    cf_admin = models.CharField(max_length=255)
    cf_admin_email = models.CharField(max_length=255)
    cf_admin_email_name = models.CharField(max_length=255)
    cf_add_script = models.TextField()
    cf_use_point = models.IntegerField()
    cf_point_term = models.IntegerField()
    cf_use_copy_log = models.IntegerField()
    cf_use_email_certify = models.IntegerField()
    cf_login_point = models.IntegerField()
    cf_cut_name = models.IntegerField()
    cf_nick_modify = models.IntegerField()
    cf_new_skin = models.CharField(max_length=255)
    cf_new_rows = models.IntegerField()
    cf_search_skin = models.CharField(max_length=255)
    cf_connect_skin = models.CharField(max_length=255)
    cf_faq_skin = models.CharField(max_length=255)
    cf_read_point = models.IntegerField()
    cf_write_point = models.IntegerField()
    cf_comment_point = models.IntegerField()
    cf_download_point = models.IntegerField()
    cf_write_pages = models.IntegerField()
    cf_mobile_pages = models.IntegerField()
    cf_link_target = models.CharField(max_length=255)
    cf_delay_sec = models.IntegerField()
    cf_filter = models.TextField()
    cf_possible_ip = models.TextField()
    cf_intercept_ip = models.TextField()
    cf_analytics = models.TextField()
    cf_add_meta = models.TextField()
    cf_syndi_token = models.CharField(max_length=255)
    cf_syndi_except = models.TextField()
    cf_member_skin = models.CharField(max_length=255)
    cf_use_homepage = models.IntegerField()
    cf_req_homepage = models.IntegerField()
    cf_use_tel = models.IntegerField()
    cf_req_tel = models.IntegerField()
    cf_use_hp = models.IntegerField()
    cf_req_hp = models.IntegerField()
    cf_use_addr = models.IntegerField()
    cf_req_addr = models.IntegerField()
    cf_use_signature = models.IntegerField()
    cf_req_signature = models.IntegerField()
    cf_use_profile = models.IntegerField()
    cf_req_profile = models.IntegerField()
    cf_register_level = models.IntegerField()
    cf_register_point = models.IntegerField()
    cf_icon_level = models.IntegerField()
    cf_use_recommend = models.IntegerField()
    cf_recommend_point = models.IntegerField()
    cf_leave_day = models.IntegerField()
    cf_search_part = models.IntegerField()
    cf_email_use = models.IntegerField()
    cf_email_wr_super_admin = models.IntegerField()
    cf_email_wr_group_admin = models.IntegerField()
    cf_email_wr_board_admin = models.IntegerField()
    cf_email_wr_write = models.IntegerField()
    cf_email_wr_comment_all = models.IntegerField()
    cf_email_mb_super_admin = models.IntegerField()
    cf_email_mb_member = models.IntegerField()
    cf_email_po_super_admin = models.IntegerField()
    cf_prohibit_id = models.TextField()
    cf_prohibit_email = models.TextField()
    cf_new_del = models.IntegerField()
    cf_memo_del = models.IntegerField()
    cf_visit_del = models.IntegerField()
    cf_popular_del = models.IntegerField()
    cf_optimize_date = models.DateField()
    cf_use_member_icon = models.IntegerField()
    cf_member_icon_size = models.IntegerField()
    cf_member_icon_width = models.IntegerField()
    cf_member_icon_height = models.IntegerField()
    cf_member_img_size = models.IntegerField()
    cf_member_img_width = models.IntegerField()
    cf_member_img_height = models.IntegerField()
    cf_login_minutes = models.IntegerField()
    cf_image_extension = models.CharField(max_length=255)
    cf_flash_extension = models.CharField(max_length=255)
    cf_movie_extension = models.CharField(max_length=255)
    cf_formmail_is_member = models.IntegerField()
    cf_page_rows = models.IntegerField()
    cf_mobile_page_rows = models.IntegerField()
    cf_visit = models.CharField(max_length=255)
    cf_max_po_id = models.IntegerField()
    cf_stipulation = models.TextField()
    cf_privacy = models.TextField()
    cf_open_modify = models.IntegerField()
    cf_memo_send_point = models.IntegerField()
    cf_mobile_new_skin = models.CharField(max_length=255)
    cf_mobile_search_skin = models.CharField(max_length=255)
    cf_mobile_connect_skin = models.CharField(max_length=255)
    cf_mobile_faq_skin = models.CharField(max_length=255)
    cf_mobile_member_skin = models.CharField(max_length=255)
    cf_captcha_mp3 = models.CharField(max_length=255)
    cf_editor = models.CharField(max_length=255)
    cf_cert_use = models.IntegerField()
    cf_cert_ipin = models.CharField(max_length=255)
    cf_cert_hp = models.CharField(max_length=255)
    cf_cert_kcb_cd = models.CharField(max_length=255)
    cf_cert_kcp_cd = models.CharField(max_length=255)
    cf_lg_mid = models.CharField(max_length=255)
    cf_lg_mert_key = models.CharField(max_length=255)
    cf_cert_limit = models.IntegerField()
    cf_cert_req = models.IntegerField()
    cf_sms_use = models.CharField(max_length=255)
    cf_sms_type = models.CharField(max_length=10)
    cf_icode_id = models.CharField(max_length=255)
    cf_icode_pw = models.CharField(max_length=255)
    cf_icode_server_ip = models.CharField(max_length=255)
    cf_icode_server_port = models.CharField(max_length=255)
    cf_googl_shorturl_apikey = models.CharField(max_length=255)
    cf_social_login_use = models.IntegerField()
    cf_social_servicelist = models.CharField(max_length=255)
    cf_payco_clientid = models.CharField(max_length=100)
    cf_payco_secret = models.CharField(max_length=100)
    cf_facebook_appid = models.CharField(max_length=255)
    cf_facebook_secret = models.CharField(max_length=255)
    cf_twitter_key = models.CharField(max_length=255)
    cf_twitter_secret = models.CharField(max_length=255)
    cf_google_clientid = models.CharField(max_length=100)
    cf_google_secret = models.CharField(max_length=100)
    cf_naver_clientid = models.CharField(max_length=100)
    cf_naver_secret = models.CharField(max_length=100)
    cf_kakao_rest_key = models.CharField(max_length=100)
    cf_kakao_client_secret = models.CharField(max_length=100)
    cf_kakao_js_apikey = models.CharField(max_length=255)
    cf_captcha = models.CharField(max_length=100)
    cf_recaptcha_site_key = models.CharField(max_length=100)
    cf_recaptcha_secret_key = models.CharField(max_length=100)
    cf_1_subj = models.CharField(max_length=255)
    cf_2_subj = models.CharField(max_length=255)
    cf_3_subj = models.CharField(max_length=255)
    cf_4_subj = models.CharField(max_length=255)
    cf_5_subj = models.CharField(max_length=255)
    cf_6_subj = models.CharField(max_length=255)
    cf_7_subj = models.CharField(max_length=255)
    cf_8_subj = models.CharField(max_length=255)
    cf_9_subj = models.CharField(max_length=255)
    cf_10_subj = models.CharField(max_length=255)
    cf_1 = models.CharField(max_length=255)
    cf_2 = models.CharField(max_length=255)
    cf_3 = models.CharField(max_length=255)
    cf_4 = models.CharField(max_length=255)
    cf_5 = models.CharField(max_length=255)
    cf_6 = models.CharField(max_length=255)
    cf_7 = models.CharField(max_length=255)
    cf_8 = models.CharField(max_length=255)
    cf_9 = models.CharField(max_length=255)
    cf_10 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_config'


class G5Content(models.Model):
    co_id = models.CharField(primary_key=True, max_length=20)
    co_html = models.IntegerField()
    co_subject = models.CharField(max_length=255)
    co_content = models.TextField()
    co_mobile_content = models.TextField()
    co_skin = models.CharField(max_length=255)
    co_mobile_skin = models.CharField(max_length=255)
    co_tag_filter_use = models.IntegerField()
    co_hit = models.IntegerField()
    co_include_head = models.CharField(max_length=255)
    co_include_tail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_content'


class G5Faq(models.Model):
    fa_id = models.AutoField(primary_key=True)
    fm_id = models.IntegerField()
    fa_subject = models.TextField()
    fa_content = models.TextField()
    fa_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'g5_faq'


class G5FaqMaster(models.Model):
    fm_id = models.AutoField(primary_key=True)
    fm_subject = models.CharField(max_length=255)
    fm_head_html = models.TextField()
    fm_tail_html = models.TextField()
    fm_mobile_head_html = models.TextField()
    fm_mobile_tail_html = models.TextField()
    fm_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'g5_faq_master'


class G5Group(models.Model):
    gr_id = models.CharField(primary_key=True, max_length=10)
    gr_subject = models.CharField(max_length=255)
    gr_device = models.CharField(max_length=6)
    gr_admin = models.CharField(max_length=255)
    gr_use_access = models.IntegerField()
    gr_order = models.IntegerField()
    gr_1_subj = models.CharField(max_length=255)
    gr_2_subj = models.CharField(max_length=255)
    gr_3_subj = models.CharField(max_length=255)
    gr_4_subj = models.CharField(max_length=255)
    gr_5_subj = models.CharField(max_length=255)
    gr_6_subj = models.CharField(max_length=255)
    gr_7_subj = models.CharField(max_length=255)
    gr_8_subj = models.CharField(max_length=255)
    gr_9_subj = models.CharField(max_length=255)
    gr_10_subj = models.CharField(max_length=255)
    gr_1 = models.CharField(max_length=255)
    gr_2 = models.CharField(max_length=255)
    gr_3 = models.CharField(max_length=255)
    gr_4 = models.CharField(max_length=255)
    gr_5 = models.CharField(max_length=255)
    gr_6 = models.CharField(max_length=255)
    gr_7 = models.CharField(max_length=255)
    gr_8 = models.CharField(max_length=255)
    gr_9 = models.CharField(max_length=255)
    gr_10 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_group'


class G5GroupMember(models.Model):
    gm_id = models.AutoField(primary_key=True)
    gr_id = models.CharField(max_length=255)
    mb_id = models.CharField(max_length=20)
    gm_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'g5_group_member'


class G5Login(models.Model):
    lo_ip = models.CharField(primary_key=True, max_length=255)
    mb_id = models.CharField(max_length=20)
    lo_datetime = models.DateTimeField()
    lo_location = models.TextField()
    lo_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'g5_login'


class G5Mail(models.Model):
    ma_id = models.AutoField(primary_key=True)
    ma_subject = models.CharField(max_length=255)
    ma_content = models.TextField()
    ma_time = models.DateTimeField()
    ma_ip = models.CharField(max_length=255)
    ma_last_option = models.TextField()

    class Meta:
        managed = False
        db_table = 'g5_mail'


class G5Member(models.Model):
    mb_no = models.AutoField(primary_key=True)
    mb_id = models.CharField(unique=True, max_length=20)
    mb_password = models.CharField(max_length=255)
    mb_name = models.CharField(max_length=255)
    mb_nick = models.CharField(max_length=255)
    mb_nick_date = models.DateField()
    mb_email = models.CharField(max_length=255)
    mb_homepage = models.CharField(max_length=255)
    mb_level = models.IntegerField()
    mb_sex = models.CharField(max_length=1)
    mb_birth = models.CharField(max_length=255)
    mb_tel = models.CharField(max_length=255)
    mb_hp = models.CharField(max_length=255)
    mb_certify = models.CharField(max_length=20)
    mb_adult = models.IntegerField()
    mb_dupinfo = models.CharField(max_length=255)
    mb_zip1 = models.CharField(max_length=3)
    mb_zip2 = models.CharField(max_length=3)
    mb_addr1 = models.CharField(max_length=255)
    mb_addr2 = models.CharField(max_length=255)
    mb_addr3 = models.CharField(max_length=255)
    mb_addr_jibeon = models.CharField(max_length=255)
    mb_signature = models.TextField()
    mb_recommend = models.CharField(max_length=255)
    mb_point = models.IntegerField()
    mb_today_login = models.DateTimeField()
    mb_login_ip = models.CharField(max_length=255)
    mb_datetime = models.DateTimeField()
    mb_ip = models.CharField(max_length=255)
    mb_leave_date = models.CharField(max_length=8)
    mb_intercept_date = models.CharField(max_length=8)
    mb_email_certify = models.DateTimeField()
    mb_email_certify2 = models.CharField(max_length=255)
    mb_memo = models.TextField()
    mb_lost_certify = models.CharField(max_length=255)
    mb_mailling = models.IntegerField()
    mb_sms = models.IntegerField()
    mb_open = models.IntegerField()
    mb_open_date = models.DateField()
    mb_profile = models.TextField()
    mb_memo_call = models.CharField(max_length=255)
    mb_1 = models.CharField(max_length=255)
    mb_2 = models.CharField(max_length=255)
    mb_3 = models.CharField(max_length=255)
    mb_4 = models.CharField(max_length=255)
    mb_5 = models.CharField(max_length=255)
    mb_6 = models.CharField(max_length=255)
    mb_7 = models.CharField(max_length=255)
    mb_8 = models.CharField(max_length=255)
    mb_9 = models.CharField(max_length=255)
    mb_10 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_member'


class G5Memo(models.Model):
    me_id = models.IntegerField(primary_key=True)
    me_recv_mb_id = models.CharField(max_length=20)
    me_send_mb_id = models.CharField(max_length=20)
    me_send_datetime = models.DateTimeField()
    me_read_datetime = models.DateTimeField()
    me_memo = models.TextField()

    class Meta:
        managed = False
        db_table = 'g5_memo'


class G5Menu(models.Model):
    me_id = models.AutoField(primary_key=True)
    me_code = models.CharField(max_length=255)
    me_name = models.CharField(max_length=255)
    me_link = models.CharField(max_length=255)
    me_target = models.CharField(max_length=255)
    me_order = models.IntegerField()
    me_use = models.IntegerField()
    me_mobile_use = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'g5_menu'


class G5NewWin(models.Model):
    nw_id = models.AutoField(primary_key=True)
    nw_device = models.CharField(max_length=10)
    nw_begin_time = models.DateTimeField()
    nw_end_time = models.DateTimeField()
    nw_disable_hours = models.IntegerField()
    nw_left = models.IntegerField()
    nw_top = models.IntegerField()
    nw_height = models.IntegerField()
    nw_width = models.IntegerField()
    nw_subject = models.TextField()
    nw_content = models.TextField()
    nw_content_html = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'g5_new_win'


class G5Point(models.Model):
    po_id = models.AutoField(primary_key=True)
    mb_id = models.CharField(max_length=20)
    po_datetime = models.DateTimeField()
    po_content = models.CharField(max_length=255)
    po_point = models.IntegerField()
    po_use_point = models.IntegerField()
    po_expired = models.IntegerField()
    po_expire_date = models.DateField()
    po_mb_point = models.IntegerField()
    po_rel_table = models.CharField(max_length=20)
    po_rel_id = models.CharField(max_length=20)
    po_rel_action = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_point'


class G5Poll(models.Model):
    po_id = models.AutoField(primary_key=True)
    po_subject = models.CharField(max_length=255)
    po_poll1 = models.CharField(max_length=255)
    po_poll2 = models.CharField(max_length=255)
    po_poll3 = models.CharField(max_length=255)
    po_poll4 = models.CharField(max_length=255)
    po_poll5 = models.CharField(max_length=255)
    po_poll6 = models.CharField(max_length=255)
    po_poll7 = models.CharField(max_length=255)
    po_poll8 = models.CharField(max_length=255)
    po_poll9 = models.CharField(max_length=255)
    po_cnt1 = models.IntegerField()
    po_cnt2 = models.IntegerField()
    po_cnt3 = models.IntegerField()
    po_cnt4 = models.IntegerField()
    po_cnt5 = models.IntegerField()
    po_cnt6 = models.IntegerField()
    po_cnt7 = models.IntegerField()
    po_cnt8 = models.IntegerField()
    po_cnt9 = models.IntegerField()
    po_etc = models.CharField(max_length=255)
    po_level = models.IntegerField()
    po_point = models.IntegerField()
    po_date = models.DateField()
    po_ips = models.TextField()
    mb_ids = models.TextField()

    class Meta:
        managed = False
        db_table = 'g5_poll'


class G5PollEtc(models.Model):
    pc_id = models.IntegerField(primary_key=True)
    po_id = models.IntegerField()
    mb_id = models.CharField(max_length=20)
    pc_name = models.CharField(max_length=255)
    pc_idea = models.CharField(max_length=255)
    pc_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'g5_poll_etc'


class G5Popular(models.Model):
    pp_id = models.AutoField(primary_key=True)
    pp_word = models.CharField(max_length=50)
    pp_date = models.DateField()
    pp_ip = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'g5_popular'
        unique_together = (('pp_date', 'pp_word', 'pp_ip'),)


class G5QaConfig(models.Model):
    qa_title = models.CharField(max_length=255)
    qa_category = models.CharField(max_length=255)
    qa_skin = models.CharField(max_length=255)
    qa_mobile_skin = models.CharField(max_length=255)
    qa_use_email = models.IntegerField()
    qa_req_email = models.IntegerField()
    qa_use_hp = models.IntegerField()
    qa_req_hp = models.IntegerField()
    qa_use_sms = models.IntegerField()
    qa_send_number = models.CharField(max_length=255)
    qa_admin_hp = models.CharField(max_length=255)
    qa_admin_email = models.CharField(max_length=255)
    qa_use_editor = models.IntegerField()
    qa_subject_len = models.IntegerField()
    qa_mobile_subject_len = models.IntegerField()
    qa_page_rows = models.IntegerField()
    qa_mobile_page_rows = models.IntegerField()
    qa_image_width = models.IntegerField()
    qa_upload_size = models.IntegerField()
    qa_insert_content = models.TextField()
    qa_include_head = models.CharField(max_length=255)
    qa_include_tail = models.CharField(max_length=255)
    qa_content_head = models.TextField()
    qa_content_tail = models.TextField()
    qa_mobile_content_head = models.TextField()
    qa_mobile_content_tail = models.TextField()
    qa_1_subj = models.CharField(max_length=255)
    qa_2_subj = models.CharField(max_length=255)
    qa_3_subj = models.CharField(max_length=255)
    qa_4_subj = models.CharField(max_length=255)
    qa_5_subj = models.CharField(max_length=255)
    qa_1 = models.CharField(max_length=255)
    qa_2 = models.CharField(max_length=255)
    qa_3 = models.CharField(max_length=255)
    qa_4 = models.CharField(max_length=255)
    qa_5 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_qa_config'


class G5QaContent(models.Model):
    qa_id = models.AutoField(primary_key=True)
    qa_num = models.IntegerField()
    qa_parent = models.IntegerField()
    qa_related = models.IntegerField()
    mb_id = models.CharField(max_length=20)
    qa_name = models.CharField(max_length=255)
    qa_email = models.CharField(max_length=255)
    qa_hp = models.CharField(max_length=255)
    qa_type = models.IntegerField()
    qa_category = models.CharField(max_length=255)
    qa_email_recv = models.IntegerField()
    qa_sms_recv = models.IntegerField()
    qa_html = models.IntegerField()
    qa_subject = models.CharField(max_length=255)
    qa_content = models.TextField()
    qa_status = models.IntegerField()
    qa_file1 = models.CharField(max_length=255)
    qa_source1 = models.CharField(max_length=255)
    qa_file2 = models.CharField(max_length=255)
    qa_source2 = models.CharField(max_length=255)
    qa_ip = models.CharField(max_length=255)
    qa_datetime = models.DateTimeField()
    qa_1 = models.CharField(max_length=255)
    qa_2 = models.CharField(max_length=255)
    qa_3 = models.CharField(max_length=255)
    qa_4 = models.CharField(max_length=255)
    qa_5 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_qa_content'


class G5Scrap(models.Model):
    ms_id = models.AutoField(primary_key=True)
    mb_id = models.CharField(max_length=20)
    bo_table = models.CharField(max_length=20)
    wr_id = models.CharField(max_length=15)
    ms_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'g5_scrap'


class G5Uniqid(models.Model):
    uq_id = models.PositiveBigIntegerField(primary_key=True)
    uq_ip = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_uniqid'


class G5Visit(models.Model):
    vi_id = models.IntegerField(primary_key=True)
    vi_ip = models.CharField(max_length=255)
    vi_date = models.DateField()
    vi_time = models.TimeField()
    vi_referer = models.TextField()
    vi_agent = models.CharField(max_length=255)
    vi_browser = models.CharField(max_length=255)
    vi_os = models.CharField(max_length=255)
    vi_device = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_visit'
        unique_together = (('vi_ip', 'vi_date'),)


class G5VisitSum(models.Model):
    vs_date = models.DateField(primary_key=True)
    vs_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'g5_visit_sum'


class G5WriteWithmindFaq(models.Model):
    wr_id = models.AutoField(primary_key=True)
    wr_num = models.IntegerField()
    wr_reply = models.CharField(max_length=10)
    wr_parent = models.IntegerField()
    wr_is_comment = models.IntegerField()
    wr_comment = models.IntegerField()
    wr_comment_reply = models.CharField(max_length=5)
    ca_name = models.CharField(max_length=255)
    wr_option = models.CharField(max_length=23)
    wr_subject = models.CharField(max_length=255)
    wr_content = models.TextField()
    wr_link1 = models.TextField()
    wr_link2 = models.TextField()
    wr_link1_hit = models.IntegerField()
    wr_link2_hit = models.IntegerField()
    wr_hit = models.IntegerField()
    wr_good = models.IntegerField()
    wr_nogood = models.IntegerField()
    mb_id = models.CharField(max_length=20)
    wr_password = models.CharField(max_length=255)
    wr_name = models.CharField(max_length=255)
    wr_email = models.CharField(max_length=255)
    wr_homepage = models.CharField(max_length=255)
    wr_datetime = models.DateTimeField()
    wr_file = models.IntegerField()
    wr_last = models.CharField(max_length=19)
    wr_ip = models.CharField(max_length=255)
    wr_facebook_user = models.CharField(max_length=255)
    wr_twitter_user = models.CharField(max_length=255)
    wr_1 = models.CharField(max_length=255)
    wr_2 = models.CharField(max_length=255)
    wr_3 = models.CharField(max_length=255)
    wr_4 = models.CharField(max_length=255)
    wr_5 = models.CharField(max_length=255)
    wr_6 = models.CharField(max_length=255)
    wr_7 = models.CharField(max_length=255)
    wr_8 = models.CharField(max_length=255)
    wr_9 = models.CharField(max_length=255)
    wr_10 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_write_withmind_faq'


class G5WriteWithmindNotice(models.Model):
    wr_id = models.AutoField(primary_key=True)
    wr_num = models.IntegerField()
    wr_reply = models.CharField(max_length=10)
    wr_parent = models.IntegerField()
    wr_is_comment = models.IntegerField()
    wr_comment = models.IntegerField()
    wr_comment_reply = models.CharField(max_length=5)
    ca_name = models.CharField(max_length=255)
    wr_option = models.CharField(max_length=23)
    wr_subject = models.CharField(max_length=255)
    wr_content = models.TextField()
    wr_link1 = models.TextField()
    wr_link2 = models.TextField()
    wr_link1_hit = models.IntegerField()
    wr_link2_hit = models.IntegerField()
    wr_hit = models.IntegerField()
    wr_good = models.IntegerField()
    wr_nogood = models.IntegerField()
    mb_id = models.CharField(max_length=20)
    wr_password = models.CharField(max_length=255)
    wr_name = models.CharField(max_length=255)
    wr_email = models.CharField(max_length=255)
    wr_homepage = models.CharField(max_length=255)
    wr_datetime = models.DateTimeField()
    wr_file = models.IntegerField()
    wr_last = models.CharField(max_length=19)
    wr_ip = models.CharField(max_length=255)
    wr_facebook_user = models.CharField(max_length=255)
    wr_twitter_user = models.CharField(max_length=255)
    wr_1 = models.CharField(max_length=255)
    wr_2 = models.CharField(max_length=255)
    wr_3 = models.CharField(max_length=255)
    wr_4 = models.CharField(max_length=255)
    wr_5 = models.CharField(max_length=255)
    wr_6 = models.CharField(max_length=255)
    wr_7 = models.CharField(max_length=255)
    wr_8 = models.CharField(max_length=255)
    wr_9 = models.CharField(max_length=255)
    wr_10 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'g5_write_withmind_notice'


class PmaBookmark(models.Model):
    dbase = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    query = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__bookmark'


class PmaCentralColumns(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    col_name = models.CharField(max_length=64)
    col_type = models.CharField(max_length=64)
    col_length = models.TextField(blank=True, null=True)
    col_collation = models.CharField(max_length=64)
    col_isnull = models.IntegerField(db_column='col_isNull')  # Field name made lowercase.
    col_extra = models.CharField(max_length=255, blank=True, null=True)
    col_default = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma__central_columns'
        unique_together = (('db_name', 'col_name'),)


class PmaColumnInfo(models.Model):
    db_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)
    column_name = models.CharField(max_length=64)
    comment = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=255)
    transformation = models.CharField(max_length=255)
    transformation_options = models.CharField(max_length=255)
    input_transformation = models.CharField(max_length=255)
    input_transformation_options = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pma__column_info'
        unique_together = (('db_name', 'table_name', 'column_name'),)


class PmaDesignerSettings(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    settings_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__designer_settings'


class PmaExportTemplates(models.Model):
    username = models.CharField(max_length=64)
    export_type = models.CharField(max_length=10)
    template_name = models.CharField(max_length=64)
    template_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__export_templates'
        unique_together = (('username', 'export_type', 'template_name'),)


class PmaFavorite(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    tables = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__favorite'


class PmaHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=64)
    db = models.CharField(max_length=64)
    table = models.CharField(max_length=64)
    timevalue = models.DateTimeField()
    sqlquery = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__history'


class PmaNavigationhiding(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    item_name = models.CharField(max_length=64)
    item_type = models.CharField(max_length=64)
    db_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pma__navigationhiding'
        unique_together = (('username', 'item_name', 'item_type', 'db_name', 'table_name'),)


class PmaPdfPages(models.Model):
    db_name = models.CharField(max_length=64)
    page_nr = models.AutoField(primary_key=True)
    page_descr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pma__pdf_pages'


class PmaRecent(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    tables = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__recent'


class PmaRelation(models.Model):
    master_db = models.CharField(primary_key=True, max_length=64)
    master_table = models.CharField(max_length=64)
    master_field = models.CharField(max_length=64)
    foreign_db = models.CharField(max_length=64)
    foreign_table = models.CharField(max_length=64)
    foreign_field = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pma__relation'
        unique_together = (('master_db', 'master_table', 'master_field'),)


class PmaSavedsearches(models.Model):
    username = models.CharField(max_length=64)
    db_name = models.CharField(max_length=64)
    search_name = models.CharField(max_length=64)
    search_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__savedsearches'
        unique_together = (('username', 'db_name', 'search_name'),)


class PmaTableCoords(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    pdf_page_number = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pma__table_coords'
        unique_together = (('db_name', 'table_name', 'pdf_page_number'),)


class PmaTableInfo(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    display_field = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pma__table_info'
        unique_together = (('db_name', 'table_name'),)


class PmaTableUiprefs(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    db_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)
    prefs = models.TextField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pma__table_uiprefs'
        unique_together = (('username', 'db_name', 'table_name'),)


class PmaTracking(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    version = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    schema_snapshot = models.TextField()
    schema_sql = models.TextField(blank=True, null=True)
    data_sql = models.TextField(blank=True, null=True)
    tracking = models.CharField(max_length=188, blank=True, null=True)
    tracking_active = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pma__tracking'
        unique_together = (('db_name', 'table_name', 'version'),)


class PmaUserconfig(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    timevalue = models.DateTimeField()
    config_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__userconfig'


class PmaUsergroups(models.Model):
    usergroup = models.CharField(primary_key=True, max_length=64)
    tab = models.CharField(max_length=64)
    allowed = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'pma__usergroups'
        unique_together = (('usergroup', 'tab', 'allowed'),)


class PmaUsers(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    usergroup = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pma__users'
        unique_together = (('username', 'usergroup'),)


class Sms5Book(models.Model):
    bk_no = models.AutoField(primary_key=True)
    bg_no = models.IntegerField()
    mb_no = models.IntegerField()
    mb_id = models.CharField(max_length=20)
    bk_name = models.CharField(max_length=255)
    bk_hp = models.CharField(max_length=255)
    bk_receipt = models.IntegerField()
    bk_datetime = models.DateTimeField()
    bk_memo = models.TextField()

    class Meta:
        managed = False
        db_table = 'sms5_book'


class Sms5BookGroup(models.Model):
    bg_no = models.AutoField(primary_key=True)
    bg_name = models.CharField(max_length=255)
    bg_count = models.IntegerField()
    bg_member = models.IntegerField()
    bg_nomember = models.IntegerField()
    bg_receipt = models.IntegerField()
    bg_reject = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sms5_book_group'


class Sms5Config(models.Model):
    cf_phone = models.CharField(max_length=255)
    cf_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms5_config'


class Sms5Form(models.Model):
    fo_no = models.AutoField(primary_key=True)
    fg_no = models.IntegerField()
    fg_member = models.CharField(max_length=1)
    fo_name = models.CharField(max_length=255)
    fo_content = models.TextField()
    fo_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms5_form'


class Sms5FormGroup(models.Model):
    fg_no = models.AutoField(primary_key=True)
    fg_name = models.CharField(max_length=255)
    fg_count = models.IntegerField()
    fg_member = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sms5_form_group'


class Sms5History(models.Model):
    hs_no = models.AutoField(primary_key=True)
    wr_no = models.IntegerField()
    wr_renum = models.IntegerField()
    bg_no = models.IntegerField()
    mb_no = models.IntegerField()
    mb_id = models.CharField(max_length=20)
    bk_no = models.IntegerField()
    hs_name = models.CharField(max_length=30)
    hs_hp = models.CharField(max_length=255)
    hs_datetime = models.DateTimeField()
    hs_flag = models.IntegerField()
    hs_code = models.CharField(max_length=255)
    hs_memo = models.CharField(max_length=255)
    hs_log = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sms5_history'


class Sms5Write(models.Model):
    wr_no = models.IntegerField()
    wr_renum = models.IntegerField()
    wr_reply = models.CharField(max_length=255)
    wr_message = models.CharField(max_length=255)
    wr_booking = models.DateTimeField()
    wr_total = models.IntegerField()
    wr_re_total = models.IntegerField()
    wr_success = models.IntegerField()
    wr_failure = models.IntegerField()
    wr_datetime = models.DateTimeField()
    wr_memo = models.TextField()

    class Meta:
        managed = False
        db_table = 'sms5_write'
