from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Модифікуйте цей шлях, щоб він вказував на ваш файл alembic.ini
config = context.config
fileConfig(config.config_file_name, disable_existing_loggers=False)

# Ця опція зчитує параметри підключення з alembic.ini
target_metadata = None

def run_migrations_offline():
    """For 'offline' mode."""

    # Не використовуйте зовнішній з'єднання з базою даних
    # engine = engine_from_config(
    #     config.get_section(config.config_ini_section),
    #     prefix='sqlalchemy.',
    #     poolclass=pool.NullPool,
    # )

    # Для SQLite:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """For 'online' mode."""

    # Застосуйте опції з alembic.ini до метаданих SQLAlchemy
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()
