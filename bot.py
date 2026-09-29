import datetime
import telebot

import os
import threading
from flask import Flask

TOKEN = "8964311692:AAFY9GPkl5atjAU6fwcb5Yeehlyg6deGqBY"
bot = telebot.TeleBot(TOKEN)

# الآيدي الخاص بك كمشرف لاستلام الطلبات
ADMIN_ID = 1864246317

# قاموس لحفظ حالة المستخدمين المؤقتة
user_states = {}


# دالة القائمة الرئيسية
def main_menu_markup():
  markup = telebot.types.InlineKeyboardMarkup(row_width=1)
  btn1 = telebot.types.InlineKeyboardButton(
      "📸 خدمات انستغرام", callback_data="insta"
  )
  btn2 = telebot.types.InlineKeyboardButton("🎵 خدمات تيك توك", callback_data="tiktok")
  btn3 = telebot.types.InlineKeyboardButton(
      "📞 الدعم الفني", url="https://t.me/a_eet"
  )
  markup.add(btn1, btn2, btn3)
  return markup


@bot.message_handler(commands=["start"])
def send_welcome(message):
  chat_id = message.chat.id
  user_states.pop(chat_id, None)
  welcome_text = (
      "أهلاً بك عزيزي في بوت خدمات الرشق والتسويق الرقمي 🚀\n\n"
      "نحن هنا لتوفير أسرع وأفضل الخدمات لحساباتك بأفضل الأسعار.\n"
      "اختر القسم المناسب لك من الأزرار أدناه للبدء:"
  )
  bot.send_message(chat_id, welcome_text, reply_markup=main_menu_markup())


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
  chat_id = call.message.chat.id

  if call.data == "back_home":
    user_states.pop(chat_id, None)
    welcome_text = (
        "أهلاً بك عزيزي في بوت خدمات الرشق والتسويق الرقمي 🚀\n\n"
        "نحن هنا لتوفير أسرع وأفضل الخدمات لحساباتك بأفضل الأسعار.\n"
        "اختر القسم المناسب لك من الأزرار أدناه للبدء:"
    )
    bot.edit_message_text(
        welcome_text,
        chat_id=chat_id,
        message_id=call.message.message_id,
        reply_markup=main_menu_markup(),
    )

  # ==================== قسم انستغرام ====================
  elif call.data == "insta":
    text = (
        "📸 قسم خدمات انستغرام:\nاختر الخدمة المطلوبة لعرض الأسعار والتفاصيل:"
    )
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    b1 = telebot.types.InlineKeyboardButton(
        "1️⃣ متابعين انستغرام (حقيقيين)", callback_data="insta_followers"
    )
    b2 = telebot.types.InlineKeyboardButton(
        "2️⃣ لايكات انستغرام (عرب)", callback_data="insta_likes"
    )
    back = telebot.types.InlineKeyboardButton(
        "🔙 القائمة الرئيسية", callback_data="back_home"
    )
    markup.add(b1, b2, back)
    bot.edit_message_text(
        text, chat_id=chat_id, message_id=call.message.message_id, reply_markup=markup
    )

  elif call.data == "insta_followers":
    text = (
        "📸 أسعار متابعين انستغرام:\n\n"
        "▫️ 1,000 متابع = 3$\n"
        "▫️ 5,000 متابع = 14$\n"
        "▫️ 10,000 متابع = 25$\n\n"
        "⚡ الضمان: تعويض في حال النقصان."
    )
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    order_btn = telebot.types.InlineKeyboardButton(
        "🛒 طلب الخدمة الآن", callback_data="order_insta_f"
    )
    back_section = telebot.types.InlineKeyboardButton(
        "🔙 رجوع لقسم انستغرام", callback_data="insta"
    )
    back_home = telebot.types.InlineKeyboardButton(
        "🏠 القائمة الرئيسية", callback_data="back_home"
    )
    markup.add(order_btn, back_section, back_home)
    bot.edit_message_text(
        text, chat_id=chat_id, message_id=call.message.message_id, reply_markup=markup
    )

  elif call.data == "insta_likes":
    text = (
        "❤️ أسعار لايكات انستغرام (عرب):\n\n"
        "▫️ 1,000 لايك = 1.5$\n"
        "▫️ 5,000 لايك = 6$\n\n"
        "⚡ السرعة: فورية."
    )
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    order_btn = telebot.types.InlineKeyboardButton(
        "🛒 طلب الخدمة الآن", callback_data="order_insta_l"
    )
    back_section = telebot.types.InlineKeyboardButton(
        "🔙 رجوع لقسم انستغرام", callback_data="insta"
    )
    back_home = telebot.types.InlineKeyboardButton(
        "🏠 القائمة الرئيسية", callback_data="back_home"
    )
    markup.add(order_btn, back_section, back_home)
    bot.edit_message_text(
        text, chat_id=chat_id, message_id=call.message.message_id, reply_markup=markup
    )

  # ==================== قسم تيك توك ====================
  elif call.data == "tiktok":
    text = "🎵 قسم خدمات تيك توك:\nاختر الخدمة المطلوبة لعرض الأسعار:"
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    b1 = telebot.types.InlineKeyboardButton(
        "1️⃣ متابعين تيك توك", callback_data="tk_followers"
    )
    b2 = telebot.types.InlineKeyboardButton(
        "2️⃣ لايكات تيك توك", callback_data="tk_likes"
    )
    back = telebot.types.InlineKeyboardButton(
        "🔙 القائمة الرئيسية", callback_data="back_home"
    )
    markup.add(b1, b2, back)
    bot.edit_message_text(
        text, chat_id=chat_id, message_id=call.message.message_id, reply_markup=markup
    )

  elif call.data == "tk_followers":
    text = (
        "🎵 أسعار متابعين تيك توك:\n\n"
        "▫️ 1,000 متابع = 2.5$\n"
        "▫️ 5,000 متابع = 11$\n\n"
        "⚡ السرعة: عالية."
    )
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    order_btn = telebot.types.InlineKeyboardButton(
        "🛒 طلب الخدمة الآن", callback_data="order_tk_f"
    )
    back_section = telebot.types.InlineKeyboardButton(
        "🔙 رجوع لقسم تيك توك", callback_data="tiktok"
    )
    back_home = telebot.types.InlineKeyboardButton(
        "🏠 القائمة الرئيسية", callback_data="back_home"
    )
    markup.add(order_btn, back_section, back_home)
    bot.edit_message_text(
        text, chat_id=chat_id, message_id=call.message.message_id, reply_markup=markup
    )

  elif call.data == "tk_likes":
    text = (
        "❤️ أسعار لايكات تيك توك:\n\n"
        "▫️ 1,000 لايك = 1$\n"
        "▫️ 5,000 لايك = 4.5$\n\n"
        "⚡ السرعة: فورية."
    )
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    order_btn = telebot.types.InlineKeyboardButton(
        "🛒 طلب الخدمة الآن", callback_data="order_tk_l"
    )
    back_section = telebot.types.InlineKeyboardButton(
        "🔙 رجوع لقسم تيك توك", callback_data="tiktok"
    )
    back_home = telebot.types.InlineKeyboardButton(
        "🏠 القائمة الرئيسية", callback_data="back_home"
    )
    markup.add(order_btn, back_section, back_home)
    bot.edit_message_text(
        text, chat_id=chat_id, message_id=call.message.message_id, reply_markup=markup
    )

  # ==================== الانتقال لطلب تفاصيل الطلب كتابةً ====================
  elif call.data in [
      "order_insta_f",
      "order_insta_l",
      "order_tk_f",
      "order_tk_l",
  ]:
    service_map = {
        "order_insta_f": "متابعين انستغرام 📸",
        "order_insta_l": "لايكات انستغرام ❤️",
        "order_tk_f": "متابعين تيك توك 🎵",
        "order_tk_l": "لايكات تيك توك ❤️",
    }

    selected_service = service_map.get(call.data)
    is_profile = "followers" in call.data or "_f" in call.data

    # تخزين حالة المستخدم بانتظار كتابة تفاصيل الطلب (الباقة والرابط)
    user_states[chat_id] = {
        "service": selected_service,
        "type": "profile" if is_profile else "post",
        "step": "waiting_for_order_text",
    }

    if is_profile:
      prompt_text = (
          f"🎯 الخدمة المختارة: {selected_service}\n\n"
          "✍️ **يرجى إرسال رسالة واحدة تحتوي على:**\n"
          "1️⃣ رقم الباقة أو العرض المطلوب\n"
          "2️⃣ رابط الحساب أو اليوزر الخاص بك\n\n"
          "*(مثال: عرض رقم 1 ويوزري @username)*"
      )
    else:
      prompt_text = (
          f"🎯 الخدمة المختارة: {selected_service}\n\n"
          "✍️ **يرجى إرسال رسالة واحدة تحتوي على:**\n"
          "1️⃣ رقم الباقة أو العرض المطلوب\n"
          "2️⃣ رابط الفيديو أو المنشور (الريل)\n\n"
          "*(مثال: عرض رقم 2 ورابط الفيديو...)*"
      )

    markup = telebot.types.InlineKeyboardMarkup()
    back_btn = telebot.types.InlineKeyboardButton(
        "🔙 إلغاء والعودة", callback_data="back_home"
    )
    markup.add(back_btn)

    bot.edit_message_text(
        prompt_text,
        chat_id=chat_id,
        message_id=call.message.message_id,
        reply_markup=markup,
    )


