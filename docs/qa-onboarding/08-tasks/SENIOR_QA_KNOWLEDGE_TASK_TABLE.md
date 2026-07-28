# تسک جمع‌آوری دانش انبوردینگ QA — نسخه جدولی

> این صفحه را به همکار قدیمی QA بده.  
> قانون: هر ردیف باید `Done` یا `N/A` شود. ردیف خالی = جا افتاده.

---

## شناسنامه تسک

| فیلد | مقدار |
| --- | --- |
| Title | `[QA Onboarding] جمع‌آوری و مستندسازی دانش اسکوادها و سامانه‌ها برای نیروهای جدید` |
| Assignee | همکار قدیمی QA |
| Reporter | QA Team Lead |
| Priority | High — بلاکر انبوردینگ |
| هدف | دانش شفاهی اسکوادها را در Confluence ساخت‌یافته کنیم تا نیروی جدید وابسته به حافظه افراد نباشد |
| DoD | ۱) همه ردیف‌های جداول پر یا N/A ۲) صفحات Confluence آپدیت ۳) Gaps با Owner/تاریخ ۴) Walkthrough ۳۰ دقیقه‌ای با Team Lead ۵) اکانت و لینک Stage تأیید شده |

---

## پیشرفت کلی اسکوادها (یک نگاه)

وضعیت هر اسکواد را اینجا به‌روز کن: `Not Started` / `In Progress` / `Done`

| # | کد | اسکواد | Owner جلسه | وضعیت قالب A | لینک صفحه Confluence | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | AI | AI |  |  |  | Not Started |
| 2 | CHEF | Chef |  |  |  | Not Started |
| 3 | COMP | Basket |  |  |  | Not Started |
| 4 | DATA | Data |  |  |  | Not Started |
| 5 | DEL | Delivery |  |  |  | Not Started |
| 6 | FIN | Fintech |  |  |  | Not Started |
| 7 | MM | Menu Management |  |  |  | Not Started |
| 8 | OMS405 | OMS |  |  |  | Not Started |
| 9 | PLAT | Platform |  |  |  | Not Started |
| 10 | PROMC | Promotion Center |  |  |  | Not Started |
| 11 | SD | Search & Discovery |  |  |  | Not Started |
| 12 | TACH | TapsiChef |  |  |  | Not Started |
| 13 | VEN | Vendor |  |  |  | Not Started |

---

## قالب اجباری A — برای هر اسکواد یک‌بار کپی کن

برای هر اسکواد، جدول زیر را در صفحه همان اسکواد پر کن.

### A — شناسنامه و دامنه

| کد آیتم | عنوان | مقدار | وضعیت |
| --- | --- | --- | --- |
| A1.1 | نام رسمی اسکواد |  |  |
| A1.2 | مخفف / نام جایگزین |  |  |
| A1.3 | ماموریت یک‌خطی |  |  |
| A1.4 | Owner محصول (PM/PO) |  |  |
| A1.5 | Owner فنی (EM/Tech Lead) |  |  |
| A1.6 | Owner QA |  |  |
| A1.7 | کانال ارتباطی |  |  |
| A1.8 | لینک برد Jira |  |  |
| A2.1 | User Journeyهای تحت مالکیت |  |  |
| A2.2 | خارج از دامنه |  |  |
| A2.3 | Upstream |  |  |
| A2.4 | Downstream |  |  |

### A — سیستم، محیط، تست، ریسک

| کد آیتم | عنوان | مقدار | وضعیت |
| --- | --- | --- | --- |
| A3.1 | لیست سرویس‌ها/اپ‌ها |  |  |
| A3.2 | ریپوی Git |  |  |
| A3.3 | زبان/فریم‌ورک |  |  |
| A3.4 | دیتابیس |  |  |
| A3.5 | صف/پیام (Kafka/RabbitMQ/…) |  |  |
| A3.6 | Swagger/OpenAPI |  |  |
| A3.7 | پنل ادمین |  |  |
| A4.1 | Base URLهای Dev/Stage/Prod |  |  |
| A4.2 | نحوه دریافت دسترسی |  |  |
| A4.3 | اکانت تست استاندارد |  |  |
| A4.4 | فیچرفلگ‌های مهم |  |  |
| A4.5 | تفاوت Stage با Prod |  |  |
| A5.1 | Smoke (حداکثر ۱۰) |  |  |
| A5.2 | Regression حیاتی |  |  |
| A5.3 | Negative/Edge |  |  |
| A5.4 | داده تست لازم |  |  |
| A5.5 | چک‌لیست قبل از ریلیز |  |  |
| A6.1 | ۳ باگ پرتکرار |  |  |
| A6.2 | ۳ نقطه شکست Prod |  |  |
| A6.3 | هشدار Observability |  |  |
| A6.4 | Runbook تریاژ |  |  |
| A7.1 | لینک مستندات موجود |  |  |
| A7.2 | نوت/ضبط جلسه دانش |  |  |
| A7.3 | وضعیت صفحه Draft/Ready |  |  |

