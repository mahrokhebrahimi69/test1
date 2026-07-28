# چک‌لیست کمبودها (Gaps) — چه چیزهایی کم/ناقص است؟

> وضعیت‌ها: `Open` / `In Progress` / `Done` / `Blocked`  
> آپدیت: پس از مشاهده برد Jira و گروه GitLab Platform

---

## اولویت بحرانی (بلاکر انبوردینگ)

| ID | کمبود | چرا مهم است | Owner پیشنهادی | وضعیت |
| --- | --- | --- | --- | --- |
| G-01 | دامنه دقیق **TACH (TapsiChef)** vs **CHEF** | نام اصلاح شد، ولی مرز مسئولیت هنوز مبهم است | Senior QA + Chef | Open |
| G-02 | مرز **COMP (Basket)** vs **SD** vs **PROMC** | سبد/کشف/پروموشن نباید قاطی شوند | Senior QA + مربوطه | Open |
| G-03 | شناسنامه سرویس‌های Platform تازه‌کشف‌شده | Atlas / BiFrost / Chronos / Melia / Saga / Iris-* | Platform + Senior QA | Open |
| G-04 | اکانت‌های تست استاندارد نداریم | نیروی جدید عملاً نمی‌تواند Smoke بزند | Senior QA | Open |
| G-05 | ماتریس دسترسی لینک‌ها ناقص است | لینک‌ها هست، ولی Granted/Blocked مشخص نیست | QA Lead + IT/Sec | Open |
| G-06 | State Machine سفارش (OMS405) مستند نشده | بدون آن E2E و تریاژ باگ ضعیف است | OMS + Senior QA | Open |
| G-07 | قوانین Availability بر اساس آدرس مکتوب نیست | بخش کلیدی SD بدون معیار تست است | Search & Discovery | Open |
| G-08 | کاتالوگ اجزای Page Builder ناقص است | Carousel/Tile گفته شد؛ بقیه اجزا و قوانین Publish نه | SD + Product | Open |
| G-34 | تأیید تناظر **Falafel ↔ Athona** | دو نام برای Rate & Review گیج‌کننده است | Platform + Senior QA | Open |
| G-35 | دامنه اسکواد **DATA** | در Jira هست؛ ماموریت مکتوب نیست | Senior QA + Data | Open |

### موارد بسته‌شده با شواهد اسکرین

| ID | نتیجه | وضعیت |
| --- | --- | --- |
| G-01-old (TPCH ناشناخته) | همان **TACH = TapsiChef** در Jira | Done |
| G-02-old (COIMP) | اسکواد سبد **COMP (Basket)** است؛ پروموشن **PROMC** | Done |
| G-03-old / G-20 (لیست Platform) | لیست اولیه از `git.tapsifood.cloud/ofd/platform` استخراج شد | Done — جزئیات هنوز Open در G-03 |

---

## کمبودهای دامنه اسکوادها

| ID | کمبود | جزئیات لازم | وضعیت |
| --- | --- | --- | --- |
| G-09 | AI | فلو Moderator، مدل‌ها، پنل، false positive/negative | Open |
| G-10 | CHEF | نقش‌ها، فلوهای عملیاتی، تفاوت با BO و TACH | Open |
| G-11 | DEL | وضعیت‌ها، Zap integration، لغو/تأخیر | Open |
| G-12 | FIN | درگاه‌ها per env، refund، reconciliation | Open |
| G-13 | MM | مدل داده منو، sync با Vendor/Discovery | Open |
| G-14 | VEN | نقش‌ها، فلو سفارش در پنل، محیط‌ها | Open |
| G-15 | SD | سرچ، availability، page builder | Open |
| G-36 | COMP | lifecycle سبد، انقضا، conflict قیمت/موجودی | Open |
| G-37 | PROMC | انواع پروموشن/کوپن و اعمال روی Basket | Open |

---

## کمبودهای Platform

| ID | کمبود | توضیح | وضعیت |
| --- | --- | --- | --- |
| G-16 | تأیید صحت مستندات با کد روز | Drift در Icarus/Yggdrasil/Artemis گزارش شده | Open |
| G-17 | محیط و Base URL واقعی Stage/Prod هر سرویس | در راهنماها localhost زیاد است | Open |
| G-18 | مجموعه Postman/Newman رسمی per service | QA-Scripts را هم بررسی کن | Open |
| G-19 | Owner on-call هر سرویس Platform | برای تریاژ | Open |
| G-38 | مرز Iris vs Iris-sms/call/gw/social | کلاینت به کدام ریپو/endpoint می‌زند؟ | Open |
| G-39 | Melia/Growthbook: راهنمای فلگ برای QA | چگونه تست با فلگ انجام شود | Open |
| G-40 | Atlas admin console: نقش‌ها و ریسک‌ها | عملیات حساس | Open |
| G-41 | BiFrost/Strapi: محتوای تحت مدیریت | ارتباط با SD | Open |
| G-42 | Chronos: ماموریت | الان ناشناخته | Open |
| G-43 | Saga: قوانین نمایش Survey | تداخل با Review؟ | Open |

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
| G-44 | توضیح ستون‌های برد Jira QA | Ready for QA / Developer Test / QA Rejected / … | Open |

---

## کمبودهای امنیتی/حریم خصوصی برای QA

| ID | کمبود | توضیح | وضعیت |
| --- | --- | --- | --- |
| G-31 | داده‌های حساس در لاگ | سیاست تیم؟ | Open |
| G-32 | دسترسی به control-plane/setup/migrate در Icarus | کنترل شبکه؟ | Open |
| G-33 | مدیریت شماره موبایل واقعی برای OTP | فرایند شماره تست | Open |

---

## چیزهایی که الان خوب است

- نام Swimlaneهای Jira مشخص شد
- لیست پروژه‌های Platform از Git مشخص شد
- مستندات عمیق Iris / Icarus / Artemis / Yggdrasil / Rate&Review
- تصویر اولیه Journey و واژه‌نامه
- فهرست اولیه لینک سامانه‌ها

---

## نحوه بستن هر Gap

```text
G-XX | Done
Owner: ...
Link: ...
Reviewed by: ...
Date: ...
Notes: ...
```
