# README #
1. This is a sample application with basic functionality for the purposes of assessing technical candidates only.
2. Do not be overly concerned if there is code in this application which does not appear to do anything or is imperfect. Just focus on the task below.
3. Don't spend more than 2 hours in total on installation and these tasks. It is ok if you do not get to everything.
4. Write your code as if you were a team member working on a joint codebase with other developers.

### Setup ###
1. Setup for a new python project as normal, eg virtualenv, install requirements.txt, etc. / done
2. Update your config file at config/my_development.cnf / done
3. Create your own MySQL databases with the same names as in my_development.cnf.template /done
4. Import config/seed.sql into your database /done
5. You need to have a local redis server running with `redis-server` / done
6. Migrate to the latest version of the database with `alembic upgrade head`.
7. Create my_test.cnf and repeat to create a test database to use for unit tests.
8. Do not commit either of your config files to the git repo.


### Checkpoint ###
1. Before proceeding further, ensure that you can:
    * see 3 rows in the user table in your database /done
    * Start the app with `python app_test.py` /done
    * The page at /dashboard is now visible and welcomes you to the task. This page will automatically log you in as user 1. / done
    * You can run unit tests with `py.test tests` and see 2 tests passing.

## Your Task ##
1. Change the username displayed in the top right corner of the page
    * Instead of "Chuck Norris", it should show the user's email /done

2. Write a migration to increase the point_balance for user 2 to 1000, and the tier for user 3 to Bronze /done

3. Add a new route at /community /done
    * Add this as a dropdown option in the top right corner of the page, below "Dashboard"
    * List the 5 most recent users (most recently signed up user first), with columns for user's tier, point_balance, display_name, and phone number.
    * Assume we want this query to be fast, so use a raw MySQL query rather than any built-in ORM methods.
    * Some users may have more than 1 phone number, each phone number should be displayed on a separate line.
    * This table of users should be bordered and striped (ie alternate rows and with grey and white stripes)
    * For each user, make the display_name clickable. Clicking this link should open a modal which shows the user's location.

4. Add any unit tests you think is appropriate.

## Assessment Criteria ##
1. Ability to handle ambiguous requirements.
2. Python ability
3. MySQL
4. CSS and Javascript
5. Development practices / code organization