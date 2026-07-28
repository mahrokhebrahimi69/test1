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
- [ ] فلو Comment Moderation از ورود کامنت تا Approve/Reject
- [ ] قوانین حساسیت محتوا
- [ ] ارتباط با Athona (Rate & Review)
- [ ] رفتار Chatbot و کانال‌های آن
- [ ] نقش AI در Category و مرز با Yggdrasil

## B2. CHEF
```text
[QA Knowledge] CHEF — Staff Ops Panel & Restaurant Relations
```
- [ ] نقش‌های کاربری Chef
- [ ] فلوهای روزانه عملیات
- [ ] تفاوت Chef با BO و Vendor Panel
- [ ] تفاوت/رابطه با TACH (TapsiChef)
- [ ] دسترسی Dev/Stage/Prod

## B3. COMP (Basket)
```text
[QA Knowledge] COMP — Basket Lifecycle
```
- [ ] افزودن/حذف/آپدیت آیتم در سبد
- [ ] انقضای سبد و conflict قیمت/موجودی
- [ ] نقطه تحویل از SD به COMP
- [ ] تعامل با PROMC هنگام اعمال کوپن
- [ ] تبدیل سبد به سفارش (OMS)

## B4. PROMC (Promotion Center)
```text
[QA Knowledge] PROMC — Promotions & Coupons
```
- [ ] انواع پروموشن و کوپن
- [ ] قوانین استک شدن تخفیف‌ها
- [ ] محدودیت شهر/کاربر/وندور/زمان
- [ ] مرز با کمپین نمایشی SD/Page Builder
- [ ] اثر روی Basket و Payment

## B5. DEL (Delivery)
```text
[QA Knowledge] DEL — Own Delivery vs Zap
```
- [ ] State machine ارسال
- [ ] تفاوت Own / Zap / Pickup
- [ ] لغو، تأخیر، برگشت پیک
- [ ] وابستگی به OMS و نوتیفیکیشن

## B6. FIN (Fintech)
```text
[QA Knowledge] FIN — Payment Gateways & Refund
```
- [ ] درگاه‌های فعال per env
- [ ] فلو Success/Fail/Timeout
- [ ] Refund و Recheck وضعیت پرداخت
- [ ] لینک مستند GetRefundAndPaymentStatusForOrder و صحت آن

## B7. MM (Menu Management)
```text
[QA Knowledge] MM — Catalog & Item Availability
```
- [ ] موجودیت‌های منو
- [ ] همگام‌سازی با Vendor و Discovery
- [ ] اثر تغییر قیمت/موجودی روی سبد باز (COMP)

## B8. OMS405
```text
[QA Knowledge] OMS405 — Order Lifecycle
```
- [ ] وضعیت‌های سفارش از ایجاد تا تکمیل
- [ ] Eventهای بین‌سیستمی
- [ ] پنل order.tapsi.food و کاربرد هر بخش
- [ ] معنی کد/پسوند 405 در نام برد
- [ ] سناریوهای لغو/شکست پرداخت/شکست ارسال

## B9. PLAT (Platform)
```text
[QA Knowledge] PLAT — Shared Services Map (git.tapsifood.cloud/ofd/platform)
```
- [ ] تأیید لیست Git: Artemis, Athona, Atlas, BiFrost, Chronos, Icarus, Iris*, Melia, QA-Scripts, Saga, Yggdrasil
- [ ] Owner هر سرویس
- [ ] ماتریس وابستگی
- [ ] تأیید تناظر Falafel docs ↔ Athona
- [ ] مستند حداقلی برای Atlas / BiFrost / Chronos / Melia / Saga / Iris-*

## B10. SD (Search & Discovery)
```text
[QA Knowledge] SD — Search, Availability, Page Builder
```
- [ ] فلو سرچ
- [ ] قوانین Availability بر اساس آدرس
- [ ] اجزای Page Builder: Carousel / Tile / Banner / ...
- [ ] Publish per city
- [ ] مرز دقیق با COMP (Basket)

## B11. VEN (Vendor)
```text
[QA Knowledge] VEN — Restaurant Panel
```
- [ ] نقش‌ها و دسترسی‌ها
- [ ] فلو دریافت و مدیریت سفارش
- [ ] مدیریت منو از پنل
- [ ] تفاوت bo-ui-dev / bo-ui / bo.tapsi.food

## B12. TACH (TapsiChef)
```text
[QA Knowledge] TACH — TapsiChef Scope vs CHEF
```
- [ ] ماموریت دقیق TapsiChef
- [ ] Owner
- [ ] تفاوت با CHEF
- [ ] لینک‌ها و ریپوها
- [ ] سناریوهای QA

## B13. DATA
```text
[QA Knowledge] DATA — Squad Scope for QA
```
- [ ] ماموریت اسکواد Data
- [ ] ابزارها و دشبوردها
- [ ] چه چیزهایی را QA باید بلد باشد

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
Login(Icarus) → Profile/Address(Artemis) → Discovery/Availability(SD)
→ Menu(MM) → Cart(COMP) → Coupon(PROMC) → Pay(FIN)
→ OMS405 → Delivery(DEL: Own/Zap) → Notif(Iris) → Review(Athona)
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
2. B12 (TACH vs CHEF) و B3/B4/B10 (COMP vs PROMC vs SD) را زود روشن کن.
3. B9 Platform را با لیست Git تکمیل و نام Athona/Falafel را یکدست کن.
4. برای هر اسکواد یک جلسه ۳۰ دقیقه‌ای با Tech Lead/QA همان اسکواد بگذار.
5. همزمان قالب بخش A را در Confluence پر کن.
6. روزانه وضعیت را در صفحه Gaps آپدیت کن.
7. در پایان، با Team Lead Walkthrough انجام بده.

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
