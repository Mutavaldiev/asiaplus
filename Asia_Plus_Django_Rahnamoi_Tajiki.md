# 📰 Дастурамали сохтани лоиҳаи Asia Plus дар Django

Ин дастурамал барои сохтани портали хабарии **Asia Plus** ҳамчун лоиҳаи омӯзишӣ пешбинӣ шудааст. Ту бояд лоиҳаро худат нависӣ: дар ин ҷо сохтори кор, номҳои моделҳо, майдонҳо, функсияҳо, URL-ҳо ва маслиҳатҳои зарурӣ оварда шудаанд.

**Ҳадаф:** мавзӯъҳои Django-ро аз сатҳи ибтидоӣ то пешрафта дар як лоиҳаи амалӣ истифода бурдан.

> ⚠️ Ин дастурамал коди пурраи тайёр нест. Намунаҳои код танҳо барои фаҳмидани тарзи навиштананд. Мантиқи асосии ҳар функсияро худат амалӣ кун.

---

## 📌 1. Лоиҳа чӣ имкониятҳо дорад?

Портали хабарии ту бояд чунин қисмҳо дошта бошад:

- Сабти ном бо Email ва тасдиқи рамзи 6-рақама.
- Воридшавӣ ва баромадан аз ҳисоб.
- Профили корбар.
- Хабарҳо, категорияҳо ва барчаспҳо (Tags).
- Илова, таҳрир ва нест кардани хабар.
- Тасдиқ ва нашри хабар аз тарафи муҳаррир.
- Шарҳҳо (Comments) ва назорати онҳо.
- Like ва нигоҳ доштани хабарҳо барои баъд.
- Ҷустуҷӯ (Search), филтр (Filter) ва тартибдиҳӣ (Sorting).
- Саҳифабандӣ (Pagination).
- Django Admin, Users, Groups ва Permissions.
- Панели шахсӣ барои корбарон ва панели корӣ барои кормандон.

---

## 🧱 2. Сохтани Project ва App

Дар Fedora терминалро кушо ва фармонҳоро пайдарпай иҷро кун:

```bash
mkdir asia_plus
cd asia_plus

python3 -m venv .venv
source .venv/bin/activate

pip install django pillow psycopg[binary]

django-admin startproject config .
python manage.py startapp accounts
python manage.py startapp news
python manage.py startapp comments
python manage.py startapp interactions
```

### Сохтори пешбинишудаи лоиҳа

```text
asia_plus/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── news/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── comments/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── interactions/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt
```

**Вазифа:** ҳамаи App-ҳоро соз ва сохтори папкаҳоро санҷ. Ҳоло ба навиштани функсияҳои мураккаб шурӯъ накун.

---

## ⚙️ 3. Танзими `settings.py`

Аввал ҳамаи App-ҳои сохтаатро ба `INSTALLED_APPS` илова кун:

```python
INSTALLED_APPS = [
    # App-ҳои стандартии Django
    'accounts',
    'news',
    'comments',
    'interactions',
]
```

Ин танҳо намунаи ҷойгиркунии App-ҳост. App-ҳои стандартии Django-ро нест накун.

### Танзимотҳое, ки бояд илова ё санҷида шаванд

| Танзимот | Вазифа |
|---|---|
| `AUTH_USER_MODEL` | Муайян кардани модели махсуси корбар |
| `LOGIN_URL` | Суроғаи саҳифаи Login |
| `LOGIN_REDIRECT_URL` | Саҳифа баъди воридшавӣ |
| `LOGOUT_REDIRECT_URL` | Саҳифа баъди баромадан |
| `STATIC_URL` | URL-и файлҳои CSS ва JavaScript |
| `STATICFILES_DIRS` | Ҷойи файлҳои Static дар вақти рушд |
| `MEDIA_URL` | URL-и аксҳо ва файлҳои боршуда |
| `MEDIA_ROOT` | Папкаи нигоҳдории файлҳои боршуда |
| `EMAIL_BACKEND` | Усули фиристодани Email |
| `EMAIL_HOST` | Сервери SMTP |
| `EMAIL_PORT` | Порти SMTP |
| `EMAIL_HOST_USER` | Email-и фиристанда |
| `EMAIL_HOST_PASSWORD` | Пароли SMTP ё App Password |

