#!/usr/bin/python
import os
import re
from xml.dom.minidom import parse
import xml.dom.minidom



if __name__ == '__main__':

    print("开始")

    # list1 = ['physics', 'chemistry', 1997, 2000]

    notFoundStrList = ['record_voice_hint', 'release_send_voice_hint', 'cancel_record_voice_hint', 'preview_play_audio_hint',
     'rest_record_time_hint', 'sdcard_not_exist_toast', 'file_not_found_toast', 'sdcard_not_prepare_toast',
     'record_video_failed', 'error_over_count_default', 'error_under_quality', 'error_over_quality',
     'button_sure_default', 'button_sure', 'qr_authorize_login', 'send_verification_code_failure', 'phone_login',
     'password_login', 'nothing_found', 'query_device_msg', 'permission_dialog_content_camera',
     'permission_dialog_content_phone', 'switch_login_function_tip', 'progress_dialog_title', 'progress_dialog_content',
     'mine_switch_account', 'mine_update_version_cn', 'mine_username_empty', 'mine_signature_empty',
     'mine_leixunid_empty', 'mine_leixunid_illegal', 'mine_avatar', 'query_picture_msg', 'set_remark',
     'send_add_contact', 'add_blacklist_tips', 'profile_setting', 'recommend_to_friend', 'set_star', 'complaint',
     'single_select', 'create_new_chat', 'send_more_tips', 'phone_contact', 'recen_chat', 'send_card_tips',
     'send_card_tips_title', 'search_none_tips', 'group_number', 'star_friend', 'phone_permission_tip',
     'device_code_tip2', 'switch_user', 'black', 'msg_sending', 'msg_send_faile', 'msg_withdraw', 'msg_online_long',
     'msg_friend_check', 'msg_delete_session', 'msg_input_hint', 'chat_msg_red', 'chat_msg_unred',
     'emoticons_count_tips', 'emoji_count', 'notify_open_tip', 'add_emoticons_fail', 'code_fail']



    i = 0


    for str in notFoundStrList:
        i = i+1

        print(f'第{i}个是：{str}')




    print("完成.")