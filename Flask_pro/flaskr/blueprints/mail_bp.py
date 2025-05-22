import random
import string

from flask import Blueprint, request

bp = Blueprint('mail', __name__, url_prefix='/mail')

@bp.route('/captcha')
def get_captcha():
    email = request.args.get('email')
    source = string.digits*4
    captcha = ''.join(random.sample(source, 4))
    print("验证码",captcha)
    return captcha


@bp.route('/send')
def send_mail():
    from ..exts import mail  # 延迟导入，可以避免循环引用
    from flask_mail import Message  # 正确导入 Message
    try:
        # 创建邮件消息
        msg = Message(
            subject='测试邮件',  # 邮件主题
            recipients=['369255095@qq.com'],  # 替换为收件人邮箱
            body='这是一封来自 Flask-Mail 的测试邮件！'  # 邮件正文
        )
        # 添加附件 注意路径在这里是相对路径
        with open('../../test.txt', 'rb') as fp:
            msg.attach(
                filename='../../test.txt',  # 附件文件名
                content_type='text/plain',  # 文件类型
                data=fp.read()  # 文件内容
            )
        mail.send(msg)
        # 发送邮件
        mail.send(msg)
        return '邮件发送成功！'
    except Exception as e:
        return f'邮件发送失败: {str(e)}'