Барои санҷиши аввалини Email аз Backend-и консолӣ истифода бурда метавонӣ:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Дар ин ҳолат рамз ба Email-и воқеӣ намеравад; он дар терминал нишон дода мешавад. Баъдтар SMTP-ро пайваст кун.

### Муҳим: `AUTH_USER_MODEL`

Агар модели махсуси корбар месозӣ, `AUTH_USER_MODEL`-ро пеш аз иҷрои мигратсияҳои аввал муайян кун. Иваз кардани модели корбар баъди сохтани базаи маълумот метавонад мушкил эҷод кунад.

**Вазифаҳо:**

1. App-ҳоро ба `INSTALLED_APPS` илова кун.
2. `templates`, `static` ва `media`-ро танзим кун.
3. `AUTH_USER_MODEL` ва URL-ҳои воридшавӣ/баромаданро муайян кун.
4. Барои Email аввал Console Backend-ро истифода бар.
5. Танзимоти базаи маълумотро мувофиқи SQLite ё PostgreSQL интихоб кун.

---

## 🗃️ 4. Models — сохтори базаи маълумот

Моделҳо маълумотеро муайян мекунанд, ки дар база нигоҳ дошта мешавад. Барои ин лоиҳа моделҳоро мувофиқи App-ҳо ҷудо кун.

### App: `accounts`

#### Model 1: `CustomUser`

Аз `AbstractUser` истифода бар.

Майдонҳои иловагӣ:

| Майдон | Навъи майдон | Вазифа |
|---|---|---|
| `email` | `EmailField` | Email-и корбар |
| `phone` | `CharField` | Рақами телефон |
| `avatar` | `ImageField` | Акси профил |
| `email_verified` | `BooleanField` | Оё Email тасдиқ шудааст |
| `date_of_birth` | `DateField` | Санаи таваллуд, ихтиёрӣ |

**Вазифа:** модели корбарро соз. Қарор гир, ки Email бояд ягона бошад ё не ва барои воридшавӣ аз username истифода мекунӣ ё Email.

#### Model 2: `EmailVerification`

Майдонҳо:

- `user` — `ForeignKey` ба `CustomUser`.
- `code_hash` — `CharField`, барои нигоҳ доштани хэши рамз.
- `created_at` — `DateTimeField`.
- `expires_at` — `DateTimeField`.
- `attempts` — `IntegerField`.
- `is_used` — `BooleanField`.

**Вазифа:** барои ҳар рамз вақти эътибор, шумораи кӯшишҳо ва ҳолати истифода шуданро нигоҳ дор.

> 🔐 Рамзи тасдиқро беҳтараш дар шакли хэш нигоҳ дор, на ҳамчун матни одӣ. Рамз бояд муҳлати эътибор дошта бошад ва баъди истифода дубора қабул нашавад.

### App: `news`

#### Model 3: `Category`

Майдонҳо:

- `name` — номи категория.
- `slug` — суроғаи кӯтоҳи категория.
- `description` — тавсиф.
- `created_at` — вақти сохтан.

Намунаи категорияҳо: Тоҷикистон, Ҷаҳон, Иқтисод, Варзиш, Технология ва Фарҳанг.

#### Model 4: `Article`

Майдонҳо:

| Майдон | Навъи пешниҳодшуда | Вазифа |
|---|---|---|
| `title` | `CharField` | Сарлавҳаи хабар |
| `slug` | `SlugField` | Суроғаи хабар |
| `short_description` | `TextField` | Хулосаи кӯтоҳ |
| `content` | `TextField` | Матни пурраи хабар |
| `image` | `ImageField` | Акси асосӣ |
| `author` | `ForeignKey` | Муаллифи хабар |
| `category` | `ForeignKey` | Категория |
| `status` | `CharField` | Ҳолати хабар |
| `views_count` | `PositiveIntegerField` | Шумораи тамошо |
| `is_featured` | `BooleanField` | Хабари интихобшуда |
| `created_at` | `DateTimeField` | Вақти сохтан |
| `updated_at` | `DateTimeField` | Вақти тағйир |
| `published_at` | `DateTimeField` | Вақти нашр |

