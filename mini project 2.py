class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\n"


class CMS:
    def __init__(self):
        self.articles = {}

    def add_article(self, title, content):
        if title in self.articles:
            print("Article with this title already exists.")
        else:
            self.articles[title] = Article(title, content)
            print(f"Article '{title}' added.")

    def view_articles(self):
        if not self.articles:
            print("No articles found.")
            return
        print("\nArticles:")
        for article in self.articles.values():
            print(article)

    def edit_article(self, title, new_content):
        if title in self.articles:
            self.articles[title].content = new_content
            print(f"Article '{title}' updated.")
        else:
            print("Article not found.")

    def delete_article(self, title):
        if title in self.articles:
            del self.articles[title]
            print(f"Article '{title}' deleted.")
        else:
            print("Article not found.")


def main():
    cms = CMS()
    while True:
        print("\nCustom Content Management System")
        print("1. Add Article")
        print("2. View Articles")
        print("3. Edit Article")
        print("4. Delete Article")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter article title: ")
            content = input("Enter article content: ")
            cms.add_article(title, content)
        elif choice == "2":
            cms.view_articles()
        elif choice == "3":
            title = input("Enter the title of the article to edit: ")
            new_content = input("Enter the new content: ")
            cms.edit_article(title, new_content)
        elif choice == "4":
            title = input("Enter the title of the article to delete: ")
            cms.delete_article(title)
        elif choice == "5":
            print("Exiting Content Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