---

## بخش B — چک‌لیست اختصاصی هر اسکواد

هر ردیف = یک خروجی لازم. ستون «جواب کوتاه» را پر کن.

### B1. AI

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | فلو Comment Moderation تا Approve/Reject |  |  |
| 2 | قوانین حساسیت محتوا |  |  |
| 3 | ارتباط با Athona (Rate & Review) |  |  |
| 4 | رفتار و کانال‌های Chatbot |  |  |
| 5 | نقش AI در Category و مرز با Yggdrasil |  |  |

### B2. CHEF

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | نقش‌های کاربری Chef |  |  |
| 2 | فلوهای روزانه عملیات |  |  |
| 3 | تفاوت Chef با BO و Vendor Panel |  |  |
| 4 | تفاوت/رابطه با TACH |  |  |
| 5 | دسترسی Dev/Stage/Prod |  |  |

### B3. COMP (Basket)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | افزودن/حذف/آپدیت آیتم سبد |  |  |
| 2 | انقضای سبد و conflict قیمت/موجودی |  |  |
| 3 | نقطه تحویل از SD به COMP |  |  |
| 4 | تعامل با PROMC هنگام کوپن |  |  |
| 5 | تبدیل سبد به سفارش (OMS) |  |  |

### B4. PROMC (Promotion Center)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | انواع پروموشن/کوپن |  |  |
| 2 | قوانین استک شدن تخفیف |  |  |
| 3 | محدودیت شهر/کاربر/وندور/زمان |  |  |
| 4 | مرز با کمپین نمایشی SD |  |  |
| 5 | اثر روی Basket و Payment |  |  |

### B5. DEL (Delivery)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | State machine ارسال |  |  |
| 2 | تفاوت Own / Zap / Pickup |  |  |
| 3 | لغو، تأخیر، برگشت پیک |  |  |
| 4 | وابستگی به OMS و Iris |  |  |

### B6. FIN (Fintech)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | درگاه‌های فعال per env |  |  |
| 2 | فلو Success/Fail/Timeout |  |  |
| 3 | Refund و Recheck پرداخت |  |  |
| 4 | صحت مستند GetRefundAndPaymentStatusForOrder |  |  |

### B7. MM (Menu Management)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | موجودیت‌های منو |  |  |
| 2 | sync با Vendor و Discovery |  |  |
| 3 | اثر تغییر قیمت/موجودی روی سبد باز |  |  |

### B8. OMS405

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | وضعیت‌های سفارش |  |  |
| 2 | Eventهای بین‌سیستمی |  |  |
| 3 | کاربرد پنل order.tapsi.food |  |  |
| 4 | معنی کد 405 در نام برد |  |  |
| 5 | سناریو لغو/شکست پرداخت/ارسال |  |  |

### B9. PLAT (Platform)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | تأیید لیست Git: Artemis, Athona, Atlas, BiFrost, Chronos, Icarus, Iris*, Melia, QA-Scripts, Saga, Yggdrasil |  |  |
| 2 | Owner هر سرویس |  |  |
| 3 | ماتریس وابستگی |  |  |
| 4 | تأیید Falafel docs = Athona؟ |  |  |
| 5 | مستند حداقلی Atlas/BiFrost/Chronos/Melia/Saga/Iris-* |  |  |

### B10. SD (Search & Discovery)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | فلو سرچ |  |  |
| 2 | قوانین Availability بر اساس آدرس |  |  |
| 3 | اجزای Page Builder (Carousel/Tile/Banner/…) |  |  |
| 4 | Publish per city |  |  |
| 5 | مرز دقیق با COMP |  |  |

