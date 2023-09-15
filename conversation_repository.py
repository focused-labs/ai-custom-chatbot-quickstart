from fastapi import Depends

from database import get_db
from models.conversation import Conversation


def create_conversation(db: Depends(get_db()), conversation: Conversation):
    db.add(conversation)
    db.commit()