Барои `status` чунин ҳолатҳоро пешбинӣ кун:

```python
DRAFT = 'draft'
PENDING = 'pending'
PUBLISHED = 'published'
```

**Вазифа:** хабар бояд аввал Draft бошад; баъд муаллиф онро барои санҷиш фиристад ва муҳаррир онро нашр кунад. Хабарҳои Draft ва Pending набояд барои хонандаи одӣ намоён бошанд.

#### Model 5: `Tag`

Майдонҳо:

- `name`
- `slug`

Муносибат: байни `Article` ва `Tag` майдони `ManyToManyField` истифода бар. Як хабар метавонад чанд Tag дошта бошад ва як Tag метавонад ба чанд хабар пайваст шавад.

### App: `comments`

#### Model 6: `Comment`

Майдонҳо:

- `user` — корбаре, ки шарҳ навиштааст.
- `article` — хабаре, ки шарҳ ба он тааллуқ дорад.
- `body` — матни шарҳ.
- `created_at` — вақти навиштан.
- `is_approved` — оё шарҳ тасдиқ шудааст.

**Вазифа:** шарҳро танҳо корбари воридшуда навишта тавонад. Пеш аз тасдиқ шарҳро ба ҳамаи хонандагон нишон надеҳ.

### App: `interactions`

#### Model 7: `Like`

Майдонҳо:

- `user`
- `article`
- `created_at`

#### Model 8: `SavedArticle`

Майдонҳо:

- `user`
- `article`
- `created_at`

**Вазифа:** корбар хабарро Like карда тавонад ва барои хондани баъдӣ нигоҳ дорад.

> 💡 Барои `Like` ва `SavedArticle` маҳдудияти `UniqueConstraint` гузор, то як корбар як хабарро ду маротиба Like ё Save карда натавонад.

---

## 🔄 5. Мигратсияҳо ва санҷиши Models

Баъди сохтани моделҳо фармонҳоро иҷро кун:

```bash
python manage.py makemigrations
python manage.py migrate
```

- `makemigrations` — тағйироти моделҳоро ба файлҳои мигратсия табдил медиҳад.
- `migrate` — мигратсияҳоро дар базаи маълумот татбиқ мекунад.

Барои санҷидани моделҳо аз Django Shell истифода бурда метавонӣ:

```bash
python manage.py shell
```

**Вазифаҳо:**

1. Ҳамаи моделҳоро соз.
2. Мигратсияҳоро иҷро кун.
3. Як Category ва як Article-и санҷишӣ илова кун.
4. Муносибатҳои ForeignKey ва ManyToMany-ро санҷ.

---

## 👥 6. Django Admin — Users, Groups ва Permissions

Django Admin барои идора кардани маълумот ва иҷозатҳои корбарон истифода мешавад.

Аввал Superuser соз:

```bash
python manage.py createsuperuser
```

Баъд серверро фаъол карда, ба ин суроға даро:

```text
http://127.0.0.1:8000/admin/
```

Дар Admin се бахши муҳим ҳаст:

- **Users** — идоракунии ҳисобҳои корбарон.
- **Groups** — сохтани гурӯҳҳо ва додани иҷозатҳо ба онҳо.
- **Permissions** — иҷозатҳои амалиётӣ барои моделҳо.

### Гурӯҳҳое, ки бояд созӣ

| Group | Вазифа |
|---|---|
| `Readers` | Хонандагони одӣ |
| `Journalists` | Хабарнигорон |
| `Editors` | Муҳаррирон |
| `Moderators` | Назоратчиёни шарҳҳо |

### Иҷозатҳои стандартии Django

Барои ҳар Model Django одатан чор иҷозат месозад:

| Permission | Маъно |
|---|---|
| `add_model` | Илова кардани объект |
| `view_model` | Дидани объект |
| `change_model` | Тағйир додани объект |
| `delete_model` | Нест кардани объект |

Масалан, барои `Article`:

- `add_article`
- `view_article`
- `change_article`
- `delete_article`

