# تسک: جمع‌آوری دانش انبوردینگ QA از تیم‌ها

## Title پیشنهادی برای Jira/Task Tracker

```text
[QA Onboarding] جمع‌آوری و مستندسازی دانش اسکوادها و سامانه‌ها برای نیروهای جدید
```

## Assignee
همکار قدیمی QA (Previous/Senior QA)

## Reporter / Requester
QA Team Lead

## هدف
چون Team Lead و بخشی از تیم هم نیوجوینر هستند، باید دانش پراکنده افراد قدیمی و اسکوادها را در Confluence یکجا و قابل‌استفاده کنیم تا انبوردینگ نیروهای جدید وابسته به حافظه افراد نباشد.

## خروجی نهایی (Definition of Done)
- [ ] همه عنوان‌های این تسک برای هر اسکواد پر شده یا صریحاً `N/A` خورده
- [ ] صفحات Confluence مربوطه آپدیت شده
- [ ] صفحه Gaps به‌روز شده (موارد باز با Owner و تاریخ)
- [ ] یک جلسه Walkthrough ۳۰ دقیقه‌ای برای Team Lead برگزار شده
- [ ] اکانت‌ها و لینک‌های حیاتی Stage تأیید شده‌اند

## اولویت
High — بلاکر انبوردینگ نیروهای جدید

## ETA پیشنهادی داخلی
تا قبل از ورود موج نیروهای جدید؛ پیشرفت روزانه در صفحه Gaps ثبت شود.

---

# بخش A — قالب اجباری برای هر اسکواد

برای **هر اسکواد** یک صفحه/سکشن با عنوان‌های زیر بساز و بدون جا انداختن پر کن.

## A1. شناسنامه اسکواد
- [ ] `نام رسمی اسکواد`
- [ ] `مخفف‌ها و نام‌های جایگزین`
- [ ] `ماموریت یک‌خطی`
- [ ] `Owner محصول (PM/PO)`
- [ ] `Owner فنی (EM/Tech Lead)`
- [ ] `Owner QA`
- [ ] `کانال ارتباطی (Slack/Teams)`
- [ ] `لینک برد Jira/YouTrack`

## A2. دامنه محصول
- [ ] `چه User Journeyهایی Owner این اسکواد است؟`
- [ ] `چه چیزهایی صریحاً خارج از دامنه است؟`
- [ ] `وابستگی بالادستی (Upstream)`
- [ ] `وابستگی پایین‌دستی (Downstream)`

## A3. سیستم‌ها و ریپوها
- [ ] `لیست سرویس‌ها/اپ‌ها`
- [ ] `ریپوی Git هر سرویس`
- [ ] `زبان و فریم‌ورک`
- [ ] `دیتابیس‌ها`
- [ ] `صف/پیام (Kafka/RabbitMQ/…)`
- [ ] `لینک Swagger/OpenAPI`
- [ ] `لینک پنل ادمین`

## A4. محیط‌ها و دسترسی
- [ ] `Base URLهای Dev/Stage/Prod`
- [ ] `نحوه دریافت دسترسی`
- [ ] `اکانت تست استاندارد`
- [ ] `فیچرفلگ‌های مهم`
- [ ] `تفاوت رفتار Stage با Prod`

## A5. سناریوهای QA
- [ ] `Smoke (حداکثر ۱۰ مورد)`
- [ ] `Regression حیاتی`
- [ ] `Negative/Edge`
- [ ] `داده‌های تست لازم (رستوران، کاربر، کوپن، …)`
- [ ] `چک‌لیست قبل از ریلیز`

## A6. باگ‌ها و ریسک‌ها
- [ ] `۳ باگ پرتکرار تاریخی`
- [ ] `۳ نقطه شکست رایج در Prod`
- [ ] `هشدارهای Observability مهم`
- [ ] `Runbook تریاژ اولیه`

