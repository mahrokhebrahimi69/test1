# گام‌به‌گام: ساخت فضای انبوردینگ در Confluence

این راهنما را خط به خط اجرا کنید. بعد از ساخت هر صفحه، محتوای فایل متناظر را کپی‌پیست کنید.

---

## گام 0 — پیش‌نیاز

1. دسترسی Create Space در Confluence داشته باشید.
2. یک پوشه موقت در Notes یا Google Doc برای نگه داشتن لینک صفحات بسازید (برای Parent/Child لینک‌دهی).
3. Owner صفحه: تیم لید QA (شما).
4. Contributor اصلی: همکار قدیمی QA + یک نفر از هر اسکواد (در صورت نیاز).

---

## گام 1 — ساخت Space

1. Confluence → Spaces → Create space
2. نوع: **Documentation** یا **Team**
3. نام Space:

```text
QA Onboarding — Tapsi Food
```

4. Key پیشنهادی:

```text
QAONB
```

5. توضیح Space:

```text
فضای رسمی انبوردینگ QA تپسی‌فود. شامل معرفی محصول، اسکوادها، سرویس‌های Platform، لینک سامانه‌ها، واژه‌نامه، و مسیر مطالعه نیروهای جدید.
```

---

## گام 2 — ساخت درخت صفحات (Parent / Child)

در Space یک صفحه Home بسازید، سپس صفحات زیر را به‌صورت Child ایجاد کنید.

### درخت پیشنهادی

```text
🏠 QA Onboarding Home
├── 1. شروع سریع نیروی جدید
├── 2. تپسی‌فود چیست؟
│   ├── سفر کاربر (User Journey)
│   └── اجزای اصلی محصول
├── 3. نقشه اسکوادها
│   ├── AI
│   ├── Chef
│   ├── COIMP / PROMC
│   ├── Delivery
│   ├── Finance
│   ├── Menu Management
│   ├── OMS (Order Management)
│   ├── Platform
│   ├── Search & Discovery
│   ├── Vendor
│   └── TPCH (نیازمند تکمیل)
├── 4. سرویس‌های Platform
│   ├── Iris (Notification)
│   ├── Icarus (Auth)
│   ├── Artemis (User Profile)
│   ├── Yggdrasil (Category & Tag)
│   └── Falafel (Review & Rating)
├── 5. لینک‌ها و سامانه‌ها
├── 6. واژه‌نامه محصول (Carousel, Tile, …)
├── 7. QA Playbook
│   ├── محیط‌ها (Dev / Stage / Prod)
│   ├── ابزارهای مشاهده‌پذیری
│   └── چک‌لیست تست Smoke
├── 8. تسک‌ها و مالکیت دانش
│   ├── تسک جمع‌آوری دانش (Senior QA)
│   └── چک‌لیست کمبودها (Gaps)
└── 9. Changelog انبوردینگ
```

---

## گام 3 — ترتیب پر کردن محتوا

| ترتیب | صفحه | منبع محتوا | وضعیت فعلی |
| --- | --- | --- | --- |
| 1 | Home | `01-home/HOME.md` | آماده |
| 2 | شروع سریع | `08-tasks/NEW_JOINER_READING_PATH.md` | آماده |
| 3 | تپسی‌فود چیست؟ | `02-product-overview/PRODUCT.md` | آماده |
| 4 | نقشه اسکوادها | `03-squads/SQUADS.md` | آماده (بخشی TBD) |
| 5 | Platform Services | `04-platform-services/PLATFORM.md` | آماده |
| 6 | لینک‌ها | `05-tools-and-links/LINKS.md` | آماده |
| 7 | واژه‌نامه | `06-glossary/GLOSSARY.md` | آماده |
| 8 | QA Playbook | `07-qa-playbook/QA_PLAYBOOK.md` | آماده |
| 9 | تسک Senior QA | `08-tasks/SENIOR_QA_KNOWLEDGE_TASK.md` | آماده |
| 10 | Gaps | `08-tasks/GAPS_CHECKLIST.md` | آماده |

---

## گام 4 — برچسب‌گذاری (Labels)

برای هر صفحه این Labelها را بزنید:

- `qa-onboarding`
- `tapsi-food`
- یکی از: `squad` / `platform-service` / `glossary` / `tooling` / `task`

---

## گام 5 — دسترسی‌ها

| گروه | دسترسی |
| --- | --- |
| QA Team | Edit |
| Engineering (همه اسکوادها) | View |
| Product / Biz | View روی صفحات محصول و واژه‌نامه |
| Guest / Contractor | فقط صفحه Home + شروع سریع (اختیاری) |

---

## گام 6 — اعلام در تیم

پیام آماده برای اسلک/تیمز:

```text
سلام تیم 👋
فضای انبوردینگ QA تپسی‌فود آماده شد:
[لینک Space]

نیروهای جدید از صفحه «شروع سریع» شروع کنند.
همکار قدیمی QA لطفاً تسک «جمع‌آوری دانش اسکوادها» را طبق چک‌لیست تکمیل کند.
کمبودها در صفحه Gaps ثبت شده و باید تا [تاریخ] بسته شوند.
```

---

## گام 7 — نگهداری

- هر اسکواد Owner یک صفحه دارد.
- هر فصل یک Review کوتاه روی Gaps انجام شود.
- تغییر سرویس/لینک/واژه باید همان روز در Confluence آپدیت شود.