Ин иҷозатҳо баъди иҷрои мигратсияҳо сохта мешаванд.

### Иҷозатҳои пешниҳодшуда барои гурӯҳҳо

| Group | Иҷозатҳои пешниҳодшуда |
|---|---|
| Readers | Дидани хабарҳои нашршуда ва навиштани шарҳ |
| Journalists | Илова, дидан ва таҳрири хабарҳои худ |
| Editors | Дидан, таҳрир ва нашри хабарҳо; идоракунии категорияҳо |
| Moderators | Дидан, тасдиқ ва нест кардани шарҳҳо |

**Вазифа:** гурӯҳҳоро дар Admin соз ва ба ҳар кадом танҳо иҷозатҳои заруриро илова кун. Баъд корбарони санҷишӣ соз ва онҳоро ба гурӯҳҳои гуногун дохил кун.

### Иҷозатҳои махсус (Custom Permissions)

Дар модели `Article` иҷозатҳои махсус эълон кун:

- `can_publish_article` — нашр кардани хабар.
- `can_approve_article` — тасдиқ кардани хабар.
- `can_feature_article` — интихоб кардани хабар ҳамчун муҳим.

Намунаи эълони иҷозат дар дохили `Meta`:

```python
class Meta:
    permissions = [
        ('can_publish_article', 'Метавонад хабарро нашр кунад'),
    ]
```

Ин танҳо эълони иҷозат аст. Барои фаъол шудани он мигратсияҳоро иҷро кун ва дар View санҷиш гузор.

### Санҷиши иҷозат дар FBV

Дар Function-Based View метавонӣ аз `login_required` ва `has_perm()` истифода барӣ:

```python
from django.contrib.auth.decorators import login_required

@login_required
def publish_article(request, pk):
    if request.user.has_perm('news.can_publish_article'):
        # Мантиқи нашри хабарро худат навис
        pass
```

- `login_required` месанҷад, ки корбар ворид шудааст ё не.
- `request.user` корбари ҳозираро медиҳад.
- `has_perm()` месанҷад, ки корбар иҷозати муайян дорад ё не.
- Формати иҷозат: `app_label.codename`, масалан `news.can_publish_article`.

> ⚠️ Пинҳон кардани тугма дар HTML муҳофизат нест. Санҷиши иҷозат бояд дар худи View низ бошад, зеро корбар метавонад URL-ро мустақим кушояд.

---

## 🔐 7. Register ва тасдиқи Email

Дар `accounts/views.py` чунин функсияҳоро соз:

| Функсия | Вазифа |
|---|---|
| `register_view()` | Сабти номи корбар |
| `verify_email_view()` | Санҷидани рамзи Email |
| `resend_code_view()` | Аз нав фиристодани рамз |
| `login_view()` | Воридшавӣ |
| `logout_view()` | Баромадан |
| `profile_view()` | Дидани профил |
| `edit_profile_view()` | Таҳрири профил |
| `change_password_view()` | Иваз кардани парол |
| `user_dashboard()` | Кабинети шахсӣ |

### Тартиби кори Register

1. Корбар ном, Email ва паролро ворид мекунад.
2. Сервер дурустии маълумотро месанҷад.
3. Агар Email аллакай истифода шуда бошад, хатогӣ нишон деҳ.
4. Корбарро соз, вале то тасдиқи Email ҳисобро фаъол насоз.
5. Рамзи тасдиқи 6-рақама соз.
6. Рамзро бо Email фирист.
7. Корбар рамзро ворид мекунад.
8. Рамз, муҳлати эътибор ва шумораи кӯшишҳоро санҷ.
9. Агар рамз дуруст бошад, `email_verified`-ро фаъол кун.

### Form-ҳои зарурӣ

Дар `accounts/forms.py` соз:

- `RegisterForm`
- `EmailVerificationForm`
- `LoginForm`
- `ProfileUpdateForm`
- `PasswordChangeForm`

**Маслиҳатҳои амниятӣ:**

