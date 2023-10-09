from .request_api import get_feed_hot_list
import textwrap


class Debank:
    @staticmethod
    def get_top_reward(show_top: int = 10):
        api_response = get_feed_hot_list()

        list_of_posts: list = api_response.get("data", {}).get("feeds", [])
        list_of_posts = sorted(
            list_of_posts,
            key=lambda x: float(x.get("article").get("reward_usd_value", 0.0)),
            reverse=True
        )

        list_of_results: list[str] = [f"<b>Топ {show_top} постов по донатам: </b>\n"]
        initial_length_of_the_list = 1

        for post in list_of_posts:
            article = post.get("article", {})
            current = len(list_of_results) - initial_length_of_the_list
            if current >= show_top:
                break
            text = textwrap.shorten(article.get('content', '...'), 22)
            link = f"https://debank.com/stream/{article.get('id', '0')}"
            list_of_results.append(
                f"<code>{str(current+1)+'.':<4}</code> |    "
                f"<code>{str(round(article.get('reward_usd_value'), 1))+'$':<7}</code>  |  "
                f"<a href='{link}'>{text}</a>"
            )

        return "\n".join(list_of_results)
