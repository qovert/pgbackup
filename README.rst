pgbackup
========

CLI for backing up remote PostgreSQL dbs

Preparing the development
-------------------------

1. Ensure using ``pip`` and ``pipenv`` are installed.
2. Clone repo ``git clone git@github.com:qovert/pgbackup``
3. ``cd`` into the repo dir.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver, and the destination.

S3 Example w/bucket name:

::
    $ pgbackup postgres://test@example.com:5432/db_one --driver s3 backups

Local Example w/local path:

::

    $ pgbackup postgres://test@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active use:

::

    $ pipenv run make


