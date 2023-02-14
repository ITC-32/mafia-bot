from logging.config import fileConfig

from environs import Env
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from config import BASE_DIR
from models.models import db

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = db
env = Env()
env.read_env(BASE_DIR / ".env")
DATABASE_URL = f"postgresql://{env.str('DB_USER')}:{env.str('PG_PASSWORD')}" \
               f"@{env.str('DB_HOST')}:5432/{env.str('DB_NAME')}"


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    conf = config.get_section(config.config_ini_section)
    conf['sqlalchemy.url'] = DATABASE_URL
    connectable = engine_from_config(
        conf,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
