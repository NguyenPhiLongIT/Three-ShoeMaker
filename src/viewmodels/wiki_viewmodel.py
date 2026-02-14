from src.models.wiki_model import get_all_wiki, get_wiki_by_id

class WikiViewModel:
    def __init__(self):
        self.wiki_list = []
    
    def get_all_summaries(self):
        """Return only ID, Title, Image, Tags for list view."""
        self.wiki_list = get_all_wiki()
        return [
            {
                'id': wiki['id'],
                'title': wiki['title'],
                'image_path': wiki['image_path'],
                'tags': wiki['tags'].split(',') if wiki['tags'] else []
            }
            for wiki in self.wiki_list
        ]
    
    def get_article_detail(self, article_id):
        """Return full article content by ID."""
        article = get_wiki_by_id(article_id)
        if not article:
            return None
        return {
            'id': article['id'],
            'title': article['title'],
            'content': article['content'],
            'image_path': article['image_path'],
            'tags': article['tags'].split(',') if article['tags'] else []
        }
