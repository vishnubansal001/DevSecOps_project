from Model.release import CreateRelease,RetrieveRelease
from Repository.Database import Database
from fastapi import HTTPException


class ReleaseService(Database):
    def __init__(self):
        super().__init__()

    async def get_releases(self):
        return await self.get_all("release")

    async def get_release(self,identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("release", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, release: CreateRelease):
        if release is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("metalEnvironment", release.metalEnvironment)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("release", release.dict())

    async def update(self,release: RetrieveRelease):
        if release is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("release", release.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("metalEnvironment", release.metalEnvironment)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("release", release.identifier, release.dict())
    
    async def delete(self,identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("release", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("release", identifier)