# استقبال طلب الزبون النصي وتحويله للمشرف
@bot.message_handler(
    func=lambda message: message.chat.id in user_states
    and user_states[message.chat.id]["step"] == "waiting_for_order_text"
)
def receive_order_text(message):
  chat_id = message.chat.id
  order_details = message.text
  user = message.from_user

  username_str = (
      f"@{user.username}" if user.username else f"{user.first_name}"
  )
  state = user_states[chat_id]
  service_name = state["service"]

import datetime
# لتحويل وقت رسالة الزبون من نظام الكود التجريدي إلى التاريخ والوقت المحلي:
order_time = (datetime.datetime.fromtimestamp(message.date) + datetime.timedelta(hours=3)).strftime("%Y-%m-%d | %I:%M %p")

# 1. إرسال رسالة تأكيد للزبون
bot.reply_to(
      message,
      "✅ تم ارسال طلبك بنجاح!\n\n- سيتم التواصل معك من قبل الدعم الفني أو"
      " المشرفين في أقرب وقت لتنفيذ طلبك.",
  )

  # 2. إرسال الطلب للمشرف بالتفاصيل الكاملة
 admin_notification = (
      f"🚨 اجاك طلب جديد!\n\n"
      f"👤 معلومات الزبون: {username_str}\n"
      f"📅 وقت الطلب: {order_time}\n"
      f"⚡ الخدمة: {service_name}\n"
      f"📝 تفاصيل الطلب (الباقة والرابط):\n{order_details}"
  )

try:
    bot.send_message(ADMIN_ID, admin_notification)
except Exception as e:
    print(f"خطأ في إرسال الإشعار للمشرف: {e}")

  # مسح الحالة بعد إتمام الطلب
user_states.pop(chat_id, None)


print(
    "البوت يعمل الآن بنظام الطلب النصي المرن (بدون أزرار كميات مقيدة)...."
)


app = Flask(__name__)

@app.route('/')
def home():
    return "البوت يعمل بنجاح!"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
