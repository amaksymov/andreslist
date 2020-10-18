# TODO

### Main directions
#### Common:
- __(Completed!)__ Replace nginx on [traefik](https://doc.traefik.io/traefik/)
- Describe project command(like test).
- Add schema with system entities to README.
- Create scripts: init db, run tests, run lint and etc.

#### Backend server:
- Common CRUD for all database entity.

        Create class CRUD for simple inheritance all function while add new entity.
        - add test for all CRUD model
- Add retry connection to db while application startup([tenacity](https://github.com/jd/tenacity)).
- Replace settings(starlette.Config) on pydantic.BaseSettings.
- Add python lint(like flake8, mypy, black, isort, autoflake) and investigate lint alternatives.

#### Frontend client:
- Replace React on Vue.js.
