# STEM Diverse TV

[![project chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://anitab-org.zulipchat.com/#narrow/stream/225705-STEM-diverse-tv)
[![project chat](https://img.shields.io/badge/Docusauras%20-2.0.0--alpha.72-brightgreen)](https://anitab-org.github.io/stem-diverse-tv/)
[![Javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://anitab-org.github.io/stem-diverse-tv/)
[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://anitab-org.github.io/stem-diverse-tv/)
[![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)](https://anitab-org.github.io/stem-diverse-tv/)

STEM Diverse TV is a project which gather and provide inspiring, motivating, informative, educational and supportive videos about diversity in STEM. This is the backend of the project. Documentation of the project is hosted [here](https://anitab-org.github.io/stem-diverse-tv/)

## Setup and run

To setup the project locally follow the instructions:

Please make a virtual environment and run the following commands.

```
virtualenv venv --python=python3
source ./venv/bin/activate
pip3 install -r requirements.txt
```

- Please download Firebase Admin SDK service json file from Firebase Console, You can download the file by following below steps:
  1.  Go to `Project Settings/Service accounts`
  2.  Click on `Generate New Primary Key`
  3.  Place the file in project's root directory and rename it to `google-credentials.json`
- Make .env file from given .env.template file and add details like API_KEY, which is a web api key from firebase. Find your project's web api key in project's overview tab on firebase console.

Use .env.template file to make a new .env file and add the following details:

```
API_KEY=<firebase-project-web-api-key>
EMAIL_USER=<Email-Address>
EMAIL_PASS=<Password>

```

After this, execute:

```
python run.py
```

or

```
python3 run.py
```

**Database setup:**

1. if you take a look into `.env.template` you will see that there are multiple config environments (the easiest for the use is local, no database setup)
2. for the ones where the database is necessary, you will need to provide the DB details in the `.env` file

PostgreSQL is the database that we are going to use in the deployed version. Here is the script that will help you create the Postgres user and and database. Of course. you need to have PostgreSQL
installed on your local machine.

```
# CREATEDB for the privilege to create it's own DB
CREATE USER <stem_diverse> WITH PASSWORD 'examplepassword' CREATEDB;

CREATE DATABASE <database_name> WITH OWNER <stem_diverse> ENCODING 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
```

#### Fork

_**Note**_: _This is only needed if you want to contribute to the project._

If you want to contribute to the project you will have to create your own copy of the project on GitHub. You can do this by clicking the Fork button that can be found on the top right corner of the [landing page](https://github.com/anitab-org/stem-diverse-tv) of the repository.

#### Clone

_**Note**_: _For this you need to install git on your machine. You can download the git tool from [here](https://git-scm.com/downloads)._

- If you have forked the project, run the following command -

  `git clone https://github.com/YOUR_GITHUB_USER_NAME/stem-diverse-tv`

  where `YOUR_GITHUB_USER_NAME` is your GitHub handle.

- If you haven't forked the project, run the following command -

  `git clone https://github.com/anitab-org/stem-diverse-tv`

- Now after you cloned the repository, move to stem-diverse-tv directory by -

  `cd stem-diverse-tv`

#### Remote

_**Note**_: _This is only needed if you want to contribute to the project._

When a repository is cloned, it has a default remote named `origin` that points to your fork on GitHub, not the original repository it was forked from. To keep track of the original repository, you should add another remote named upstream. For this project it can be done by running the following command -

`git remote add upstream https://github.com/anitab-org/stem-diverse-tv`

You can check that the previous command worked by running `git remote -v`. You should see the following output:

```
$ git remote -v
origin  https://github.com/YOUR_GITHUB_USER_NAME/stem-diverse-tv (fetch)
origin  https://github.com/YOUR_GITHUB_USER_NAME/stem-diverse-tv (push)
upstream        https://github.com/anitab-org/stem-diverse-tv (fetch)
upstream        https://github.com/anitab-org/stem-diverse-tv (push)
```

### Run tests

To run the unitests run the following command in the terminal (while the virtual environment is activated):

```
python -m unittest discover tests
```

### Auto-formatting with black

We use [_Black_](https://github.com/psf/black) to format code automatically so that we don't have to worry about clean and
readable code. To install _Black_:

```
pip install black
```

To run black:

```
black .
```

## YouTube Data API Enabling

**Steps**

1. You need a [Google Account](https://www.google.com/accounts/NewAccount) to access the Google API Console, request an API key, and register your application.
2. Create a project in the [Google Developers Console](https://console.developers.google.com/) and [obtain authorization credentials](https://developers.google.com/youtube/registering_an_application) so your application can submit API requests.

3. After creating your project, make sure the YouTube Data API is one of the services that your application is registered to use:

- Go to the [API Console](https://console.developers.google.com/) and select the project that you just registered.
- Visit the [Enabled APIs page](https://console.developers.google.com/apis/enabled). In the list of APIs, make sure the status is ON for the YouTube Data API v3

## Contributing

**This project is under active development**

Please read our [Contributing Guidelines](docs/contributing_guidelines.md), [Code of Conduct](docs/code_of_conduct.md) and [Reporting Guidelines](docs/reporting_guidelines.md) thoroughly.

### Contributors

Thanks goes to these people ([emoji key](https://github.com/all-contributors/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/annabauza"><img src="https://avatars.githubusercontent.com/u/31966073?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Anna Bauza</b></sub></a><br /><a href="https://github.com/anitab-org/stem-diverse-tv/commits?author=annabauza" title="Code">💻</a> <a href="#maintenance-annabauza" title="Maintenance">🚧</a> <a href="https://github.com/anitab-org/stem-diverse-tv/commits?author=annabauza" title="Tests">⚠️</a> <a href="https://github.com/anitab-org/stem-diverse-tv/commits?author=annabauza" title="Documentation">📖</a> <a href="#design-annabauza" title="Design">🎨</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.
Contributions of any kind welcome!

## Contact

If you have any questions or want to discuss something about this repo, feel free to reach out to our team on our Zulip channel [#Design-team](https://anitab-org.zulipchat.com/#narrow/stream/216323-design/topic/STEM.20Diverse.20TV). If you are a new contributor, head over to this project's stream (https://anitab-org.zulipchat.com/#narrow/stream/225705-STEM-diverse-tv) on Zulip to see ongoing discussions.

## License

The project is licensed under the GNU General Public License v3.0. Learn more about it in the [LICENSE](LICENSE) file.
