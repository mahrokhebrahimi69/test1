# نقشه اسکوادهای تپسی‌فود

> منبع نام‌گذاری: برد Jira (`desktapsifood.atlassian.net`) + توضیح تیم  
> هر اسکواد مالک بخشی از محصول است و معمولاً با فناوری/زبان جداگانه کار می‌کند.

---

## جدول خلاصه اسکوادها (مطابق Swimlaneهای Jira)

| کد Jira | نام | مسئولیت اصلی | وضعیت دانش |
| --- | --- | --- | --- |
| AI | AI | Comment Moderator، Chatbot، Category-related AI | جزئی |
| CHEF | Chef | آفیس همکاران ستادی + ارتباط با رستوران‌ها | جزئی |
| COMP | COMP (Basket) | سبد خرید (Basket) | جزئی — قبلاً اشتباه با پروموشن قاطی شده بود |
| DATA | Data | داده / تحلیل / نیازهای دیتایی اسکواد | جزئی |
| DEL | Delivery | ارسال سفارش (رستوران یا زپ) | جزئی |
| FIN | Fintech / Finance | مالی و درگاه‌های پرداخت | جزئی |
| MM | Menu Management | مدیریت منو | جزئی |
| OMS405 | OMS | Order Management System | جزئی |
| PLAT | Platform | زیرساخت مشترک همه تیم‌ها | خوب‌تر (لیست Git مشخص شد) |
| PROMC | Promotion Center | پروموشن‌ها و کوپن‌ها | جزئی |
| SD | Search & Discovery | سرچ، دیسکاوری، Availability، Page Builder | جزئی |
| TACH | TapsiChef | مرتبط با اکوسیستم Chef / TapsiChef | جزئی — قبلاً به‌اشتباه TPCH خوانده می‌شد |
| VEN | Vendor | رستوران‌ها و پنل وندور | جزئی |

> نکته اصلاحی: مخفف **COIMP** در دانش اولیه اشتباه بود. در Jira اسکواد سبد **COMP (Basket)** است و پروموشن‌ها زیر **PROMC (Promotion Center)**.

---

## AI

### چه کاری می‌کند؟
- **Comment Moderator**: بررسی/فیلتر کامنت‌ها
- **Chatbot**: پاسخ‌گویی خودکار
- **Category**: کمک/اتوماسیون مرتبط با دسته‌بندی

### چیزهایی که Senior QA باید تکمیل کند
- Owner فنی و QA
- لیست سرویس‌ها و ریپوها
- محیط‌ها و لینک Swagger/Admin
- سناریوهای بحرانی مودریشن
- وابستگی به Athona (Rate & Review) / Yggdrasil

---

## CHEF

### چه کاری می‌کند؟
آفیس داخلی همکاران ستادی سازمان است و با رستوران‌ها ارتباط دارد.

### لینک‌های شناخته‌شده
- `https://chef.tapsi.food/login/cellphone`
- `https://chef.foodstg.com/login/cellphone`
- `https://chef-dev.foodstg.com/login/cellphone`

### چیزهایی که باید تکمیل شود
- نقش‌های کاربری داخل Chef
- فلوهای اصلی عملیات
- تفاوت Chef با Backoffice (BO)
- تفاوت/رابطه با اسکواد **TACH (TapsiChef)**
- دسترسی‌های لازم برای QA

---

## COMP — Basket

### چه کاری می‌کند؟
مالک **سبد خرید (Basket)** است.

### نکته مهم برای QA
- افزودن به سبد / تغییر تعداد / حذف آیتم / اعتبارسنجی سبد قبل از سفارش اینجا متمرکز است.
- هم‌پوشانی احتمالی با SD (تا لحظه افزودن به سبد) باید دقیق مرزبندی شود.

### چیزهایی که باید تکمیل شود
- APIها و State سبد
- انقضای سبد / تغییر قیمت/موجودی وسط کار
- تعامل با PROMC هنگام اعمال کوپن روی سبد
- تعامل با OMS هنگام تبدیل سبد به سفارش

---

## DATA

### چه کاری می‌کند؟
اسکواد داده (در Jira با کد DATA). دامنه دقیق باید تکمیل شود: احتمالاً پایپلاین دیتا، متریک، یا ابزارهای داده محصول.

### چیزهایی که باید تکمیل شود
- ماموریت دقیق
- ابزارها (Metabase؟ دیتابیس‌ها؟)
- چه چیزهایی را QA این اسکواد باید بداند vs فقط مصرف‌کننده باشد

---

## DEL — Delivery

### چه کاری می‌کند؟
ارسال سفارش. دو مدل اصلی:

