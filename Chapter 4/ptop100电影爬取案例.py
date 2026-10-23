import requests
from lxml import html
import csv

all_movie_info_list = []

"""
"电影名", "年份", "上映时间", 
"类型", "时长", "评分", "语言", "主演",
"Slogan", "简介"
"""


def get_movie_info(movie_url):
    response = requests.get(movie_url)
    document = html.fromstring(response.text)

    movie_name = document.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/h2/a/text()")
    movie_year = document.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/h2/span/text()")
    movie_release_date = document.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[2]/text()")
    # list
    movie_type_list = document.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[3]/a/text()")

    movie_duration = document.xpath("//*[@id=\"original_header\"]/div[2]/section/div[1]/div/span[4]/text()")
    movie_rating = document.xpath("//*[@id=\"consensus_pill\"]/div/div[1]/div/div/@data-percent")
    movie_language = document.xpath(
        "//*[@id=\"media_v4\"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_actor = document.xpath("//*[@id=\"cast_scroller\"]/ol/li[1]/p[1]/a/text()")
    movie_slogan = document.xpath("//*[@id=\"original_header\"]/div[2]/section/div[3]/h3[1]/text()")
    movie_introduction = document.xpath("//*[@id=\"original_header\"]/div[2]/section/div[3]/div/p/text()")

    movie_name = movie_name[0].strip() if movie_name else None
    movie_year = movie_year[0].strip() if movie_year else None
    movie_release_date = movie_release_date[0].strip() if movie_release_date else None
    movie_type_list = "|".join(movie_type_list) if movie_type_list is not None and len(movie_type_list) > 0 else None
    movie_duration = movie_duration[0].strip() if movie_duration else None
    movie_rating = movie_rating[0].strip() if movie_rating else None
    movie_language = movie_language[0].strip() if movie_language else None
    movie_actor = movie_actor[0].strip() if movie_actor else None
    movie_slogan = movie_slogan[0].strip() if movie_slogan else None
    movie_introduction = movie_introduction[0].strip() if movie_introduction else None

    return {
        "电影名": movie_name,
        "年份": movie_year,
        "上映时间": movie_release_date,
        "类型": movie_type_list,
        "时长": movie_duration,
        "评分": movie_rating,
        "语言": movie_language,
        "主演": movie_actor,
        "Slogan": movie_slogan,
        "简介": movie_introduction
    }


# 网址路径
high_score_movie_url = "https://www.themoviedb.org/movie/top-rated"
base_movie_url = "https://www.themoviedb.org/"
high_score_other_movie_url = "https://www.themoviedb.org/discover/movie/items"


def main():
    for page in range(1, 6):
        if page == 1:
            # 向网址发起请求
            response = requests.get(high_score_movie_url)
        else:
            response = requests.post(high_score_other_movie_url, timeout=60,data=f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-04-16&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&vote_count.lte=&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400&view=&discover_preset=top-rated")
        # 将当前高分电影网页的纯文本 转换为 文档对象
        document = html.fromstring(response.text)
        # 拿到当前页面所有影片
        movie_div_element_list = document.xpath("//*[@class=\"media-list-results contents\"]/div")

        # 遍历  movie_div_element_list列表
        for movie_div_element in movie_div_element_list:
            # 获取到对应影片的详细页面链接  href属性中
            movie_info_url = movie_div_element.xpath("./div/div/a/@href")

            if movie_info_url:
                # 将单影片完整信息页面的链接地址 添加到 all_movie_info_list列表中
                movie_info = get_movie_info(base_movie_url + movie_info_url[0])
                all_movie_info_list.append(movie_info)

        with open("./data/high_score_movie.csv", "w", encoding="utf-8", newline="") as f:
            dict_write = csv.DictWriter(f, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "主演",
                                                       "Slogan", "简介"])
            # 写入表头信息
            dict_write.writeheader()
            # 写入所有电影信息
            dict_write.writerows(all_movie_info_list)


if __name__ == '__main__':
    main()
