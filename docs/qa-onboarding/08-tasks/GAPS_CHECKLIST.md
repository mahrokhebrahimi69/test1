# چک‌لیست کمبودها (Gaps) — چه چیزهایی کم/ناقص است؟

> این صفحه لیست چیزهایی است که با اطلاعات فعلی **کامل نیست** و باید توسط Senior QA / اسکوادها تکمیل شود.  
> وضعیت‌ها: `Open` / `In Progress` / `Done` / `Blocked`

---

## اولویت بحرانی (بلاکر انبوردینگ)

| ID | کمبود | چرا مهم است | Owner پیشنهادی | وضعیت |
| --- | --- | --- | --- | --- |
| G-01 | معنی و دامنه **TPCH** مشخص نیست | اسکواد بدون تعریف در نقشه تیم می‌ماند | Senior QA + Eng | Open |
| G-02 | مرز دقیق **COIMP vs PROMC** نامشخص است | تست کوپن/پروموشن دوباره‌کاری یا جاافتادگی دارد | Senior QA + Promo teams | Open |
| G-03 | لیست کامل سرویس‌های Platform از Git موجود نیست | فقط Iris/Icarus/Artemis/Yggdrasil/Falafel را داریم | Platform + Senior QA | Open |
| G-04 | اکانت‌های تست استاندارد نداریم | نیروی جدید عملاً نمی‌تواند Smoke بزند | Senior QA | Open |
| G-05 | ماتریس دسترسی لینک‌ها ناقص است | لینک‌ها هست، ولی Granted/Blocked مشخص نیست | QA Lead + IT/Sec | Open |
| G-06 | State Machine سفارش (OMS) مستند نشده | بدون آن E2E و تریاژ باگ ضعیف است | OMS + Senior QA | Open |
| G-07 | قوانین Availability بر اساس آدرس مکتوب نیست | بخش کلیدی Discovery بدون معیار تست است | Search & Discovery | Open |
| G-08 | کاتالوگ اجزای Page Builder ناقص است | Carousel/Tile گفته شد؛ بقیه اجزا و قوانین Publish نه | Search & Discovery + Product | Open |

---

## کمبودهای دامنه اسکوادها

| ID | کمبود | جزئیات لازم | وضعیت |
| --- | --- | --- | --- |
| G-09 | AI | فلو دقیق Moderator، مدل‌ها، پنل، false positive/negative | Open |
| G-10 | Chef | نقش‌ها، فلوهای عملیاتی، تفاوت با BO | Open |
| G-11 | Delivery | وضعیت‌ها، Zap integration، لغو/تأخیر | Open |
| G-12 | Finance | درگاه‌ها per env، refund، reconcilation | Open |
| G-13 | Menu Management | مدل داده منو، sync با Vendor/Discovery | Open |
| G-14 | Vendor | نقش‌ها، فلو سفارش در پنل، محیط‌ها | Open |
| G-15 | Search & Discovery | سرچ relevancy، سبد قبل از سفارش، page builder | Open |

---

## کمبودهای Platform (با وجود مستندات خوب)

| ID | کمبود | توضیح | وضعیت |
| --- | --- | --- | --- |
| G-16 | تأیید صحت مستندات با کد روز | Drift در Icarus/Yggdrasil/Artemis گزارش شده | Open |
| G-17 | محیط و Base URL واقعی Stage/Prod هر سرویس | در راهنماها localhost زیاد است | Open |
| G-18 | مجموعه Postman/Newman رسمی per service | برای انبوردینگ عملی لازم است | Open |
| G-19 | Owner on-call هر سرویس Platform | برای تریاژ | Open |
| G-20 | سرویس‌های Platform خارج از ۵ مورد فعلی | نام‌های اساطیری دیگر در Git | Open |

---

## کمبودهای محصول/واژه‌نامه/UI

| ID | کمبود | توضیح | وضعیت |
| --- | --- | --- | --- |
| G-21 | اسکرین‌شات مرجع برای Carousel/Tile/Banner/… | تعریف متنی بدون تصویر کافی نیست | Open |
| G-22 | فهرست کامل اصطلاحات Design System محصول | فقط بخشی گفته شد | Open |
| G-23 | تفاوت هوم‌پیج شهرها (نمونه‌های واقعی) | مثال مشهد گفته شد؛ نمونه صفحه لازم است | Open |
| G-24 | نقشه صفحات اصلی tapsi.food | Home / Search / Vendor / Cart / Order Tracking / Profile | Open |

---

## کمبودهای ابزار و عملیات QA

| ID | کمبود | توضیح | وضعیت |
| --- | --- | --- | --- |
| G-25 | Runbook دیباگ با Kibana | از کجا Trace را پیدا کنیم | Open |
| G-26 | کوئری‌های آماده Metabase | سفارش، کاربر، پرداخت، ریویو | Open |
| G-27 | توضیح Datagif در استک ما | لینک هست، نقشش نامشخص است | Open |
| G-28 | سیاست تست Prod | چه چیزهایی مجاز/غیرمجاز است | Open |
| G-29 | قالب تست‌پلن استاندارد تیم | هنوز توافق‌شده نیست | Open |
| G-30 | منبع حقیقت برای نسخه دیپلوی‌شده | CD چطور خوانده شود | Open |

---

## کمبودهای امنیتی/حریم خصوصی برای QA

| ID | کمبود | توضیح | وضعیت |
| --- | --- | --- | --- |
| G-31 | داده‌های حساس در لاگ | Iris/Icarus/Artemis نکات privacy دارند؛ سیاست تیم؟ | Open |
| G-32 | دسترسی به control-plane/setup/migrate در Icarus | ریسک امنیتی شناخته‌شده؛ کنترل شبکه؟ | Open |
| G-33 | مدیریت شماره موبایل واقعی برای OTP | فرایند دریافت سیم‌کارت/شماره تست | Open |

---

## چیزهایی که الان خوب است (نیاز به اختراع مجدد ندارد)

- مستندات عمیق Iris
- مستندات عمیق Icarus
- مستندات عمیق Artemis
- مستندات عمیق Yggdrasil
- مستندات عمیق Falafel
- تصویر اولیه اسکوادها و Journey
- فهرست اولیه لینک سامانه‌ها
- تعریف اولیه واژه‌های Carousel/Tile/Page Builder/Availability

---

## نحوه بستن هر Gap

برای هر ID:

1. Owner مشخص شود
2. لینک صفحه Confluence خروجی گذاشته شود
3. Reviewer (QA Lead) Approve کند
4. وضعیت `Done` شود
5. در Changelog انبوردینگ ثبت شود

### قالب آپدیت

```text
G-XX | Done
Owner: ...
Link: ...
Reviewed by: ...
Date: ...
Notes: ...
```