1. **ارسال توسط رستوران** (Own Delivery)
2. **ارسال توسط تپسی‌فود** از طریق شرکت تابعه **زپ (Zap)**

مدل سوم: **Pickup**

### چیزهایی که باید تکمیل شود
- وضعیت‌های سفارش در مسیر ارسال
- SLA و تایم‌اوت‌ها
- ریتری/لغو/مرجوعی مرتبط با دلیوری
- ابزار مانیتورینگ Dedicated دلیوری

---

## FIN — Fintech / Finance

### چه کاری می‌کند؟
مالی و درگاه‌های پرداخت (Fintech).

### چیزهایی که باید تکمیل شود
- درگاه‌های فعال در Stage/Prod
- فلو موفقیت / شکست / برگشت وجه (Refund)
- وابستگی به OMS
- سندهای موجود مثل GetRefundAndPaymentStatusForOrder

---

## MM — Menu Management

### چه کاری می‌کند؟
مدیریت منوی رستوران‌ها.

### چیزهایی که باید تکمیل شود
- موجودیت‌های منو
- هم‌گام‌سازی با Vendor Panel و Discovery
- اثر تغییر منو روی سبد باز (COMP) و سفارش جاری (OMS)

---

## OMS405 — Order Management System

### چه کاری می‌کند؟
مدیریت چرخه عمر سفارش از ثبت تا اتمام/لغو.

### لینک‌های شناخته‌شده
- `https://order.tapsi.food/dashboard`

### چیزهایی که باید تکمیل شود
- State Machine سفارش
- Eventهای بین OMS و Delivery / Finance / Iris
- معنی پسوند/کد `405` در نام برد (اگر معنادار است)

---

## PLAT — Platform

### چه کاری می‌کند؟
زیرساخت و سرویس‌های مشترک همه تیم‌ها.

گروه GitLab: `git.tapsifood.cloud/ofd/platform`

لیست پروژه‌های دیده‌شده:

| پروژه | نقش |
| --- | --- |
| Artemis | User Profile |
| Athona | Rate And Review |
| Atlas | Platform Admin Console |
| BiFrost | Strapi |
| Chronos | TBD |
| Icarus | SSO |
| Iris | Centralized notification service |
| Iris-call / Iris-gw / Iris-sms / Iris-social | زیرسرویس‌های Iris |
| Melia | Growthbook |
| QA-Scripts | اسکریپت‌های QA |
| Saga | In-app survey |
| Yggdrasil | Tag and Category Management |

جزئیات: صفحه **سرویس‌های Platform**

---

## PROMC — Promotion Center

### چه کاری می‌کند؟
پروموشن‌ها و کوپن‌ها (Promotion Center).

### چیزهایی که باید تکمیل شود
- انواع پروموشن
- قوانین اعمال کوپن روی سبد (COMP)
- محدودیت کاربر/شهر/رستوران/زمان
- مرز با کمپین‌های نمایشی در SD/Page Builder

---

## SD — Search & Discovery

### چه کاری می‌کند؟
کارهای کشف و پیش از سفارش:

1. سرچ و کشف رستوران/غذا
2. **Availability**: بر اساس آدرس، چه رستوران/غذایی نشان داده شود
3. **Page Builder**: ساخت هوم‌پیج‌های متفاوت برای شهرهای مختلف

### نکته مرز با COMP
SD تا مسیر کشف و انتخاب جلو می‌آید؛ مالک سبد در Jira اسکواد **COMP** است. Senior QA باید نقطه تحویل دقیق را مشخص کند.

### چیزهایی که باید تکمیل شود
- اجزای UI: Carousel / Tile / Banner / …
- قوانین Availability
- فلو Page Builder از ساخت تا Publish
- اثر تغییر آدرس روی نتایج

---

## TACH — TapsiChef

### چه کاری می‌کند؟
اسکواد **TapsiChef** (در دانش اولیه به‌اشتباه TPCH خوانده می‌شد).

### چیزهایی که باید تکمیل شود
- تفاوت TACH با CHEF
- دامنه محصول/پنل
- Owner و ریپوها
- سناریوهای QA اختصاصی

---

## VEN — Vendor

### چه کاری می‌کند؟
رستوران‌ها و پنلی که در اختیار آن‌هاست.

### لینک‌های شناخته‌شده
- `https://bo.tapsi.food/vendor/2696km/management`
- `https://bo-ui.foodstg.com/vendor`
- `https://bo-ui-dev.foodstg.com/`
- `https://bo-ui.foodstg.com/`

### چیزهایی که باید تکمیل شود
- نقش‌های وندور
- فلو پذیرش/رد سفارش
- مدیریت منو از پنل وندور
- تفاوت BO و Vendor Panel
