# Як не стати кібер-жертвою

Правила персональної кібербезпеки, які врятують вам гроші, нерви, а може й життя.

Цей документ створений фахівцями у сфері кібербезпеки з великим досвідом у розробці, аналізі та етичному хакінгу комп'ютерних систем і мереж. Інструкції надаються "як є", і автори не несуть відповідальності за ваші дії чи бездіяльність. Ви вільні розповсюджувати, використовувати в бізнесі або модифікувати цей документ. Це безплатно. Посилання на оригінал заохочуються, але не є обов'язковими.

Дякуємо, що піклуєтеся про свою кібербезпеку. Поширте ці рекомендації серед рідних, друзів та колег, щоб зробити світ безпечнішим. Якщо у вас є доповнення або ви помітили помилку в тексті, зверніться за адресою ✉️ [vlad@styran.com](mailto:vlad@styran.com) або [створіть issue на GitHub](https://github.com/sapran/dontclickshit/issues/new).

## Зміст

1. [Не натискайте каку](#user-content-не-натискайте-каку)
1. [Використовуйте парольні менеджери](#user-content-використовуйте-парольні-менеджери)
1. [Використовуйте двофакторну автентифікацію](#user-content-використовуйте-двофакторну-автентифікацію)
1. [Використовуйте безпечні месенджери](#user-content-використовуйте-безпечні-месенджери)
1. [Використовуйте віртуальні приватні мережі (VPN)](#user-content-використовуйте-віртуальні-приватні-мережі-vpn)
1. [Шифруйте дані](#user-content-шифруйте-дані)
1. [Операційна система та програми](#user-content-операційна-система-та-програми)
1. [Антивірус](#user-content-антивірус)
1. [Фаєрвол](#user-content-фаєрвол)
1. [Робіть резервні копії](#user-content-робіть-резервні-копії)
1. [Мобільна безпека](#user-content-мобільна-безпека)
1. [Фізична безпека](#user-content-фізична-безпека)
1. [Подяка](#user-content-подяка)

## Не натискайте каку

### Що мається на увазі?

Не відкривайте, не натискайте, та не запускайте підозрілі файли, посилання та програми. 💡 Головне правило: якщо ви на це (лист, файл, посилання тощо) не чекали, – це підозріло.

### Підозрілі файли

Не відкривайте файли, електронні вкладення або архіви від недовірених джерел. Все, що надходить від незнайомців, слід вважати потенційно небезпечним. Рекомендуємо перенаправити такі електронні листи в спам.

Якщо ви знайомі з відправником, але не очікували від нього кореспонденції або файлів, зверніться до нього через інший комунікаційний канал для підтвердження. Це необхідно для виявлення можливого компрометування його акаунту. Наприклад, якщо ви отримали документ Word через електронну пошту, зв'яжіться з відправником по телефону або через месенджер, щоб уточнити, чи дійсно він вас цікавить та чи відправив вам цей файл.

:exclamation: Найбільш ризиковані типи файлів:
- Виконувані файли: `EXE`, `COM`, `CMD`, `BAT`, `PS1`, `ELF`.
- Скрипти та код: `JS`, `VBS`, `PY`, `PHP`, `SH`.
- Офісні документи з макросами: `DOCM`, `XLSM`, `PPTM`.
- PDF з активним вмістом: `PDF`.
- Файли векторної графіки з вбудованим кодом: `SVG`.
- Архіви, особливо з авто-виконанням або захищені паролем: `ZIP`, `RAR`, `7Z`.

Інколи, зокрема коли час тисне, важко відрізнити безпечні файли від шкідливих. Для експрес-аналізу використовуйте сервіс VirusTotal. Ця платформа сканує файли за допомогою понад 50 антивірусних програм. Однак ❗зверніть увагу, що завантажуючи файли на VirusTotal, ви надаєте до них доступ третім сторонам.

:wrench: VirusTotal: https://virustotal.com

### Підозрілі посилання

Не клацайте на сумнівні URL, особливо на ті, що ведуть до незнайомих вебсайтів. Перевіряйте доменні імена перед клацанням. Зловмисники часто маскують домени під знайомі назви (наприклад, `facelook.com`, `gooogle.com`, `tw1tter.com`, `gma1l.com`, `amaz0n.co` тощо). Використовуйте HTTPS і перевіряйте SSL-сертифікати.

Шкідливі URL можуть бути приховані в HTML, документах та емейлах. Наведіть курсор на URL, але не клацайте, щоб побачити справжню адресу. Використовуйте VirusTotal для перевірки URL, як і для файлів.

Будьте обережні з QR-кодами та скороченими URL від сервісів типу tinyurl.com. Не скануйте та не вводьте їх, якщо не впевнені в їхній безпекі.

- CheckShortURL: [https://checkshorturl.com/](https://checkshorturl.com/)
- GetLinkInfo: [http://getlinkinfo.com/](http://getlinkinfo.com/)
- Unshorten.it: [https://unshorten.it/](https://unshorten.it/)
- Unshorten.me: [https://unshorten.me/](https://unshorten.me/)
- RevealURL: [http://revealurl.com/](http://revealurl.com/)
### Спливаючі (pop-up) вікна

Будьте уважні до спливаючих вікон і повідомлень в браузері, програмах, ОС та смартфоні. Завжди уважно читайте їх вміст і не погоджуйтеся з ними поспішно.

Зловмисники можуть використовувати спливаючі вікна для різних цілей: встановлення фальшивих SSL-сертифікатів для перехоплення мережевого трафіку, завантаження шкідливого ПЗ на вашу техніку, або перенаправлення браузера на інфіковані сайти.

### Підозрілі пристрої

Не підключайте невідомі флешки, зовнішні диски, CD чи DVD до свого комп'ютера. Злам може відбутися навіть перед тим, як ви відкриєте файл, і до того, як антивірус його просканує. Якщо пристрій знайдено в офісі, отримано поштою або від незнайомця, існує ризик, що він може бути інфікований. Використовуйте лише відомі вам носії та будьте обережні з пристроями від третіх осіб.

## Використовуйте парольні менеджери

Використовуйте менеджери паролів для генерації, зберігання та захисту паролів, дотримуючись наступних рекомендацій:

1. Створюйте паролі довжиною не менше 20 символів, використовуючи випадкову комбінацію.
2. Встановіть складний майстер-пароль для доступу до менеджера паролів.
3. Виберіть менеджер паролів, який зберігає базу даних у зашифрованому вигляді, перш ніж зберігати її в хмарі або синхронізувати між пристроями.
4. Регулярно, ідеально автоматично, створюйте резервні копії вашої бази паролів.

🔧 Приклади надійних парольних менеджерів:

- Dashlane: [https://www.dashlane.com/](https://www.dashlane.com/)
- 1Password: [https://1password.com/](https://1password.com/)
- Bitwarden: [https://bitwarden.com/](https://bitwarden.com/)
- NordPass: [https://nordpass.com/](https://nordpass.com/)

### Тримайте паролі в секреті

Тільки ви повинні знати свої паролі. Не діліться ними з ніким, навіть з вашими близькими, керівниками чи службою підтримки. Для них немає жодної логічної чи законної причини знати ваші паролі. З технічного боку, система, де ви використовуєте пароль, не має до нього прямого доступу. Замість цього вона зберігає криптографічний "хеш" пароля.

### Як вигадати мастер-пароль?

Майстер-пароль до вашого парольного менеджера має бути зручним, але надійним. Він може складатися з чотирьох або більше незалежних слів. Щоб зробити пароль сильнішим, одне зі слів можна ввести великими літерами.

:bulb: Приклади сильних паролів, згенерованих програмою 1Password:

`hyping-BASKET-bouquet-outs`

`tinsel-dolt-INDIGENT-echo`

### Оновлення паролів

:bulb: "Правило буравчика": чим частіше ви використовуєте пароль, тим частіше він повинен змінюватись.

### Перевірити чи пароль не скомпрометовано

Витоки баз даних з логінами та паролями стаються регулярно. Використовуйте сайт [';--have i been pwned?](https://haveibeenpwned.com/) для перевірки безпеки вашого пароля. Зареєструйтеся на сайті, щоб отримувати сповіщення про можливі майбутні порушення безпеки ваших аккаунтів.

## Використовуйте двофакторну автентифікацію

### Увімкніть двофакторну автентифікацію

Увімкніть двофакторну автентифікацію на всіх сучасних онлайн-сервісах за допомогою апаратних ключів чи програмних токенів від Microsoft, Google, Authy та інших. Деякі парольні менеджери також підтримують цю функцію.

Налаштування двофакторної автентифікації популярних сервісів:

- Google: [https://myaccount.google.com/signinoptions/two-step-verification](https://myaccount.google.com/signinoptions/two-step-verification)
- Facebook: [https://www.facebook.com/settings?tab=security&section=two_fac_auth&view](https://www.facebook.com/settings?tab=security&section=two_fac_auth&view)
- Twitter: [https://twitter.com/settings/security](https://twitter.com/settings/security)
- Instagram: [https://www.instagram.com/accounts/two_factor_authentication/](https://www.instagram.com/accounts/two_factor_authentication/)
- Microsoft: [https://account.microsoft.com/security](https://account.microsoft.com/security)
- Apple: [https://appleid.apple.com/account/manage](https://appleid.apple.com/account/manage)
- LinkedIn: [https://www.linkedin.com/psettings/two-step-verification](https://www.linkedin.com/psettings/two-step-verification)
- GitHub: [https://github.com/settings/security](https://github.com/settings/security)
- Dropbox: [https://www.dropbox.com/account/security](https://www.dropbox.com/account/security)
- PayPal: [https://www.paypal.com/myaccount/settings/security/2fa](https://www.paypal.com/myaccount/settings/security/2fa)

🔧 Решту сервісів ви знайдете на цьому вебсайті: [https://twofactorauth.org](https://twofactorauth.org/)

Найкращий другий фактор автентифікації – це ключ безпеки або токен.

🔧 Найпопулярніші ключі безпеки:

- YubiKey: [https://www.yubico.com/products/yubikey-hardware/](https://www.yubico.com/products/yubikey-hardware/)
- Google Titan Security Key: [https://store.google.com/product/titan_security_key](https://store.google.com/product/titan_security_key)
- Thetis FIDO U2F Security Key: [https://thetismedia.com/products/thetis-fido-u2f-security-key](https://thetismedia.com/products/thetis-fido-u2f-security-key)
- Feitian MultiPass K16: [https://www.ftsafe.com/Products/FIDO/BLE/K16](https://www.ftsafe.com/Products/FIDO/BLE/K16)
- Ledger Nano S: [https://shop.ledger.com/products/ledger-nano-s](https://shop.ledger.com/products/ledger-nano-s)

🔧 Зручні додатки для другого фактору автентифікації:

- Google Authenticator for Android [https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)
- Google Authenticator for iOS [https://apps.apple.com/us/app/google-authenticator/id388497605](https://apps.apple.com/us/app/google-authenticator/id388497605)
- Authy: [https://authy.com/](https://authy.com/)
- Microsoft Authenticator: [https://www.microsoft.com/en-us/account/authenticator](https://www.microsoft.com/en-us/account/authenticator)
- Duo Mobile: [https://duo.com/product/trusted-users/two-factor-authentication/duo-mobile](https://duo.com/product/trusted-users/two-factor-authentication/duo-mobile)

### Уникайте SMS

Уникайте другого фактору автентифікації з використанням одноразових паролів через SMS – це вкрай небезпечно.

## Використовуйте безпечні месенджери

Використовуйте наскрізне шифрування для захисту приватних та конфіденційних повідомлень. Це забезпечує, що доступ до даних мають лише ви та ваш співрозмовник.

🔧 Безпечні месенджери:

- Signal: [https://signal.org/](https://signal.org/)
- Threema: [https://threema.ch/en](https://threema.ch/en)
- Wickr Me: [https://wickr.com/](https://wickr.com/)
- Wire: [https://wire.com/en/](https://wire.com/en/)

:bulb: Порівняння безпеки месенджерів: https://www.securemessagingapps.com

## Використовуйте віртуальні приватні мережі (VPN)

Щоб захистити ваш мережевий трафік від прослуховування, використовуйте віртуальні приватні мережі (Virtual Private Networks, VPN). Найкращий спосіб зробити це – встановити свій власний VPN-сервер.

🔧 Algo – розгорнути власний сервер VPN в будь-якому популярному хмарному сервісі: [https://github.com/trailofbits/algo](https://github.com/trailofbits/algo)

🔧 Outline – ще простіший спосіб налаштувати власний сервер VPN: [https://getoutline.org/](https://getoutline.org/)

🔧 Додаткові альтернативи:

- WireGuard: [https://www.wireguard.com/](https://www.wireguard.com/)
- ZeroTier: [https://www.zerotier.com/](https://www.zerotier.com/)

Використання VPN-сервісів не рекомендується, але може бути допустимим, коли немає змоги скористатися власним VPN.

🔧 Порівняльна таблиця VPN-сервісів: https://thatoneprivacysite.net/#simple-vpn-comparison

## Шифруйте дані

### Перевіряйте шифрування вебсайтів

Завжди переконуйтесь, що вебсайт, якому ви передаєте свої чутливі дані, використовує HTTPS. Це означає, що його адреса в адресному рядку браузера починається з `https://` та його сертифікат перевірений вашим браузером, отже він не робить вам попереджень безпеки.

Однак, наявності HTTPS не достатньо для повної довіри до вебсайту: будь-хто може згенерувати дійсний сертифікат для свого вебсервера. Потрібно звернути увагу та перевірити правильність доменного імені вебсайту, тому що його можна підробити.

❗ Ніколи, навіть для тимчасового використання, не приймайте недійсні сертифікати SSL.

### Шифруйте хмарні дані

Шифруйте дані перед завантаженням в хмару. Пам'ятайте: немає ніякої "хмари", це просто чийсь чужий комп'ютер. `Keybase` та `Boxcryptor` – це інструменти, які дозволяють шифрувати дані в автономному режимі, перш ніж завантажити їх у хмарне сховище. `Cryptomator` створює універсальний зашифрований логічний диск, який можна синхронізувати між вашими пристроями через хмарне сховище.

🔧 Популярні інструменти хмарного шифрування:

- Boxcryptor: [https://www.boxcryptor.com/](https://www.boxcryptor.com/)
- Cryptomator: [https://cryptomator.org/](https://cryptomator.org/)
- Tresorit: [https://tresorit.com/](https://tresorit.com/)
- NordLocker: [https://nordlocker.com/](https://nordlocker.com/)
- VeraCrypt: [https://www.veracrypt.fr/en/Home.html](https://www.veracrypt.fr/en/Home.html)

🔧 В iCloud існує вбудований інструмент `Advanced Data Protection` для надійного шифрування: [https://support.apple.com/en-us/HT212520](https://support.apple.com/en-us/HT212520).
### Шифруйте дані на диску

Використовуйте функцію `Full Disk Encryption` вашої операційної системи для захисту даних на ноутбуці або ПК від крадіжки або втрати. FDE це безплатна функція у Linux, MacOS та Windows Pro.

#### macOS

Увімкніть `File Vault` ([](https://support.apple.com/en-us/HT204837)[https://support.apple.com/en-us/HT204837](https://support.apple.com/en-us/HT204837)).

1. Відкрийте `System Preferences` (Системні налаштування).
1. Клацніть на `Security & Privacy` (Безпека та конфіденційність).
1. Перейдіть на вкладку `FileVault`.
1. Клацніть на замок унизу і введіть адміністративний пароль.
1. Клацніть `Turn On FileVault` (Увімкнути FileVault).

Це ввімкне FileVault і почне процес шифрування диска.

#### Linux

Використовуйте `LUKS` (Linux Unified Key Setup) або інші засоби повного шифрування диску. Як альтернативу, під час встановлення ОС зазвичай можна вибрати параметри шифрування диску або шифрування тільки вашого домашнього розділу.

🔧 Ось посилання на інструкції для популярних дистрибутивів Linux:

- Ubuntu: [https://help.ubuntu.com/community/FullDiskEncryptionHowto](https://help.ubuntu.com/community/FullDiskEncryptionHowto)
- Fedora: [https://fedoraproject.org/wiki/Disk_encryption](https://fedoraproject.org/wiki/Disk_encryption)
- Debian: [https://www.debian.org/doc/manuals/securing-debian-howto/ch-crypto-disk.en.html](https://www.debian.org/doc/manuals/securing-debian-howto/ch-crypto-disk.en.html)
- Arch Linux: [https://wiki.archlinux.org/title/Disk_encryption](https://wiki.archlinux.org/title/Disk_encryption)
- CentOS: [https://wiki.centos.org/HowTos/OS_Protection](https://wiki.centos.org/HowTos/OS_Protection)
#### Windows

Щоб увімкнути повне шифрування диску в Windows за допомогою `BitLocker`, зробіть наступне:

1. Відкрийте `Панель управління` (Control Panel).
2. Перейдіть до `Система і безпека`" (System and Security).
3. Клацніть на `BitLocker Drive Encryption` (Шифрування диска BitLocker).
4. Оберіть диск, який ви хочете зашифрувати, і клацніть `Увімкнути BitLocker` (Turn On BitLocker).
5. Оберіть метод аутентифікації (пароль, смарт-карта тощо) і продовжте.
6. Виберіть режим шифрування і клацніть `Далі` (Next).
7. Підтвердіть увімкнення BitLocker.

Зауважте, що процес шифрування може зайняти певний час. Щойно процес буде завершений, диск буде зашифрований.

💡 Ви також можете шифрувати зовнішні диски або окремі файли.

## Операційна система та програми

Не запускайте програми з правами адміністратора. Завжди входьте в ОС з правами "звичайного" користувача та за потреби підвищуйте привілеї в меню програми `Run As...` коли це потрібно.

❗ Запускаючи програми з правами локального адміністратора, ви надаєте їм можливість перехоплювати доступ та дані інших користувачів, які зараз працюють на вашому комп'ютері або нещодавно заходили в нього. Таким чином зловмисник може перехопити реквізити доступу доменного адміністратора корпорації та повністю скомпрометувати домен `Active Directory`.

Не використовуйте піратські програми. Не запускайте та не встановлюйте програми, завантажені з ненадійних джерел, включаючи торенти та інші мережі обміну файлами. Це особливо стосується "кейгенів" та "крякалок", які зазвичай вимагають прав адміністратора для запуску.

### Windows

Щоб увімкнути автоматичні оновлення в Windows, виконайте наступні кроки:

1. Відкрийте `Панель управління` (Control Panel) або введіть в пошук `Windows Update`.
2. Перейдіть до `Система і безпека` (System and Security).
3. Клацніть на `Windows Update`.
4. Виберіть `Змінити налаштування` (Change settings).
5. В розділі `Важливі оновлення` (Important updates) виберіть `Встановлювати оновлення автоматично` (Install updates automatically).
6. За бажанням, ви можете також вибрати, як часто і коли саме будуть встановлюватися оновлення.
7. Клацніть `ОК` для збереження змін.

Оновлюйте програмне забезпечення від "сторонніх" постачальників регулярно та автоматично.

### macOS

Щоб увімкнути автоматичні оновлення на macOS, зробіть наступне:

1. Відкрийте `System Preferences` (Системні налаштування).
2. Клацніть на `Software Update` (Оновлення програмного забезпечення).
3. Поставте галочку біля `Automatically keep my Mac up to date` (Автоматично тримати мій Mac оновленим).
4. Для додаткових налаштувань клацніть на `Advanced` (Додатково).
5. Виберіть опції, які вам потрібні (наприклад, автоматичне завантаження та встановлення оновлень).
6. Клацніть `OK` для збереження змін.

Тепер ваш Mac буде автоматично оновлюватися.

### Linux

Сучасні дистрибутиви Linux дають змогу налаштувати автооновлення за допомогою засобів ОС, або ж регулярно оновлювати ПЗ вручну. Наприклад, в Ubuntu Linux оновлення ПЗ здійснюється за допомогою команди

```bash
apt update && apt -y upgrade
```

За подробицями щодо вашого дистрибутиву Linux зверніться до документації.

## Антивірус

### macOS та Linux

Сучасні дистрибутиви Linux дають змогу налаштувати автооновлення за допомогою засобів ОС, або ж регулярно оновлювати ПЗ вручну. Наприклад, в Ubuntu Linux оновлення ПЗ здійснюється за допомогою команди

:wrench: Malwarebytes https://www.malwarebytes.com

:wrench: BitDefender https://www.bitdefender.de

### Windows

У Windows користуйтеся антивірусом. Увімкніть та не вимикайте вбудований Microsoft Defender.

## Фаєрвол

### macOS

Для активації файрволу на macOS, виконайте наступні кроки:

1. Відкрийте `System Preferences` (Системні налаштування).
2. Перейдіть у розділ `Security & Privacy` (Безпека і конфіденційність).
3. Переключитесь на вкладку `Firewall` (Файрвол).
4. Клацніть на `Turn On Firewall` (Ввімкнути файрвол) або `Start` для активації.

Ви також можете клацнути на `Firewall Options` (Опції файрволу) для додаткового налаштування, такого як вибір додатків, які можуть приймати вхідні з'єднання.

Встановіть та навчіться користуватися одним зі спеціалізованих клієнтських фаєрволів, таких як

🔧 [Little Snitch](https://www.obdev.at/products/littlesnitch/index.html) (комерційний) або

🔧 [LuLu](https://objective-see.org/products/lulu.html) (безкоштовний з відкритим кодом).

### Windows

Щоб ввімкнути файрвол у Windows, виконайте наступні кроки:

1. Відкрийте `Панель керування` (Control Panel).
2. Перейдіть у розділ `Система та безпека` (System and Security).
3. Клацніть на `Windows Defender Firewall`.
4. У лівій панелі виберіть `Увімкнути або вимкнути Windows Firewall` (Turn Windows Defender Firewall on or off).
5. Увімкніть файрвол для потрібних типів мережі (приватна, публічна) шляхом вибору опції `Увімкнути Windows Firewall` (Turn on Windows Defender Firewall).
6. Збережіть зміни, натиснувши `OK`.
### Linux

Для активації файрволу на Linux, залежно від дистрибутиву, можна використовувати такі інструменти:

1. UFW (Ubuntu Firewall)
    - Встановлення: `sudo apt install ufw`
    - Ввімкнення: `sudo ufw enable`
2. Firewalld (Fedora, CentOS)
    - Встановлення: `sudo dnf install firewalld`
    - Ввімкнення: `sudo systemctl enable --now firewalld`
3. Iptables (Для більшості дистрибутивів)
    - Зазвичай вже встановлено.
    - Налаштування: Редагування правил за допомогою команд `iptables`.
4. nftables (Сучасна альтернатива Iptables)
    - Встановлення: Зазвичай вже встановлено.
    - Налаштування: Редагування правил за допомогою команд `nft`.
5. Gufw (Графічний інтерфейс для UFW)
    - Встановлення: `sudo apt install gufw`
    - Ввімкнення: Запуск через графічний інтерфейс.

Кожен інструмент має свої особливості і налаштування. Вибір залежить від вашої системи і потреб.

## Робіть резервні копії

### macOS

Для налаштування Time Machine на macOS, виконайте наступні кроки:

1. Підключіть зовнішній диск до Mac.
2. Відкрийте `System Preferences` (Системні налаштування).
3. Перейдіть у розділ `Time Machine`.
4. Клацніть на `Select Backup Disk` (Вибрати диск для резервного копіювання).
5. Виберіть підключений диск і клацніть `Use Disk` (Використовувати диск).
6. Включіть опцію `Back Up Automatically` (Робити резервні копії автоматично), якщо хочете автоматичне резервне копіювання.

Додатково можна вибрати папки для виключення з резервних копій у налаштуваннях `Options` (Опції).

Тепер Time Machine буде робити резервні копії вашої системи на вибраному диску коли він підключений.

### Windows

Для налаштування резервного копіювання в найновішій версії Windows (зазвичай Windows 10 або 11), виконайте наступні кроки:

1. Відкрийте `Settings` (Параметри) через меню `Start` (Пуск).
2. Перейдіть у розділ `Update & Security` (Оновлення та безпека).
3. Виберіть `Backup` (Резервне копіювання) у лівій панелі.
4. Клацніть на `Add a drive` (Додати диск) і виберіть диск для резервного копіювання. Це активує функцію `File History`.
### Linux

Користувачі Linux мають доступ до різноманіття засобів створення резервних копій: від `tar` до `rsync` на мережеву файлову шару.

## Мобільна безпека

Мобільна (стільникова) мережа є так само небезпечною, як публічні точки доступу Wi-Fi. Використовуйте ті ж криптографічні засоби у вашій мобільній мережі передачі даних. Не вважайте SMS або ваші голосові розмови приватними: замість цього використовуйте голосові виклики та повідомлення, які шифруються наскрізь.

Використовуйте `iOS`. Судячи з усього, мобільна безпека `Apple` та безпека їхньої екосистеми застосунків є набагато безпечнішою за рішення на базі ОС Android, які контролюються вашим оператором зв'язку або OEM-виробником (Samsung, LG, Sony тощо.)

Якщо `Android`, то `Google`. Тільки пряма підтримка операційної системи з боку виробника може гарантувати своєчасні оновлення безпеки. Будь-які додаткові кроки в ланцюжку постачання (OEM постачальники, стільникові оператори, корпоративні ІТ тощо) знижують рівень безпеки. У деяких випадках оновлення просто припиняють надходити до вашого пристрою через рік або два після початку його використання.

Не "рутайте" (`root`) свій смартфон. Використовуйте тільки дозволені репозиторії додатків, наприклад, `Google Play` та `AppStore`. Не завантажуйте та не встановлюйте "оновлення безпеки", які надходять з неавторизованих джерел програмного забезпечення.

## Фізична безпека

Тримайте ваші речі, де ви можете їх бачити або контролювати. Ваш комп'ютер і гаджети вимагають такого ж рівня фізичної безпеки, який ви забезпечуєте вашим кредитним карткам та ключам від квартири та автомобіля. Пам'ятайте: якщо зловмисник проведе навіть недовгий час наодинці з вашим комп'ютером, це вже буде не ваш комп'ютер, а його. Швидше за все, він зможе повністю скомпрометувати вашу систему. Блокування екрану допомагає, але існують сучасні атаки, від яких воно не захищає.

Отже, не залишайте ваш пристрій без нагляду, особливо коли він працює. Вимикайте його або відправляйте у режим гібернації кожного разу, коли ви залишаєте його без нагляду навіть на декілька хвилин. Налаштуйте повне шифрування диску та запит паролю кожного разу, коли він вмикається.

Здійснюйте чутливі та нечутливі операції з різних комп'ютерів. Якщо ви дозволяєте дітям грати в онлайн-ігри на комп'ютері, який ви використовуєте для онлайн-банкінгу – вас зламають. Якщо ви відвідуєте інтернет-крамниці з ПК в комп'ютерному клубі або інтернет-кафе – вас зламають. Якщо ви відправляєте ділові листи з ПК у відкритій зоні вашого готелю – вас зламають.

Використовуйте окремий комп'ютер для бізнесу та фінансових операцій та усіх дій, які вимагають приватності або конфіденційності. Використовуйте спеціальну віртуальну або фізичну машину для найбільш критичних операцій.

❗ В деяких авторитарних країнах вас можуть _попросити_ надати пароль до вашого зашифрованого носія інформації на кордоні та в аеропорті. Перетинаючи кордони таких держав, скористайтеся порадою: попросіть людину, якій ви довіряєте (бажано юриста) змінити ваш пароль перед від'їздом та надати його вам лише коли ви завершите подорож. Повторіть процедуру на зворотному шляху.

## Подяка

Цей посібник був би неможливий без допомоги багатьох фахівців галузі кібербезпеки в Україні та за кордоном. Щиро вдячний всім, хто зробив внесок у зміст цього документу та пропонував правки та оновлення під час та після його створення. Скомпільовано та підготовлено [Vlad Styran](https://fb.me/vstyran), [BSG](https://bsg.tech), https://styran.com

Special thanks go to Boris "[@jadedsecurity](https://twitter.com/jadedsecurity)" Sverdlik for a great deal of inspiration and coining the "Don't click shit" slogan.

Взяти участь в розробці: https://github.com/sapran/dontclickshit/