- Паролро ҳеҷ гоҳ худат бо матни одӣ нигоҳ надор; аз механизмҳои Django истифода бар.
- Барои рамзи Email муҳлати эътибор муайян кун.
- Шумораи кӯшишҳои нодурустро маҳдуд кун.
- Барои фиристодани рамзи нав фосилаи вақт пешбинӣ кун.
- Рамзи истифодашударо дубора қабул накун.

---

## 📰 8. Views — функсияҳои асосии лоиҳа

Дар ин лоиҳа аз **FBV (Function-Based Views)** истифода бар: ҳар View функсияи Python мебошад, ки `request`-ро қабул мекунад.

### `news/views.py`

| Номи функсия | Вазифа |
|---|---|
| `home_view()` | Саҳифаи асосӣ |
| `article_list()` | Рӯйхати хабарҳо |
| `article_detail()` | Намоиши як хабар |
| `category_detail()` | Хабарҳои як категория |
| `create_article()` | Сохтани хабар |
| `update_article()` | Таҳрири хабар |
| `delete_article()` | Нест кардани хабар |
| `search_articles()` | Ҷустуҷӯи хабарҳо |
| `filter_articles()` | Филтр кардани хабарҳо |
| `popular_articles()` | Хабарҳои машҳур |
| `latest_articles()` | Хабарҳои навтарин |
| `publish_article()` | Нашр кардани хабар |
| `approve_article()` | Тасдиқи хабар |

### Саволҳои муҳим барои ҳар View

- Оё корбар бояд ворид шуда бошад?
- Оё барои ин амал иҷозати махсус лозим аст?
- Агар объект вуҷуд надошта бошад, чӣ ҷавоб медиҳӣ?
- Агар корбар соҳиби хабар набошад, чӣ мешавад?
- Баъди иҷрои амал корбар ба кадом саҳифа бармегардад?

Барои гирифтани объект бо ҷавоби 404 аз `get_object_or_404()` истифода бурда метавонӣ.

### `comments/views.py`

- `add_comment()` — илова кардани шарҳ.
- `edit_comment()` — таҳрири шарҳ.
- `delete_comment()` — нест кардани шарҳ.
- `approve_comment()` — тасдиқи шарҳ.

### `interactions/views.py`

- `like_article()` — Like кардани хабар.
- `unlike_article()` — бекор кардани Like.
- `save_article()` — нигоҳ доштани хабар.
- `remove_saved_article()` — хориҷ кардани хабар аз рӯйхати нигоҳдошта.
- `saved_articles_list()` — рӯйхати хабарҳои нигоҳдошташуда.

---

## 📝 9. Forms — формаҳо

Формаҳо маълумоти воридкардаи корбарро қабул ва санҷиш мекунанд.

### `accounts/forms.py`

- `RegisterForm`
- `EmailVerificationForm`
- `LoginForm`
- `ProfileUpdateForm`
- `PasswordChangeForm`

### `news/forms.py`

- `ArticleCreateForm`
- `ArticleUpdateForm`
- `CategoryForm`
- `ArticleSearchForm`

### `comments/forms.py`

- `CommentForm`

### Саволи омӯзишӣ

Фарқи `forms.Form` ва `forms.ModelForm` чист?

- `forms.Form` — майдонҳоро худат муайян мекунӣ ва коркарди маълумотро худат менависӣ.
- `forms.ModelForm` — майдонҳои форма аз Model гирифта мешаванд ва барои сохт ё таҳрири объект қулай аст.

**Вазифа:** барои Register ва Search форма соз. Барои сохтани хабар `ModelForm`-ро санҷ.

---

## 🔎 10. Search, Filter ва Sorting

Ҷустуҷӯ бояд аз рӯйи сарлавҳа ва матни хабар кор кунад.

Параметрҳои пешниҳодшуда:

| Параметр | Вазифа |
|---|---|
| `q` | Матни ҷустуҷӯ |
| `category` | Филтр аз рӯйи категория |
| `date_from` | Санаи оғоз |
| `date_to` | Санаи анҷом |
| `author` | Филтр аз рӯйи муаллиф |
| `sort` | Тартибдиҳӣ |

Барои ҷустуҷӯи чанд майдон аз `Q` истифода бурда метавонӣ:

