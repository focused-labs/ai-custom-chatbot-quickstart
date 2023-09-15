from pydantic import BaseModel


class ImportedUrls(BaseModel):
    page_urls: list