### B11. VEN (Vendor)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | نقش‌ها و دسترسی‌ها |  |  |
| 2 | فلو دریافت/مدیریت سفارش |  |  |
| 3 | مدیریت منو از پنل |  |  |
| 4 | تفاوت bo-ui-dev / bo-ui / bo.tapsi.food |  |  |

### B12. TACH (TapsiChef)

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | ماموریت دقیق TapsiChef |  |  |
| 2 | Owner |  |  |
| 3 | تفاوت با CHEF |  |  |
| 4 | لینک‌ها و ریپوها |  |  |
| 5 | سناریوهای QA |  |  |

### B13. DATA

| # | باید مشخص شود | جواب کوتاه | وضعیت |
| --- | --- | --- | --- |
| 1 | ماموریت اسکواد Data |  |  |
| 2 | ابزارها و دشبوردها |  |  |
| 3 | آنچه QA باید بداند |  |  |

---

## بخش C — کارهای افقی (Cross-cutting)

| کد | عنوان تسک | خروجی لازم | Owner | وضعیت |
| --- | --- | --- | --- | --- |
| C1 | Standard Test Accounts & Access Matrix | جدول اکانت + ماتریس دسترسی + Owner تمدید |  |  |
| C2 | Complete Product Glossary | اصطلاحات UI + اسکرین نمونه + تأیید Product |  |  |
| C3 | E2E Order Happy Path | زنجیره کامل زیر + معیار پاس هر گام |  |  |
| C4 | Debug with Kibana/Metabase/CD | کوئری آماده + روش TraceId + خواندن نسخه CD |  |  |
| C5 | Validate All System Links | دسته‌بندی لینک‌ها + Env + Owner + وضعیت سلامت |  |  |

### خروجی اجباری C3

```text
Login(Icarus) → Profile/Address(Artemis) → Discovery/Availability(SD)
→ Menu(MM) → Cart(COMP) → Coupon(PROMC) → Pay(FIN)
→ OMS405 → Delivery(DEL: Own/Zap) → Notif(Iris) → Review(Athona)
```

| گام | سرویس | پنل | داده تست | معیار پاس | وضعیت |
| --- | --- | --- | --- | --- | --- |
| Login | Icarus |  |  |  |  |
| Profile/Address | Artemis |  |  |  |  |
| Discover | SD |  |  |  |  |
| Menu | MM |  |  |  |  |
| Cart | COMP |  |  |  |  |
| Coupon | PROMC |  |  |  |  |
| Pay | FIN |  |  |  |  |
| Order | OMS405 |  |  |  |  |
| Delivery | DEL |  |  |  |  |
| Notif | Iris |  |  |  |  |
| Review | Athona |  |  |  |  |

---

## ترتیب اجرا (که قاطی نشود)

| مرحله | کار | وابسته به | وضعیت |
| --- | --- | --- | --- |
| 1 | C5 لینک‌ها | - |  |
| 2 | C1 اکانت‌ها و دسترسی | C5 |  |
| 3 | B12 TACH vs CHEF | جلسه Chef |  |
| 4 | B3 + B4 + B10 مرز COMP/PROMC/SD | جلسه SD/Promo/Basket |  |
| 5 | B9 Platform کامل | Git group |  |
| 6 | باقی اسکوادها (AI, DEL, FIN, MM, OMS, VEN, DATA) | جلسات ۳۰ دقیقه‌ای |  |
| 7 | C2 واژه‌نامه + C3 E2E + C4 Observability | بعد از Bها |  |
| 8 | آپدیت Gaps + Walkthrough با Team Lead | همه موارد بالا |  |

---

## پیام اساین (کپی برای Jira/Mattermost)

```text
عنوان: [QA Onboarding] جمع‌آوری دانش اسکوادها برای نیروهای جدید

سلام،
برای انبوردینگ نیروهای جدید QA باید دانش اسکوادها از حالت شفاهی خارج و در Confluence جدولی شود.

لطفاً صفحه «تسک جمع‌آوری دانش — نسخه جدولی» را باز کن و:
1) جدول پیشرفت کلی اسکوادها را جلو ببر
2) برای هر اسکواد قالب A را پر کن
3) چک‌لیست B همان اسکواد را بدون ردیف خالی ببند
4) کارهای C1 تا C5 را طبق ترتیب اجرا تکمیل کن

قانون: هر ردیف یا Done است یا N/A. ردیف خالی یعنی کار جا افتاده.
```
