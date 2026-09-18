"""Insertar datos iniciales

Revision ID: 256ee9016429
Revises: 4cdd7974b8d2
Create Date: 2026-09-17 09:33:21.073244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '256ee9016429'
down_revision: Union[str, Sequence[str], None] = '4cdd7974b8d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
