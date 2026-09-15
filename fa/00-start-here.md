# فصل صفر — شروع Linux از هیچ

[فهرست دوره](README.md)

## Linux، kernel و distribution چیست؟

سیستم‌عامل واسطهٔ برنامه و سخت‌افزار است. Kernel هسته‌ای است که CPU، memory، process، device و filesystem را مدیریت می‌کند. «Linux» دقیق‌تر نام kernel است. Distribution یا توزیع، kernel را همراه commandها، package manager، installer و تنظیم‌ها ارائه می‌کند؛ Debian، Ubuntu، Rocky Linux، AlmaLinux، Fedora و openSUSE نمونه‌اند.

LPIC-1 وابسته به یک توزیع نیست. به همین دلیل هم APT/Dpkg و هم RPM/DNF/Zypper، و هم ابزار جدید و قدیمی را می‌خوانید.

## محیط امن بسازید

برای دوره دو VM پیشنهاد می‌شود:

| VM | سیستم پیشنهادی | CPU | RAM | دیسک | کاربرد |
|---|---|---:|---:|---:|---|
| `lpic-debian` | Debian 12/13 یا Ubuntu LTS | 2 | 2 GiB | 25 GiB | APT، Bash، systemd، NetworkManager |
| `lpic-rpm` | Rocky/AlmaLinux 9/10 | 2 | 2 GiB | 25 GiB | RPM و DNF |

یک دیسک مجازی خالی جدا برای storage lab اضافه کنید. پیش از تغییر خطرناک snapshot بگیرید. Snapshot داخل همان storage، backup مستقل نیست.

### مثال ۱: شناخت نسخه

```bash
cat /etc/os-release
uname -r
uname -m
```

توضیح خط‌به‌خط:

1. `cat` فایل شناسایی توزیع را می‌خواند؛ `NAME` نام و `VERSION_ID` نسخه است.
2. `uname -r` نسخهٔ kernel در حال اجرا را می‌دهد؛ این با نسخهٔ توزیع یکی نیست.
3. `uname -m` معماری machine مثل `x86_64` یا `aarch64` را می‌دهد.

## Terminal، shell و prompt

Terminal ورودی/خروجی متن و shell برنامهٔ تفسیر دستور است. در راهنما:

```text
$ command
# administrative-command
```

علامت `$` یا `#` را تایپ نکنید. اولی معمولاً کاربر عادی و دومی root را نشان می‌دهد. در مثال‌های دوره فرمان مدیریتی با `sudo` صریح نوشته می‌شود.

### مثال ۲: اولین پوشهٔ تمرین

```bash
pwd
mkdir -p "$HOME/lpic-course/first-lab"
cd "$HOME/lpic-course/first-lab"
printf 'hello linux\n' > hello.txt
cat hello.txt
```

توضیح خط‌به‌خط:

1. `pwd` مسیر فعلی را نشان می‌دهد.
2. `mkdir` پوشه می‌سازد؛ `-p` والدهای لازم را هم می‌سازد؛ `$HOME` خانهٔ کاربر است و نقل‌قول فاصله را امن نگه می‌دارد.
3. `cd` پوشهٔ همین shell را عوض می‌کند.
4. `printf` متن و newline می‌سازد؛ `>` آن را در فایل تازه می‌ریزد و اگر فایل قبلاً باشد محتوایش را جایگزین می‌کند.
5. `cat` فایل را می‌خواند. خروجی باید `hello linux` باشد.

## مسیر absolute و relative

`/etc/hosts` مسیر absolute است چون از `/` آغاز می‌شود. `hello.txt` relative است و از پوشهٔ فعلی پیدا می‌شود. `.` یعنی همین پوشه، `..` والد و `~` در shell خانهٔ کاربر است.

### مثال ۳: دنبال‌کردن مسیر

```bash
pwd
ls -l ./hello.txt
cd ..
pwd
ls -l first-lab/hello.txt
```

توضیح خط‌به‌خط:

1. محل فعلی باید first-lab باشد.
2. `./` همین پوشه و `-l` جزئیات فایل است.
3. `..` یک سطح بالا می‌رود.
4. مسیر جدید را تأیید می‌کند.
5. همان فایل از مسیر relative جدید پیدا می‌شود.

## root، `/` و `/root` سه معنی متفاوت

- `root` نام حساب مدیر با UID صفر است.
- `/` بالاترین پوشهٔ درخت فایل است.
- `/root` home معمول حساب root است.

`sudo COMMAND` فقط همان فرمان را با مجوز policy اجرا می‌کند. `sudo` دستور غلط را درست یا بی‌خطر نمی‌کند.

### مثال ۴: مستندات و موفقیت فرمان

```bash
type cd
command -v ls
man ls
true
printf 'status=%s\n' "$?"
false
printf 'status=%s\n' "$?"
```

توضیح خط‌به‌خط:

1. `type` می‌گوید cd builtin است.
2. `command -v` راه اجرای ls را نشان می‌دهد.
3. manual را باز می‌کند؛ `/pattern` جست‌وجو و `q` خروج است.
4. `true` همیشه status صفر برمی‌گرداند.
5. `$?` نتیجهٔ بلافاصله قبل است، پس صفر چاپ می‌شود.
6. `false` status غیرصفر می‌دهد.
7. این بار عدد 1 معمول است. status متن خطا نیست؛ قراردادی برای نتیجه است.

## وقتی خروجی فرق دارد

پشت‌سرهم فرمان تصادفی نزنید. این شش مورد را بنویسید:

1. فرمان دقیق و علامت مشاهده‌شده
2. خروجی و status
3. توزیع و نسخه
4. دو علت احتمالی
5. یک آزمون فقط‌خواندنی که آن دو را جدا کند
6. کوچک‌ترین اصلاح برگشت‌پذیر و روش بررسی آن

پس از انجام مثال‌های این فصل، [فصل 101](101.md) را شروع کنید.
