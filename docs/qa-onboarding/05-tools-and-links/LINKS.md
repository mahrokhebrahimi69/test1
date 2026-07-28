# لینک‌ها و سامانه‌ها

> قبل از شروع تست، دسترسی همه لینک‌های لازم را درخواست و تأیید کنید.

---

## محصول و پنل‌ها

| سامانه | لینک | کاربرد تقریبی |
| --- | --- | --- |
| سایت اصلی | https://tapsi.food | محصول مشتری |
| Order Dashboard | https://order.tapsi.food/dashboard | مانیتور/عملیات سفارش |
| Vendor BO (نمونه) | https://bo.tapsi.food/vendor/2696km/management | مدیریت وندور |
| BO UI Stage | https://bo-ui.foodstg.com/ | بک‌آفیس Stage |
| BO UI Dev | https://bo-ui-dev.foodstg.com/ | بک‌آفیس Dev |
| Vendor در BO Stage | https://bo-ui.foodstg.com/vendor | پنل وندور Stage |
| Chef Prod | https://chef.tapsi.food/login/cellphone | آفیس ستادی |
| Chef Stage | https://chef.foodstg.com/login/cellphone | Chef Stage |
| Chef Dev | https://chef-dev.foodstg.com/login/cellphone | Chef Dev |

---

## Identity / Auth

| سامانه | لینک | کاربرد |
| --- | --- | --- |
| Keycloak Stage Admin | https://kc.foodstg.com/realms/master/protocol/openid-connect/auth?... | مدیریت Identity |
| Icarus (از طریق APM) | Kibana APM services/Icarus | مانیتور تراکنش‌های Auth |

---

## Observability / Data

| سامانه | لینک | کاربرد |
| --- | --- | --- |
| Kibana Prod-like | https://kibana.tapsifood.cloud/login?... | APM / لاگ / تریس |
| Kibana Stage | https://kibana.foodstg.com/login?next=%2F | لاگ Stage |
| Metabase | https://metabase.tapsifood.cloud/... | کوئری دیتا / بررسی سفارش و کاربر |
| CD (Continuous Delivery) | https://cd.foodstg.com/login?... | دیپلوی اپلیکیشن‌ها |
| Doc portal | https://doc.tapsifood.cloud/pages/viewpage.action?spaceKey=TD&title=GetRefundAndPaymentStatusForOrder | مستندات فنی (نمونه Refund) |
| Datagif | https://datagif.fr/en/ | ابزار/مرجع مرتبط داده (نیازمند توضیح Owner) |

---

## چک‌لیست دسترسی نیروی جدید

برای هر مورد وضعیت را مشخص کنید: `Requested / Granted / Blocked`

- [ ] tapsi.food (حساب تست)
- [ ] BO Dev
- [ ] BO Stage
- [ ] Chef Dev/Stage
- [ ] Order Dashboard
- [ ] Kibana Stage
- [ ] Kibana Prod (در صورت نیاز)
- [ ] Metabase
- [ ] Keycloak Stage
- [ ] CD Stage
- [ ] Confluence / Doc portal
- [ ] GitLab/GitHub ریپوهای مرتبط
- [ ] Vault / Secret access (در صورت نیاز QA)
- [ ] شماره تست و امکان دریافت OTP واقعی/استیج

---

## اکانت‌های تست استاندارد (باید تکمیل شود)

| نقش | یوزرنیم/موبایل | محیط | Owner | توضیحات |
| --- | --- | --- | --- | --- |
| Customer | TBD | Stage | TBD | |
| Vendor | TBD | Stage | TBD | |
| Support | TBD | Stage | TBD | |
| Chef Staff | TBD | Stage | TBD | |
| Finance Ops | TBD | Stage | TBD | |

---

## قانون نگهداری لینک‌ها

1. لینک شکسته را همان روز Fix یا `Deprecated` کنید.
2. برای هر سامانه Owner مشخص باشد.
3. لینک Prod و Stage را قاطی نکنید؛ همیشه Environment را در عنوان بنویسید.
