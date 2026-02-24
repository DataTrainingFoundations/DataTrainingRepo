"""
Pytest configuration and fixtures for database testing.

This module provides shared test fixtures and configuration for all test modules.
"""

import pytest
import os
from sqlalchemy.orm import Session
from database import DatabaseManager
from models import Base


@pytest.fixture(scope="function")
def test_db():
    """
    Create a fresh test database for each test function.
    
    This fixture:
    - Creates a temporary SQLite in-memory database
    - Creates all necessary tables
    - Seeds sample data
    - Yields the database manager for use in tests
    - Cleans up by dropping all tables after each test
    
    Yields:
        DatabaseManager: A database manager configured for testing
    """
    # Use in-memory SQLite database for testing
    test_db_manager = DatabaseManager("sqlite:///:memory:")
    
    # Create all tables
    test_db_manager.create_tables()
    
    # Seed sample data
    test_db_manager.seed_sample_data()
    
    yield test_db_manager
    
    # Cleanup: drop all tables
    test_db_manager.drop_tables()


@pytest.fixture(scope="function")
def test_session(test_db: DatabaseManager) -> Session:
    """
    Get a test database session from the test database.
    
    Args:
        test_db: The test database fixture
    
    Yields:
        A SQLAlchemy Session for database operations
    """
    session = test_db.get_session()
    yield session
    session.close()


@pytest.fixture(scope="function")
def empty_db():
    """
    Create an empty test database (no seed data).
    
    This fixture is useful for tests that need to verify
    creation of entities from scratch.
    
    Yields:
        DatabaseManager: An empty test database manager
    """
    test_db_manager = DatabaseManager("sqlite:///:memory:")
    test_db_manager.create_tables()
    
    yield test_db_manager
    
    test_db_manager.drop_tables()
