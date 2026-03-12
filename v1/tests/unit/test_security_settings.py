
import pytest
from src.config.settings import Settings, validate_settings

def test_security_settings_defaults():
    """Verify that current defaults for allowed_hosts and cors_origins are secure (empty)."""
    settings = Settings(secret_key="test-secret-key")

    # These should now be secure defaults
    assert settings.allowed_hosts == []
    assert settings.cors_origins == []

def test_validate_settings_production_insecure():
    """Verify that validate_settings still identifies insecure configurations in production."""
    settings = Settings(
        environment="production",
        secret_key="test-secret-key",
        database_url="postgresql://user:pass@host:5432/db",
        allowed_hosts=["*"],
        cors_origins=["*"]
    )

    issues = validate_settings(settings)

    assert "Allowed hosts should be restricted in production" in issues
    assert "CORS origins should be restricted in production" in issues

def test_validate_settings_production_secure():
    """Verify that validate_settings does not complain about specific hosts/origins."""
    settings = Settings(
        environment="production",
        secret_key="test-secret-key",
        database_url="postgresql://user:pass@host:5432/db",
        allowed_hosts=["api.example.com"],
        cors_origins=["https://dashboard.example.com"]
    )

    issues = validate_settings(settings)

    assert "Allowed hosts should be restricted in production" not in issues
    assert "CORS origins should be restricted in production" not in issues
