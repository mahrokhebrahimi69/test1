# سرویس‌های Platform

تیم Platform زیرساخت مشترک را نگه می‌دارد. چند سرویس کلیدی با نام‌های اساطیری/پروژه‌ای:

| سرویس | نقش ساده | تکنولوژی (خلاصه) |
| --- | --- | --- |
| Iris | مرکز ارسال نوتیفیکیشن | SMS / Call / Telegram + RabbitMQ |
| Icarus | لاگین و هویت | Go + Keycloak + Redis + Iris |
| Artemis | پروفایل کاربر | .NET + SQL Server |
| Yggdrasil | دسته‌بندی و تگ | .NET 8 + MySQL + RabbitMQ |
| Falafel | ریویو و ریتینگ | NestJS + MySQL + Redis + RabbitMQ |

> راهنماهای کامل Flow هر سرویس در ریپو/مستندات جدا موجود است. این صفحه نسخه خلاصه برای انبوردینگ است.

---

## Iris — Notification Service

### یک جمله‌ای
دفتر پست مرکزی نوتیفیکیشن: بقیه سیستم‌ها به Iris می‌گویند پیام بفرست؛ Iris از طریق Provider ارسال می‌کند.

### کانال‌ها
- `sms`
- `call`
- `telegram` (OTP عددی)

### مفاهیم کلیدی
| مفهوم | معنی |
| --- | --- |
| Master API Key | کلید ادمین برای ساخت Profile/Line/Pattern |
| Profile Generated Key | کلید هر سرویس کلاینت برای ارسال نوتیف |
| Line | شماره فرستنده SMS |
| Provider | شرکت ارسال‌کننده (FAVA, PISHGAMAN, KAVENEGAR, MEDIANA) |
| Pattern | قالب/تمپلیت Provider |
| ULID | شناسه پیگیری هر گیرنده |

### فلو ساده
1. ادمین Line/Pattern/Profile می‌سازد
2. Iris کلید Profile می‌دهد
3. کلاینت با آن کلید `POST /api/v1/notifications/send` می‌زند
4. کار وارد RabbitMQ می‌شود
5. Consumer ارسال می‌کند
6. کلاینت با ULID وضعیت را می‌پرسد

### نکات QA مهم
- در development، master key ممکن است چک نشود
- Telegram فقط ۱ گیرنده و پیام ۴ تا ۸ رقم
- Call حداکثر ۳۰۰ کاراکتر
- SMS تا ۵۰ گیرنده (با محدودیت template)
- Fallback روی Line/Provider بعدی

### Endpoints کلیدی
- `POST /api/v1/notifications/send`
- `GET /api/v1/notifications/sms/:ulid`
- `GET /api/health/liveness|readiness`

---

## Icarus — Authentication

### یک جمله‌ای
میز امنیت ساختمان: OTP، لاگین تپسی، توکن، رفرش، لاگ‌اوت.

### فلو اصلی OTP
```text
Phone → OTP SMS (Iris) → Verify → Cookie/Profile user → Keycloak tokens → Cookies
```

### فلو تپسی SSO
```text
Tapsi code → Tapsi profile → Cookie user → Keycloak tokens
```

### Endpoints کلیدی
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/verify`
- `POST /api/v1/auth/tapsi-login`
- `GET /api/v1/auth/validate-token`
- `POST /api/v1/auth/refresh-token`
- `POST /api/v1/auth/logout`

### نکات QA مهم
- توکن‌ها عمدتاً از Cookie خوانده می‌شوند (نه فقط Bearer)
- OTP TTL پیش‌فرض حدود ۱۲۰ ثانیه
- ریسک‌های شناخته‌شده: ناسازگاری طول OTP، مسیرهای control-plane/setup/migrate بدون middleware واضح
- وابستگی‌ها: Redis, Keycloak, Iris, Cookie service, Tapsi account

---

## Artemis — User Profile

### یک جمله‌ای
دفترچه پروفایل کاربر: موبایل، نام، کد ملی، تاریخ تولد، آدرس‌ها، Type و Status.

### موجودیت‌ها
- Profile
- Address
- Profile Type
- Profile Status
- User Identity (در دامنه هست؛ API عمومی فعلاً محدود/ندارد)

### نکته مهم
`userId` در پاسخ‌ها encode شده است؛ تست‌ها باید با ID انکدشده کار کنند.

### Happy path تست
1. Create Profile Type / Status
2. Create Profile
3. Update Profile
4. Add/Update/Delete Address
5. Attach/Detach Type & Status

---

## Yggdrasil — Category & Tag Catalog

### یک جمله‌ای
موتور سازمان‌دهی کاتالوگ: Category درختی + Tag + Association به Product/Vendor/User/Ticket.

### مفاهیم
| مفهوم | معنی |
| --- | --- |
| Category | پوشه درختی |
| Tag | برچسب/بج |
| Association | لینک آیتم به دسته/تگ |
| Product Type | User / Product / Vendor / Ticket |
| Task | کار بک‌گراند (مثلاً حذف Category) |
| staff-id | هدر ممیزی برای Write APIها |

### نکات QA
- Auth واقعی روی خیلی از APIها نیست؛ `staff-id` برای audit است
- حذف Category async است
- مستندات قدیمی ممکن است با Controller فعلی فرق داشته باشد → Swagger/کد منبع حقیقت است

---

## Falafel — Review & Rating

### یک جمله‌ای
مغز امتیاز و نظر: مشتری می‌نویسد، Support مودریت می‌کند، Vendor جواب می‌دهد، Public نسخه امن را می‌بیند، ریتینگ آپدیت می‌شود.

### دسته‌بندی ریویو
- ORDER
- PRODUCT
- DELIVERY

### وضعیت‌ها
- PENDING
- APPROVED
- DISAPPROVED

### نکات QA بحرانی
- کامنت Pending/Rejected نباید اشتباهاً Public شود
- Mask کردن نام مشتری
- Duplicate review نباید ریتینگ را باد کند
- Publish به RabbitMQ روی تغییر ریتینگ
- Insight وندور با OpenAI (نباید کل Stats را بشکند)

---

## وابستگی بین سرویس‌ها (برای دیباگ E2E)

```text
Icarus --OTP SMS--> Iris
Icarus --create/find user--> Cookie/Profile (Artemis سمت پروفایل)
App --address/profile--> Artemis
Discovery --categories/tags--> Yggdrasil
Order complete --reviews--> Falafel
Falafel --rating updated--> سایر سیستم‌ها (RabbitMQ)
هر سرویس --notif--> Iris
```

---

## لینک مشاهده‌پذیری مرتبط

- Kibana/APM سرویس‌ها (نمونه Icarus): `https://kibana.tapsifood.cloud/...`
- Kibana Stage: `https://kibana.foodstg.com/login?next=%2F`
- Keycloak Stage Admin: `https://kc.foodstg.com/...`
