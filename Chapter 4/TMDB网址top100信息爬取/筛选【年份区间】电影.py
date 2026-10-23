import os.path
import requests
from lxml import html
import csv
import bisect       # 内置模块  专门用来在 有序列表 上做二分查找
import re

TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"


def get_movie_info(movie_info_url):
    movie_response = requests.get(movie_info_url, timeout=60)
    movie_doc = html.fromstring(movie_response.text)

    movie_names = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/h2/a/text()")  # 电影名
    movie_years = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/h2/span/text()")  # 年份
    movie_dates = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[2]/text()")  # 上映时间
    movie_tags = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[3]/a/text()")  # 类型
    movie_cost_times = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[4]/text()")  # 时长
    movie_scores = movie_doc.xpath("//*[@id=\"consensus_pill\"]/div/div[1]/div/div/@data-percent")  # 评分
    movie_languages = movie_doc.xpath(
        "//*[@id=\"media_v4\"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")  # 语言
    movie_actor = movie_doc.xpath("//*[@id=\"cast_scroller\"]/ol/li[1]/p[1]/a/text()")  # 主演
    movie_slogans = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[3]/h3[1]/text()")  # Slogan
    movie_descriptions = movie_doc.xpath("//*[@id=\"original_header\"]/div[2]/section/div[3]/div/p/text()")  # 简介

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
    return movie_info


def save_all_movies(all_movies):
    if not os.path.exists("./data"):
        os.makedirs("./data")

    with open("./data/movie_list.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "主演",
                                               "Slogan", "简介"])
        writer.writeheader()
        writer.writerows(all_movies)


# ========== 新增：二分查找筛选年份区间函数 ==========
def filter_movie_by_year_bisect(all_movies, start_year, end_year):
    # 1.清洗年份，提取数字，构造 (年份数字, 电影字典)，过滤掉年份为空的数据
    movie_with_year = []
    for movie in all_movies:
        year_str = movie["年份"]
        if year_str is None:
            continue
        # 正则提取数字，去掉括号，例如 "(2010)" -> 2010
        res = re.search(r"\d{4}", year_str)
        if res:
            year_num = int(res.group())         # 拿到 用正则去掉括号的年份
            movie_with_year.append((year_num, movie))

    # 2.按年份升序排序（二分必须有序）
    movie_with_year.sort(key=lambda x: x[0])        # 按年份进行排序
    year_list = [item[0] for item in movie_with_year]       # 推导式  获取年份信息

    # 3.bisect二分查找左右边界
    left_idx = bisect.bisect_left(year_list, start_year)        # 第一个 >=2020  获取到对应的下标
    right_idx = bisect.bisect_right(year_list, end_year)        # 第一个 >2026  获取到对应的下标    没有有2027所有取到列表最后一位(包含) 结果为len(year_list)

    # 4.切片取出区间内电影
    selected = movie_with_year[left_idx:right_idx]
    result_movies = [item[1] for item in selected]
    return result_movies


def main():
    all_movies = []

    # 循环获取电影列表(1-5页)
    for page_num in range(1, 6):
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     data=f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-04-16&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&vote_count.lte=&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400&view=&discover_preset=top-rated",
                                     timeout=60)

        document = html.fromstring(response.text)
        movie_list = document.xpath("//*[@class='media-list-results contents']/div")

        for movie in movie_list:
            movie_urls = movie.xpath("./div/div/a/@href")
            if movie_urls:
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)

    # 保存全部电影到csv
    save_all_movies(all_movies)
    print(f"全部爬取完成，一共 {len(all_movies)} 部电影")

    # ========== 调用二分筛选：设置年份区间 ==========
    start = 2020
    end = 2026
    filter_result = filter_movie_by_year_bisect(all_movies, start, end)
    print(f"\n==== 使用二分查找筛选 {start}-{end} 年电影 ====")
    print(f"符合条件电影数量：{len(filter_result)}")
    for m in filter_result:
        print(f"{m['电影名']} | {m['年份']}")

    # 可选：把筛选结果单独保存成新csv
    with open("./data/filter_movie.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "主演",
                                               "Slogan", "简介"])
        writer.writeheader()
        writer.writerows(filter_result)
    print("\n筛选后的电影已保存到 ./data/filter_movie.csv")


if __name__ == '__main__':
    main()
