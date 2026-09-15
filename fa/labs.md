# آزمایشگاه‌ها و پروژهٔ پایانی

[فهرست دوره](README.md)

هر آزمایش باید شامل «وضعیت قبل، فرمان‌ها، خروجی مهم، تفسیر، تغییر، بررسی، بازگشت و درس آموخته‌شده» باشد. تصویر صفحه بدون متن فرمان و تفسیر کافی نیست.

## Lab 1 — گزارش فقط‌خواندنی سیستم

بدون sudo یک گزارش بسازید که توزیع، kernel، CPU، memory، disk، filesystemهای متصل، user فعلی، process شمارهٔ یک، interface و route را ثبت کند. هر فرمان را از فصل‌های 101 تا 103 انتخاب و توضیح دهید کدام ستون پاسخ کدام سؤال است. هیچ secret یا کل env را داخل گزارش نگذارید.

معیار قبول: بتوانید از روی گزارش مسیر firmware → bootloader → kernel/initramfs → PID 1 را توضیح دهید و تفاوت disk، partition و mount را نشان دهید.

## Lab 2 — متن و backup قابل بازیابی

یک پوشه با فایل عادی، مخفی، دارای فاصله و نام‌های مشابه بسازید. با find آن‌ها را بدون شکستن نام پیدا کنید، با tar+gzip آرشیو بسازید، محتوا را پیش از استخراج لیست کنید، در پوشهٔ خالی استخراج کنید و با SHA-256 و cmp بازیابی را بسنجید.

خطای کنترل‌شده: یک فایل را پس از ساخت archive تغییر دهید و توضیح دهید چرا hash یا cmp فرق می‌کند.

## Lab 3 — Bash report

اسکریپتی بنویسید که دقیقاً یک output directory بگیرد؛ ورودی غلط را روی stderr و status 2 بدهد؛ با تابع heading بسازد؛ hostname، kernel، uptime، memory و filesystem را ذخیره کند؛ با loop فایل‌های خروجی را بررسی کند؛ در خطای تولید status غیرصفر دهد؛ و `bash -n` و ShellCheck را بگذراند.

## Lab 4 — Storage مصرفی

ابتدا تمرین image فصل 104 را کامل کنید. سپس فقط روی دیسک مجازی خالیِ جدا و با تأیید دو‌مرحله‌ای:

1. نام، اندازه، model و mount را با lsblk/findmnt ثابت کنید.
2. GPT و یک partition بسازید.
3. ext4 با label بسازید.
4. mount موقت و نوشتن فایل را بررسی کنید.
5. UUID واقعی را بگیرید و entry محدود fstab بسازید.
6. با findmnt --verify بررسی و همان mount را آزمایش کنید.
7. unmount، check غیرتغییردهنده و cleanup تنظیم را انجام دهید.

معیار رد: استفاده از device حدسی، fsck اصلاح‌کننده روی mount فعال، یا reboot پیش از اعتبارسنجی fstab.

## Lab 5 — دو user و پوشهٔ تیمی

در VM دو user و یک group lab بسازید. عضویت را با `usermod -aG` اضافه کنید. یک پوشهٔ SGID با mode 2770 بسازید. در نشست تازهٔ هر user فایل بسازید و inheritance گروه را بررسی کنید. umaskهای 022، 027 و 077 را مقایسه کنید. در پایان UIDهای مالک فایل را پیش از حذف حساب‌ها بررسی کنید.

## Lab 6 — سه scheduler

یک script فقط‌خواندنی را با cron، at و systemd timer اجرا کنید. محیط، مسیر executable، زمان واقعی و log هر سه را ثبت کنید. یک اجرای ازدست‌رفتهٔ timer را با `Persistent=true` در VM بررسی کنید. هر سه را بدون حذف jobهای نامرتبط cleanup کنید.

## Lab 7 — شبکه و DNS

وضعیت سالم link، address، route، socket و DNS را ثبت کنید. روی interface جداگانهٔ lab، هر بار فقط یکی از خطاهای prefix غلط، route گمشده، resolver غلط و service متوقف را ایجاد کنید. پیش از اصلاح، دو فرضیه و آزمون تفکیک‌کننده بنویسید. dig مستقیم و getent را مقایسه کنید.

## Lab 8 — Log و rotation

یک tag با logger بسازید، آن را در journal با tag/time/priority پیدا کنید، یک rule local0 فقط برای lab اضافه و قبل از reload با rsyslogd -N1 بررسی کنید. policy logrotate بسازید و نخست با --debug بخوانید. فایل‌ها و ruleهای lab را در پایان حذف کنید.

## Lab 9 — SSH و GPG

از console fingerprint host را بگیرید. key با passphrase بسازید، public key را نصب و نشست دوم را پیش از هر تغییر auth آزمایش کنید. یک tunnel loopback-only بسازید. سپس key GPG مصرفی تولید، public key و revocation را جدا ذخیره، یک فایل را encrypt/decrypt و sign/verify کنید.

معیار رد: چاپ private key، پذیرش host key بدون مقایسه، یا بستن روش ورود قبلی پیش از آزمون نشست دوم.

## پروژهٔ پایانی — آماده‌سازی یک Linux کوچک

روی VM تازه و بدون دنبال‌کردن recipe خط‌به‌خط:

1. موجودی system و طرح disk را مستند کنید.
2. یک service ساده را از repository نصب و مالک package/file را اثبات کنید.
3. user غیرroot محدود و پوشهٔ داده با گروه درست بسازید.
4. script health report و timer روزانه بسازید.
5. log آن را با retention محدود نگه دارید.
6. profile شبکه و DNS را مستند و مسیر عیب‌یابی را آزمایش کنید.
7. SSH key و fingerprint را امن مدیریت کنید.
8. listener، service، SUID/SGID و sudo را audit کنید.
9. از دادهٔ برنامه backup مستقل بگیرید و restore روی VM دوم انجام دهید.
10. تمام تغییرها، verification و rollback را در یک runbook بنویسید.

پروژه وقتی قبول است که شخص دیگری فقط با runbook شما بتواند وضعیت را بررسی، خطای ایجادشده را تشخیص و داده را بازیابی کند.
