# QA Playbook — تپسی‌فود

## هدف

این صفحه روش کار استاندارد QA را مشخص می‌کند تا نیروهای جدید یکسان تست کنند و دانش در ذهن افراد نماند.

---

## اصول

1. اول Owner اسکواد/سرویس را پیدا کن، بعد تست کن.
2. همیشه محیط را بنویس: Dev / Stage / Prod.
3. برای باگ E2E زنجیره سرویس‌ها را ذکر کن.
4. بدون اکانت تست استاندارد، تست را Start نکن مگر برای دسترسی‌ها.
5. مستند و تست را همزمان جلو ببر؛ دانش شفاهی کافی نیست.

---

## محیط‌ها

| محیط | کاربرد QA | نکته |
| --- | --- | --- |
| Dev | توسعه و دیباگ سریع | ناپایدارتر |
| Stage / foodstg | تست اصلی پیش از Prod | نزدیک به واقعیت |
| Prod | مانیتور و بررسی محدود | بدون داده مخرب |

---

## حداقل Smoke روزانه/هفتگی (پیشنهادی)

### Customer App / Web
- [ ] باز شدن هوم
- [ ] لاگین OTP
- [ ] تغییر آدرس و تغییر لیست رستوران
- [ ] سرچ رستوران/غذا
- [ ] افزودن به سبد
- [ ] اعمال کوپن (اگر اکانت داشته باشد)
- [ ] رسیدن تا درگاه (بدون پرداخت واقعی در صورت محدودیت)

### Vendor
- [ ] لاگین پنل وندور
- [ ] مشاهده سفارش تست
- [ ] تغییر وضعیت ساده منو/موجودی (در Stage)

### Platform
- [ ] Icarus login/verify
- [ ] Iris health + send test SMS در Stage
- [ ] Artemis create/get profile در Stage
- [ ] Athona create review path در Stage

---

## قالب گزارش باگ

```text
Title:
[Squad][Env] خلاصه مشکل

Environment:
- Dev / Stage / Prod

Squad / Service:
- ...

Preconditions:
- ...

Steps:
1.
2.
3.

Expected:
- ...

Actual:
- ...

Evidence:
- Screenshot / video
- RequestId / TraceId
- OrderId / UserId / ULID

Impact:
- Blocker / High / Medium / Low

Suspected chain:
- e.g. Discovery → OMS → Finance
```

---

## ابزارهای اجباری آشنایی

1. Confluence همین Space
2. Kibana/APM
3. Metabase
4. Postman/Newman یا مجموعه API تیم
5. Swagger سرویس‌های Platform
6. CD برای فهم نسخه دیپلوی‌شده
7. پنل‌های Chef / BO / Vendor / Order

---

## استراتژی تست بر اساس نوع تغییر

| نوع تغییر | حداقل پوشش |
| --- | --- |
| تغییر UI هوم/کروسل/تایل | Visual + Deep link + شهرهای مختلف |
| تغییر Auth | OTP, refresh, logout, cookie |
| تغییر کوپن | مرزهای اعمال، هم‌زمانی با سبد |
| تغییر دلیوری | Own vs Zap vs Pickup |
| تغییر منو | نمایش در Discovery + سفارش |
| تغییر ریویو | Visibility Pending/Approved |

---

## Definition of Ready برای تست

- لینک بیلد/محیط آماده است
- اکانت تست مشخص است
- معیار پذیرش نوشته شده
- Owner برای سوال موجود است
- داده تست (رستوران/کد تخفیف/آدرس) مشخص است

## Definition of Done برای QA

- سناریوهای پذیرش پاس شده
- ریسک‌های باقی‌مانده نوشته شده
- باگ‌های باز اولویت‌بندی شده
- در صورت نیاز، صفحه Confluence آپدیت شده