## A7. تحویل دانش
- [ ] `لینک مستندات موجود`
- [ ] `ضبط/نوت جلسه دانش`
- [ ] `وضعیت صفحه: Draft / Ready`

---

# بخش B — تسک‌های جداگانه به تفکیک اسکواد (عنوان آماده)

این عنوان‌ها را عیناً در Task Tracker بساز (Sub-task یا چک‌لیست).

## B1. AI
```text
[QA Knowledge] AI — Moderator / Chatbot / Category
```
باید مشخص شود:
- [ ] فلو Comment Moderation از ورود کامنت تا Approve/Reject
- [ ] قوانین حساسیت محتوا
- [ ] ارتباط با Falafel
- [ ] رفتار Chatbot و کانال‌های آن
- [ ] نقش AI در Category و مرز با Yggdrasil

## B2. Chef
```text
[QA Knowledge] Chef — Staff Ops Panel & Restaurant Relations
```
- [ ] نقش‌های کاربری Chef
- [ ] فلوهای روزانه عملیات
- [ ] تفاوت Chef با BO و Vendor Panel
- [ ] دسترسی Dev/Stage/Prod

## B3. COIMP
```text
[QA Knowledge] COIMP — Promotions Engine
```
- [ ] انواع پروموشن
- [ ] قوانین استک شدن تخفیف‌ها
- [ ] محدودیت شهر/کاربر/وندور/زمان
- [ ] اثر روی سبد و پرداخت

## B4. PROMC
```text
[QA Knowledge] PROMC — Coupons Scope & Boundary vs COIMP
```
- [ ] دامنه دقیق PROMC
- [ ] تفاوت/هم‌پوشانی با COIMP
- [ ] Owner نهایی کوپن در هر فلو
- [ ] سناریوهای تست مشترک و جدا

## B5. Delivery
```text
[QA Knowledge] Delivery — Own Delivery vs Zap
```
- [ ] State machine ارسال
- [ ] تفاوت Own / Zap / Pickup
- [ ] لغو، تأخیر، برگشت پیک
- [ ] وابستگی به OMS و نوتیفیکیشن

## B6. Finance
```text
[QA Knowledge] Finance — Payment Gateways & Refund
```
- [ ] درگاه‌های فعال per env
- [ ] فلو Success/Fail/Timeout
- [ ] Refund و Recheck وضعیت پرداخت
- [ ] لینک مستند GetRefundAndPaymentStatusForOrder و صحت آن

## B7. Menu Management
```text
[QA Knowledge] Menu Management — Catalog & Availability of Items
```
- [ ] موجودیت‌های منو
- [ ] همگام‌سازی با Vendor و Discovery
- [ ] اثر تغییر قیمت/موجودی روی سبد باز

## B8. OMS
```text
[QA Knowledge] OMS — Order Lifecycle
```
- [ ] وضعیت‌های سفارش از ایجاد تا تکمیل
- [ ] Eventهای بین‌سیستمی
- [ ] پنل order.tapsi.food و کاربرد هر بخش
- [ ] سناریوهای لغو/شکست پرداخت/شکست ارسال

## B9. Platform
```text
[QA Knowledge] Platform — Shared Services Map (Greek/Norse services)
```
- [ ] لیست کامل سرویس‌های Platform از Git (فراتر از ۵ سرویس فعلی)
- [ ] Owner هر سرویس
- [ ] ماتریس وابستگی
- [ ] تأیید صحت مستندات Iris/Icarus/Artemis/Yggdrasil/Falafel
- [ ] سرویس‌های بدون مستند QA

## B10. Search & Discovery
```text
[QA Knowledge] Search & Discovery — Search, Cart pre-order, Availability, Page Builder
```
- [ ] فلو سرچ
- [ ] قوانین Availability بر اساس آدرس
- [ ] اجزای Page Builder: Carousel / Tile / Banner / ...
- [ ] Publish per city
- [ ] تست‌های رگرسیون هوم‌پیج