```python
from django.db.models import Q

articles = Article.objects.filter(
    Q(title__icontains=query) |
    Q(content__icontains=query)
)
```

### Вазифаҳои Search ва Filter

1. Ҷустуҷӯ аз рӯйи сарлавҳа.
2. Ҷустуҷӯ аз рӯйи матни хабар.
3. Филтр аз рӯйи категория.
4. Филтр аз рӯйи муаллиф.
5. Филтр аз рӯйи санаи оғоз ва анҷом.
6. Тартибдиҳӣ аз рӯйи навтарин.
7. Тартибдиҳӣ аз рӯйи шумораи тамошо.
8. Якҷоя кор кардани Search ва Filter.

> 💡 Ҳангоми истифодаи якчанд филтр натиҷаҳои навро аз QuerySet-и қаблӣ гир, то филтрҳо якдигарро бекор накунанд.

---

## 📄 11. Pagination — саҳифабандӣ

Агар 100 хабар дошта бошӣ, ҳамаи онҳоро дар як саҳифа нишон додан қулай нест.

Аз `Paginator` истифода бар.

**Вазифаҳо:**

- Дар ҳар саҳифа 10 хабар нишон деҳ.
- Тугмаҳои «Баъдӣ» ва «Қаблӣ» соз.
- Рақами саҳифаи ҷориро нишон деҳ.
- Ҳангоми Search ё Filter гузаштан ба саҳифаи дигар параметрҳоро нигоҳ дор.

---

## 🌐 12. URL-ҳо

Барои ҳар App файли `urls.py` соз ва онро ба `config/urls.py` пайваст кун.

### `accounts/urls.py`

| URL | View |
|---|---|
| `register/` | `register_view` |
| `verify-email/` | `verify_email_view` |
| `resend-code/` | `resend_code_view` |
| `login/` | `login_view` |
| `logout/` | `logout_view` |
| `profile/` | `profile_view` |
| `profile/edit/` | `edit_profile_view` |
| `password/change/` | `change_password_view` |
| `dashboard/` | `user_dashboard` |

### `news/urls.py`

| URL | View |
|---|---|
| `/` | `home_view` |
| `news/` | `article_list` |
| `news/<slug>/` | `article_detail` |
| `category/<slug>/` | `category_detail` |
| `news/create/` | `create_article` |
| `news/<id>/edit/` | `update_article` |
| `news/<id>/delete/` | `delete_article` |
| `search/` | `search_articles` |
| `popular/` | `popular_articles` |
| `latest/` | `latest_articles` |

### `comments/urls.py`

- `article/<id>/comment/`
- `comment/<id>/edit/`
- `comment/<id>/delete/`

### `interactions/urls.py`

- `like/<id>/`
- `save/<id>/`
- `saved/`

**Вазифа:** ҳамаи URL-ҳоро бо `path()` муайян кун ва барои ҳар кадом `name` гузор. Дар Template аз `{% url %}` истифода бар, на аз навиштани суроғаҳои такрорӣ.

---

## 🛡️ 13. Authentication ва Authorization

Ин мафҳумҳоро дар лоиҳа амалӣ кун:

| Мафҳум | Вазифа |
|---|---|
| `AUTH_USER_MODEL` | Модели корбар |
| `LOGIN_URL` | Саҳифаи воридшавӣ |
| `login_required` | Танҳо барои корбари воридшуда |
| `permission_required` | Санҷиши иҷозат |
| `user_passes_test` | Санҷиши шарти худӣ |
| `request.user` | Корбари ҷорӣ |
| `is_authenticated` | Оё корбар ворид шудааст |
| `is_staff` | Иҷозати воридшавӣ ба Admin |
| `is_superuser` | Ҳамаи иҷозатҳои Django |
| `has_perm()` | Санҷидани иҷозати муайян |
| `groups` | Гурӯҳҳои корбар |

Фарқи ин се хусусиятро хуб фаҳм:

- `is_staff` — иҷозати ворид шудан ба Admin медиҳад, аммо худ аз худ ҳамаи иҷозатҳои моделҳоро намедиҳад.
- `is_superuser` — ҳамаи иҷозатҳои Django-ро дорад.
- `is_active` — нишон медиҳад, ки ҳисоб фаъол аст ё не.

