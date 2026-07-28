# سرویس‌های Platform

منبع لیست پروژه‌ها: گروه GitLab  
`git.tapsifood.cloud/ofd/platform`

ماموریت گروه (از صفحه GitLab):

> We design, build, and maintain scalable platforms and services that power our SaaS offerings. Focus on flexibility, security, performance and enabling teams—without locking into a single technology stack.

---

## نقشه کامل پروژه‌های Platform

| پروژه | نقش رسمی در Git | وضعیت دانش QA |
| --- | --- | --- |
| Artemis | User Profile | خوب (Flow Guide موجود) |
| Athona | Rate And Review | خوب‌تر با راهنمای Falafel — باید نام‌گذاری یکسان شود |
| Atlas | Platform Admin Console | کم |
| BiFrost | Strapi | کم |
| Chronos | نامشخص در UI گروه | کم |
| Icarus | SSO | خوب (Flow Guide موجود) |
| Iris | Centralized notification service | خوب (Flow Guide موجود) |
| Iris-call | زیرسرویس تماس Iris | کم |
| Iris-gw | Gateway مرتبط با Iris | کم |
| Iris-sms | زیرسرویس SMS Iris | کم |
| Iris-social | زیرسرویس Social/Telegram؟ | کم |
| Melia | Growthbook | کم |
| QA-Scripts | اسکریپت‌های QA | جزئی |
| Saga | In-app survey | کم |
| Yggdrasil | Tag and Category Management Taxonomy | خوب (Flow Guide موجود) |

> نکته نام‌گذاری: راهنمای مفصل Rate & Review که در تیم با نام **Falafel** موجود است، احتمالاً متناظر با ریپوی **Athona** است. Senior QA باید این تناظر را تأیید و در مستندات یکدست کند.

---

## Artemis — User Profile

پروفایل کاربر: موبایل، نام، کد ملی، تاریخ تولد، آدرس‌ها، Type و Status.

نکته QA: `userId` در APIها encode می‌شود.

---

## Athona — Rate And Review

سرویس امتیاز و نظر (Rate & Review).

اگر راهنمای Falafel همان Athona باشد، فلوهای اصلی این‌هاست:
- مشتری ریویو می‌نویسد (ORDER / PRODUCT / DELIVERY)
- Support مودریت می‌کند (PENDING / APPROVED / DISAPPROVED)
- Vendor پاسخ می‌دهد
- Public فقط نسخه امن را می‌بیند
- ریتینگ آپدیت و روی RabbitMQ پابلیش می‌شود

---

## Atlas — Platform Admin Console

کنسول ادمین Platform. دامنه دقیق، نقش‌ها و صفحات باید تکمیل شود.

Checklist دانش:
- [ ] چه تیم‌هایی از Atlas استفاده می‌کنند؟
- [ ] چه عملیات حساسی دارد؟
- [ ] دسترسی Stage/Prod چطور گرفته می‌شود؟

---

## BiFrost — Strapi

احتمالاً CMS مبتنی بر Strapi برای محتوای قابل مدیریت.

Checklist دانش:
- [ ] چه محتوایی اینجا مدیریت می‌شود؟
- [ ] ارتباط با Page Builder / SD؟
- [ ] محیط‌ها و نقش‌های ادیتور

---

## Chronos

نقش در صفحه گروه Git مشخص نبود.

Checklist دانش:
- [ ] ماموریت یک‌خطی
- [ ] Owner
- [ ] وابستگی‌ها

---

## Icarus — SSO / Auth

احراز هویت و نشست:
- OTP SMS از طریق Iris
- Tapsi Super App login
- Validate / Refresh / Logout
- Keycloak + Redis + Cookie/Profile service

---

## Iris — Notification (+ زیرسرویس‌ها)

مرکز نوتیفیکیشن.

### خانواده Iris در Git
| ریپو | فرض اولیه |
| --- | --- |
| Iris | سرویس اصلی / orchestration |
| Iris-sms | مسیر SMS |
| Iris-call | مسیر تماس |
| Iris-social | مسیر social/telegram |
| Iris-gw | Gateway ورودی/خروجی |

Senior QA باید مرز دقیق این ریپوها و این‌که کلاینت به کدام endpoint بزند را مشخص کند.

مفاهیم کلیدی: Master Key، Profile Key، Line، Provider، Pattern، ULID

---

## Melia — Growthbook

Feature flag / آزمایش با Growthbook.

Checklist دانش:
- [ ] کجا Feature Flag تعریف می‌شود؟
- [ ] چطور QA فلگ را برای تست روشن/خاموش می‌کند؟
- [ ] محیط‌های متصل به Melia

---

## QA-Scripts

محل اسکریپت‌های QA (احتمالاً Postman/Newman/automation helpers).

Checklist دانش:
- [ ] چه مجموعه‌هایی داخلش است؟
- [ ] چطور اجرا می‌شود؟
- [ ] Owner نگهداری

---

## Saga — In-app survey

سرویس نظرسنجی داخل اپ.

Checklist دانش:
- [ ] چه زمانی Survey نشان داده می‌شود؟
- [ ] پنل مدیریت سوالات
- [ ] اثر روی UX و تداخل با Review (Athona)

---

## Yggdrasil — Tag & Category Taxonomy

موتور دسته‌بندی و تگ برای Product/Vendor/User/Ticket + Associationها.

---

## وابستگی‌های متداول (برای دیباگ E2E)

```text
Icarus --OTP SMS--> Iris / Iris-sms
Icarus --user profile--> Artemis (و/یا Cookie service)
App --address/profile--> Artemis
Discovery --categories/tags--> Yggdrasil
App --feature flags--> Melia (Growthbook)
CMS/content --> BiFrost (Strapi) --> احتمالاً SD/Page Builder
Order complete --reviews--> Athona
Athona --rating updated--> سایر سیستم‌ها
Survey triggers --> Saga
Admin ops --> Atlas
هر سرویس --notif--> Iris
```

---

## لینک‌ها

- Git group: `https://git.tapsifood.cloud/ofd/platform`
- Kibana/APM سرویس‌ها
- Keycloak Stage: `https://kc.foodstg.com/...`