## B11. Vendor
```text
[QA Knowledge] Vendor — Restaurant Panel
```
- [ ] نقش‌ها و دسترسی‌ها
- [ ] فلو دریافت و مدیریت سفارش
- [ ] مدیریت منو از پنل
- [ ] تفاوت bo-ui-dev / bo-ui / bo.tapsi.food

## B12. TPCH
```text
[QA Knowledge] TPCH — Identify Scope (Unknown Squad)
```
- [ ] معنی مخفف
- [ ] Owner
- [ ] دامنه
- [ ] لینک‌ها و ریپوها
- [ ] اگر اسکواد منسوخ است، وضعیت Archive شود

---

# بخش C — تسک‌های افقی (Cross-cutting)

## C1. اکانت‌ها و دسترسی‌ها
```text
[QA Knowledge] Standard Test Accounts & Access Matrix
```
- [ ] جدول اکانت Customer/Vendor/Support/Chef/Finance
- [ ] ماتریس دسترسی لینک‌ها
- [ ] Owner تمدید دسترسی

## C2. واژه‌نامه محصول
```text
[QA Knowledge] Complete Product Glossary (Carousel, Tile, …)
```
- [ ] تکمیل اصطلاحات UI از Product/Design
- [ ] اسکرین شات نمونه برای هر مفهوم
- [ ] تأیید نهایی با Product

## C3. نقشه E2E
```text
[QA Knowledge] End-to-End Order Happy Path (with service chain)
```
خروجی:
```text
Login(Icarus) → Profile/Address(Artemis) → Discovery/Availability
→ Menu → Cart → Coupon(COIMP/PROMC) → Pay(Finance)
→ OMS → Delivery(Own/Zap) → Notif(Iris) → Review(Falafel)
```
برای هر گام: سرویس، پنل، داده تست، معیار پاس

## C4. Observability
```text
[QA Knowledge] How to Debug with Kibana / Metabase / CD
```
- [ ] کوئری‌های آماده Metabase برای سفارش/کاربر
- [ ] چطور TraceId را از کلاینت تا سرویس دنبال کنیم
- [ ] چطور نسخه دیپلوی‌شده را در CD ببینیم

## C5. مجموعه لینک‌ها
```text
[QA Knowledge] Curate and Validate All System Links
```
- [ ] همه لینک‌های داده‌شده باز و دسته‌بندی شوند
- [ ] لینک‌های منقضی/نیازمند لاگین مشخص شوند
- [ ] برای هر لینک Owner و Environment ثبت شود

---

# بخش D — روش اجرا (برای Assignee)

1. اول بخش C5 و C1 را ببند (دسترسی و لینک).
2. بعد B12 (TPCH) را روشن کن؛ اگر Unknown ماند در Gaps بماند.
3. برای هر اسکواد یک جلسه ۳۰ دقیقه‌ای با Tech Lead/QA همان اسکواد بگذار.
4. همزمان قالب بخش A را در Confluence پر کن.
5. روزانه وضعیت را در صفحه Gaps آپدیت کن.
6. در پایان، با Team Lead Walkthrough انجام بده.

---

# بخش E — پیام آماده برای اساین کردن

```text
عنوان: [QA Onboarding] جمع‌آوری دانش اسکوادها برای نیروهای جدید

سلام،
برای انبوردینگ نیروهای جدید QA لازم است دانش فعلی تیم‌ها را از حالت شفاهی خارج و در Confluence ساخت‌یافته کنیم.

لطفاً طبق چک‌لیست تسک، برای هر اسکواد شناسنامه، دامنه، لینک‌ها، سناریوهای Smoke، و ریسک‌ها را تکمیل کن.
خروجی باید طوری باشد که یک نیوجوینر بدون پرسیدن مکرر، تصویر درستی از تپسی‌فود و مرز اسکوادها بگیرد.

مرجع ساختار:
Confluence → QA Onboarding → تسک جمع‌آوری دانش
```