**Вазифа:** View-ҳои сохтани хабар, таҳрир, нест кардан, нашр ва идоракунии шарҳҳоро бо санҷишҳои мувофиқ муҳофизат кун.

---

## 🧰 14. Admin.py — идоракунии моделҳо

Ҳамаи моделҳоро дар `admin.py`-и App-и мувофиқ ба Admin пайваст кун.

Барои `Article` имкониятҳои зеринро санҷ:

| Танзимот | Вазифа |
|---|---|
| `list_display` | Майдонҳо дар рӯйхати Admin |
| `list_filter` | Филтр дар Admin |
| `search_fields` | Ҷустуҷӯ дар Admin |
| `list_editable` | Таҳрири зуд аз рӯйхат |
| `prepopulated_fields` | Пур кардани slug аз title |
| `date_hierarchy` | Гурӯҳбандӣ аз рӯйи сана |
| `ordering` | Тартиби намоиши объектҳо |

**Вазифа:** Admin-ро тавре танзим кун, ки муҳаррир тавонад хабарҳоро ҷустуҷӯ, филтр ва таҳрир кунад. Барои шарҳҳо низ имконияти дидан ва тасдиқро илова кун.

---

## 🧠 15. Мавзӯъҳои иловагии Django

Ин мавзӯъҳоро дар қисмҳои гуногуни лоиҳа истифода бар:

| Мавзӯъ | Дар куҷо истифода мешавад |
|---|---|
| `ForeignKey` | Article ва Category |
| `ManyToManyField` | Article ва Tag |
| `OneToOneField` | Агар Profile-ро аз User ҷудо кунӣ |
| `related_name` | Дастрасӣ ба объектҳои вобаста |
| `__str__()` | Номи объект дар Admin |
| `class Meta` | Танзимоти Model |
| `get_object_or_404()` | Гирифтани объект бо 404 |
| `Paginator` | Саҳифабандӣ |
| `Q` | Ҷустуҷӯи чанд майдон |
| `F` | Нав кардани `views_count` бе хондани арзиши кӯҳна |
| `annotate()` | Ҳисоб кардани шумораи Like ё Comment |
| `aggregate()` | Ҳисобҳои умумӣ |
| `select_related()` | Оптимизатсияи ForeignKey |
| `prefetch_related()` | Оптимизатсияи ManyToMany ва муносибатҳои баръакс |
| `messages` | Паёмҳои муваффақият ва хато |
| `transaction.atomic()` | Амалиёти якҷояи база |
| `signals` | Амалҳои автоматӣ |
| `ModelForm` | Форма аз Model |
| `ImageField` | Бор кардани акс |
| `FileField` | Бор кардани файл |

---

## 🧪 16. Санҷиши лоиҳа

Пеш аз анҷом додан ин ҳолатҳоро санҷ:

1. Корбари нав метавонад сабти ном шавад.
2. Email-и тасдиқнашуда ба қисмҳои муҳофизатшуда роҳ надорад.
3. Рамзи нодуруст қабул намешавад.
4. Рамзи муҳлаташ гузашта қабул намешавад.
5. Хабарнигор метавонад хабар илова кунад.
6. Хабарнигор наметавонад хабарро бе иҷозат нашр кунад.
7. Муҳаррир метавонад хабарро тасдиқ ва нашр кунад.
8. Хонандаи одӣ хабарҳои нашрнашударо намебинад.
9. Корбар наметавонад шарҳи корбари дигарро таҳрир кунад.
10. Like ва Save такрорӣ намешаванд.
11. Search ва Filter якҷоя кор мекунанд.
12. Pagination дуруст кор мекунад.

Барои санҷиш беҳтар аст аз корбарони одӣ истифода барӣ, на танҳо аз Superuser. Superuser ҳамаи иҷозатҳоро дорад ва санҷиши маҳдудиятҳо бо ӯ натиҷаи воқеӣ намедиҳад.

---

## 📚 17. Марҳилаҳои супориши хонагӣ

