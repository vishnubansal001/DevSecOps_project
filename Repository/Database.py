from typing import Any, Dict, Optional, List
from Config.Connection import prisma_connection

class Database:
    def __init__(self):
        self.client = prisma_connection.prisma

    async def get_one(self, table: str, item_id: int) -> Optional[Dict[str, Any]]:
        return await getattr(self.client, table).find_first(where={"id": item_id})

    async def get_all(self, table: str) -> List[Dict[str, Any]]:
        return await getattr(self.client, table).find_many()

    async def update_one(self, table: str, item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        return await getattr(self.client, table).update(where={"id": item_id}, data=data)

    async def delete_one(self, table: str, item_id: int) -> bool:
        return await getattr(self.client, table).delete(where={"id": item_id})

    async def add_item(self, table: str, data: Dict[str,str]) -> Dict[str, Any]:
        return await getattr(self.client, table).create(data=data)
