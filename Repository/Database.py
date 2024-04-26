from typing import Any, Dict, Optional, List
from Config.Connection import prisma_connection

class Database:
    def __init__(self):
        self.client = prisma_connection.prisma

    async def get_one(self, table: str, item_id: int) -> Optional[Dict[str, Any]]:
        return await getattr(self.client, table).find_first(where={"id": item_id})

    async def get_all(self, table: str) -> List[Dict[str, Any]]:
        return await getattr(self.client, table).find_many()

    def update_one(self, table: str, item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if table in self.client.__dict__:
            return self.client.__dict__[table].update(where={"id": item_id}, data=data)

    def delete_one(self, table: str, item_id: int) -> bool:
        if table in self.client.__dict__:
            result = self.client.__dict__[table].delete(where={"id": item_id})
            return True if result else False

    def head_get_one(self, table: str, item_id: int) -> Optional[Dict[str, Any]]:
        if table in self.client.__dict__:
            return self.client.__dict__[table].find_first(
                where={"id": item_id},
                select={"id"}
            )

    def add_item(self, table: str, data: Dict[str, Any]) -> Dict[str, Any]:
        if table in self.client.__dict__:
            return self.client.__dict__[table].create(data=data)