Ҳар марҳиларо пурра иҷро кун ва баъд ба марҳилаи дигар гузар.

### Марҳилаи 1 — Project ва App

- [ ] Папкаи `asia_plus` соз.
- [ ] Virtual environment соз ва фаъол кун.
- [ ] Django ва Pillow насб кун.
- [ ] Project бо номи `config` соз.
- [ ] App-ҳои `accounts`, `news`, `comments`, `interactions` соз.
- [ ] App-ҳоро ба `INSTALLED_APPS` илова кун.
- [ ] URL-ҳои асосиро пайваст кун.

### Марҳилаи 2 — Models

- [ ] `CustomUser` соз.
- [ ] `EmailVerification` соз.
- [ ] `Category` ва `Article` соз.
- [ ] `Tag` соз ва ManyToMany-ро пайваст кун.
- [ ] `Comment` соз.
- [ ] `Like` ва `SavedArticle` соз.
- [ ] Мигратсияҳоро иҷро ва моделҳоро санҷ.

### Марҳилаи 3 — Admin ва Permissions

- [ ] Superuser соз.
- [ ] Ҳамаи моделҳоро ба Admin пайваст кун.
- [ ] Group-ҳои Readers, Journalists, Editors ва Moderators соз.
- [ ] Иҷозатҳои ҳар гурӯҳро муайян кун.
- [ ] Custom Permissions илова кун.
- [ ] Бо корбарони гуногун санҷ.

### Марҳилаи 4 — Authentication

- [ ] Register соз.
- [ ] Тасдиқи Email соз.
- [ ] Фиристодани рамзи навро амалӣ кун.
- [ ] Login ва Logout соз.
- [ ] Profile ва Edit Profile соз.
- [ ] Change Password соз.
- [ ] Саҳифаҳои заруриро муҳофизат кун.

### Марҳилаи 5 — News CRUD

- [ ] Рӯйхати хабарҳоро нишон деҳ.
- [ ] Саҳифаи тафсилоти хабар соз.
- [ ] Сохтани хабарро амалӣ кун.
- [ ] Таҳрири хабарро амалӣ кун.
- [ ] Нест кардани хабарро амалӣ кун.
- [ ] Тасдиқ ва нашри хабарро амалӣ кун.

### Марҳилаи 6 — Search ва Filter

- [ ] Search бо `Q` соз.
- [ ] Filter аз рӯйи Category соз.
- [ ] Filter аз рӯйи Date соз.
- [ ] Filter аз рӯйи Author соз.
- [ ] Sorting аз рӯйи сана ва тамошо соз.
- [ ] Pagination илова кун.

### Марҳилаи 7 — Функсияҳои пешрафта

- [ ] Comments соз.
- [ ] Тасдиқи шарҳҳоро соз.
- [ ] Like ва Unlike соз.
- [ ] Saved Articles соз.
- [ ] Permissions-ро дар FBV санҷ.
- [ ] Messages ва Signals-ро истифода бар.
- [ ] QuerySet-ҳоро оптимизатсия кун.
- [ ] Санҷишҳо навис ва лоиҳаро ба GitHub фирист.

---

## 🚀 18. Аз куҷо оғоз мекунем?

Мо метавонем лоиҳаро марҳила ба марҳила созем:

1. Ту вазифаро иҷро мекунӣ ва кодро худат менависӣ.
2. Натиҷаи терминал ё коди навиштаатро мефиристӣ.
3. Ман хатоҳоро мефаҳмонам ва роҳнамоӣ мекунам.
4. Вақте марҳила дуруст шуд, ба вазифаи навбатӣ мегузарем.

### Вазифаи аввал

**Марҳилаи 1 — Project ва App**

Ҳоло танҳо ин корҳоро иҷро кун:

1. Папкаи `asia_plus` соз.
2. Virtual environment соз ва фаъол кун.
3. Django насб кун.
4. Project бо номи `config` соз.
5. App-ҳои `accounts`, `news`, `comments`, `interactions` соз.

Баъд сохтори папкаҳо ё натиҷаи терминалро фирист. Пас аз санҷиш ба марҳилаи Models мегузарем.
