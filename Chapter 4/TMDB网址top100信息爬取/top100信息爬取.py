import os.path

import requests
from lxml import html
import csv

TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"


def get_movie_info(movie_info_url):
    movie_response = requests.get(movie_info_url, timeout=60)
    movie_doc = html.fromstring(movie_response.text)

    movie_names = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/h2/a/text()")  # 电影名
    # print(movie_names)
    movie_years = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/h2/span/text()")  # 年份
    # print(movie_years)
    movie_dates = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[2]/text()")  # 上映时间
    # print(movie_dates)
    movie_tags = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[3]/a/text()")  # 类型
    # print(movie_tags)
    movie_cost_times = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[4]/text()")  # 时长
    # print(movie_cost_times)
    movie_scores = movie_doc.xpath("//*[@id=\"consensus_pill\"]/div/div[1]/div/div/@data-percent")  # 评分
    # print(movie_scores)
    movie_languages = movie_doc.xpath(
        "//*[@id=\"media_v4\"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")  # 语言
    # print(movie_languages)
    movie_actor = movie_doc.xpath("//*[@id=\"cast_scroller\"]/ol/li[1]/p[1]/a/text()")  # 主演
    # print(movie_actor)
    movie_slogans = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[3]/h3[1]/text()")  # Slogan
    # print(movie_slogans)
    movie_descriptions = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[3]/div/p/text()")  # 简介
    # print(movie_descriptions)

    # 返回电影详情  以字典形式
    movie_info = {
        "电影名": movie_names[0].strip() if movie_names else None,
        "年份": movie_years[0].strip() if movie_years else None,
        "上映时间": movie_dates[0].strip() if movie_dates else None,
        "类型": "|".join(movie_tags) if movie_tags else None,
        "时长": movie_cost_times[0].strip() if movie_cost_times else None,
        "评分": movie_scores[0].strip() if movie_scores else None,
        "语言": movie_languages[0].strip() if movie_languages else None,
        "主演": movie_actor[0].strip() if movie_actor else None,
        "Slogan": movie_slogans[0].strip() if movie_slogans else None,
        "简介": movie_descriptions[0].strip() if movie_descriptions else None,
    }
    # print(movie_info)
    return movie_info


def save_all_movies(all_movies):
    if not os.path.exists("./data"):
        os.makedirs("./data")

    with open("./data/movie_list.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "主演",
                                               "Slogan", "简介"])
        writer.writeheader()
        writer.writerows(all_movies)


def main():
    # 保存所有的电影数据
    all_movies = []

    # 循环获取电影列表(1-5页)
    for page_num in range(1, 6):
        if page_num == 1:
            # 发送请求 获取高分电影榜单数据
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     data=f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-04-16&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&vote_count.lte=&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400&view=&discover_preset=top-rated",
                                     timeout=60)

        # 解析数据 获取电影列表
        document = html.fromstring(response.text)
        movie_list = document.xpath("//*[@class='media-list-results contents']/div")

        # 遍历电影列表 获取电影详情
        for movie in movie_list:
            movie_urls = movie.xpath("./div/div/a/@href")

            if movie_urls:
                # 电影详情的url
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # print(movie_info_url)
                # 发起请求获取电影详细数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)

    save_all_movies(all_movies)


if __name__ == '__main__':
    main()
