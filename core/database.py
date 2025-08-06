from typing import Union, Optional, Any

import psycopg2
from psycopg2.extras import DictRow, DictCursor

from core.config import DB_CONFIG


class DatabaseManager:
    """
    A context manager for handling PostgreSQL database connections.

    Provides automatic connection management with proper cleanup and transaction handling.
    Uses DictCursor to return results as dictionary-like objects for easier column access.
    """

    def __init__(self):
        """Initialize the database manager with None values for connection and cursor."""
        self.conn: Optional[psycopg2.extensions.connection] = None
        self.cursor: Optional[psycopg2.extensions.cursor] = None

    def __enter__(self) -> "DatabaseManager":
        """
        Context manager entry point.

        Establishes database connection and creates a cursor with DictCursor factory
        for dictionary-style result access.

        Returns:
            DatabaseManager: Self instance for method chaining
        """
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(cursor_factory=DictCursor)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit point.

        Handles transaction cleanup - rolls back on exceptions, commits on success.
        Ensures proper cleanup of database resources.

        Args:
            exc_type: Exception type if an exception occurred
            exc_val: Exception value if an exception occurred
            exc_tb: Exception traceback if an exception occurred
        """
        # Roll back transaction if an exception occurred
        if exc_type:
            self.conn.rollback()
        else:
            # Commit transaction if no exceptions
            self.conn.commit()

        # Close connection and cursor to free resources
        if self.conn:
            self.conn.close()

        if self.cursor:
            self.cursor.close()

    def execute(self, query: str, params: Union[tuple, dict, None] = None):
        """
        Execute a SQL query without returning results.

        Typically used for INSERT, UPDATE, DELETE operations.

        Args:
            query: SQL query string to execute
            params: Query parameters for safe parameterized queries
        """
        self.cursor.execute(query, params)

    def fetchone(self, query: str, params: Union[tuple, dict, None] = None) -> Optional[DictRow]:
        """
        Execute a query and return a single result row.

        Args:
            query: SQL query string to execute
            params: Query parameters for safe parameterized queries

        Returns:
            Optional[DictRow]: Single row as dictionary-like object, or None if no results
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query: str, params: Union[tuple, dict, None] = None) -> list[tuple[Any, ...]]:
        """
        Execute a query and return all result rows.

        Args:
            query: SQL query string to execute
            params: Query parameters for safe parameterized queries

        Returns:
            list[tuple[Any, ...]]: List of all rows from the query result
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()


def execute_query(
        query: str,
        params: Union[tuple, dict, None] = None,
        fetch: Union[str, None] = None
) -> DictRow | None | list[tuple[Any, ...]]:
    """
    Convenience function for executing database queries with automatic connection management.

    This function wraps the DatabaseManager context manager to provide a simple interface
    for common database operations without manual connection handling.

    Args:
        query: SQL query string to execute
        params: Query parameters for safe parameterized queries (tuple or dict)
        fetch: Determines return behavior:
               - "one": Returns single row using fetchone()
               - "all": Returns all rows using fetchall()
               - None: Executes query without returning results (for INSERT/UPDATE/DELETE)

    Returns:
        DictRow | None | list[tuple[Any, ...]]:
        - DictRow for fetch="one" with results, None if no results
        - list of tuples for fetch="all"
        - None for fetch=None or on error

    Example:
        # Insert data
        execute_query("INSERT INTO users (name) VALUES (%s)", ("John",))

        # Get single user
        user = execute_query("SELECT * FROM users WHERE id = %s", (1,), fetch="one")

        # Get all users
        users = execute_query("SELECT * FROM users", fetch="all")
    """
    try:
        # Use context manager for automatic connection handling
        with DatabaseManager() as db:
            if fetch == "one":
                return db.fetchone(query=query, params=params)
            elif fetch == "all":
                return db.fetchall(query=query, params=params)
            else:
                # Execute without fetching results (INSERT/UPDATE/DELETE)
                db.execute(query=query, params=params)
                return None
    except psycopg2.Error as e:
        # Log database errors and return None to indicate failure
        print(e)
        return None