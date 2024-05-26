# Base Plugin App for Alliance Auth<a name="base-plugin-app-for-alliance-auth"></a>

Swashmans base plugin for Alliance Auth that can be used as a starting point to develop custom plugins.

### Cloning From Repo<a name="cloning-from-repo"></a>

Just cd into the top folder (e.g. aa-dev) and clone the repo.

```bash
git clone https://github.com/swashman/aa-base-plugin.git aa-your-app-name
cd aa-your-app-name
rm -rf .git
git init
pre-commit install
```

### Renaming the App<a name="renaming-the-app"></a>

Here is an overview of the places that you need to edit to adopt the name.

Easiest is to just find & replace `example` with your new app name in all files
listed below.

| Location                                 | Description                                                                            |
| ---------------------------------------- | -------------------------------------------------------------------------------------- |
| `./example/`                             | Folder name                                                                            |
| `./example/static/example/`              | Folder name                                                                            |
| `./example/templates/example/`           | Folder name                                                                            |
| `./pyproject.cfg`                        | Update module name for version import, update package name, update title, author, etc. |
| `./example/apps.py`                      | App name                                                                               |
| `./example/__init__.py`                  | App name                                                                               |
| `./example/auth_hooks.py`                | Menu hook config incl. icon and label of your app's menu item appearing in the sidebar |
| `./example/models.py`                    | App name                                                                               |
| `./example/urls.py`                      | App name                                                                               |
| `./example/views.py`                     | Permission name and template path                                                      |
| `./example/templates/example/base.html`  | Title of your app to be shown in all views and as title in the browser tab             |
| `./example/templates/example/index.html` | Template path                                                                          |
| `./testauth/local.py`                    | App name in `PACKAGE` constant                                                         |
| `./.coveragerc`                          | App name                                                                               |
| `./MANIFEST.in`                          | App name                                                                               |
| `./README.md`                            | Clear content                                                                          |
| `./LICENSE`                              | Replace with your own license                                                          |
| `./tox.ini`                              | App name                                                                               |
| `./.isort.cfg`                           | App name for `import_heading_firstparty`                                               |
| `./Makefile`                             | App name and package name                                                              |

## Installing Into Your Dev AA<a name="installing-into-your-dev-aa"></a>

Make sure you're in your venv. Then install it with pip in editable mode:

```bash
pip install -e aa-your-app-name
```

First add your app to the Django project by adding the name of your app to
INSTALLED_APPS in `settings/local.py`.

Next, we will create new migrations for your app:

```bash
python manage.py makemigrations
```

Then run a check to see if everything is set up correctly.

```bash
python manage.py check
```

In case they're errors make sure to fix them before proceeding.

Next, perform migrations to add your model to the database:

```bash
python manage.py migrate
```

Finally, restart your AA server and that's it.

## DELETE EVERYTHING ABOVE HERE<a name="delete-everything-above-here"></a>

# Base Plugin App<a name="base-plugin-app"></a>

Description of app

![License](https://img.shields.io/badge/license-GPLv3-green)
![python](https://img.shields.io/badge/python-3.8-informational)
![django](https://img.shields.io/badge/django-3.2-informational)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

_(These badges are examples, you can and should replace them with your own)_

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [Base Plugin App for Alliance Auth](#base-plugin-app-for-alliance-auth)
  - [Cloning From Repo](#cloning-from-repo)
  - [Renaming the App](#renaming-the-app)
  - [Installing Into Your Dev AA](#installing-into-your-dev-aa)
  - [DELETE EVERYTHING ABOVE HERE](#delete-everything-above-here)
- [Base Plugin App](#base-plugin-app)
  - [Installing into production AA](#installing-into-production-aa)
  - [Optional Settings](#optional-settings)
  - [Permissions](#permissions)

<!-- mdformat-toc end -->

## Installing into production AA<a name="installing-into-production-aa"></a>

To install your plugin into a production AA run this command within the virtual Python environment of your AA installation:

```bash
pip install git+https://github.com/swashman/base_plugin
```

- Add `'base_plugin',` to `INSTALLED_APPS` in `settings/local.py`
- add the following settings to `settings/local.py`

```python
## base plugin SETTINGS
SOME_SETTING = "setting"
```

- run migrations
- restart your allianceserver.

## Optional Settings<a name="optional-settings"></a>

| Setting            | Default | Description                          |
| :----------------- | :------ | :----------------------------------- |
| `OPTIONAL_SETTING` | `True`  | some optional setting does something |

## Permissions<a name="permissions"></a>

| ID             | Description           | Notes                   |
| :------------- | :-------------------- | :---------------------- |
| `basic_access` | Can access the module | basic access permission |
