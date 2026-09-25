import phpkb_update_articles as publisher


class _MetadataCursor:
    def __init__(self):
        self.query = ""

    def execute(self, query):
        self.query = query

    def fetchone(self):
        return "Методы System Core API", "API, REST", 0


class _MetadataConnection:
    def __init__(self):
        self.cursor_instance = _MetadataCursor()

    def cursor(self):
        return self.cursor_instance


def test_update_article_does_not_load_existing_content(monkeypatch):
    connection = _MetadataConnection()
    monkeypatch.setattr(publisher, "CONNECTION", connection)
    monkeypatch.setattr(publisher, "getArticleContentById", lambda _article_id: None)

    assert publisher.updateArticle(5331) is False
    assert "article_content" not in connection.cursor_instance.query.lower()
