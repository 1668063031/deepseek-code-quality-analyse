import requests
import json
import csv

def fetch_all_problems():
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    data = response.json()
    return [
        {
            "id": item["stat"]["question_id"],
            "title": item["stat"]["question__title"],
            "slug": item["stat"]["question__title_slug"],
            "difficulty": ["Easy", "Medium", "Hard"][item["difficulty"]["level"] - 1],
            "paid_only": item["paid_only"]
        }
        for item in data["stat_status_pairs"]
    ]

# 测试
all_problems = fetch_all_problems()
easy_problems = [p for p in all_problems if p["difficulty"] == "Easy" and not p["paid_only"]][:400]
med_problems = [p for p in all_problems if p["difficulty"] == "Medium" and not p["paid_only"]][:400]
hard_problems = [p for p in all_problems if p["difficulty"] == "Hard" and not p["paid_only"]][:400]


def fetch_question(title_slug):
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        title
        content
        difficulty
        topicTags { name }
      }
    }
    """
    response = requests.post(
        "https://leetcode.com/graphql",
        json={"query": query, "variables": {"titleSlug": title_slug}},
        headers={"Content-Type": "application/json"}
    )
    return response.json()

# 保存到 CSV 文件
def catch_question( ):
    with open("leetcode_easy_1600.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "title", "slug", "difficulty", "paid_only"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # 写入表头
        writer.writerows(easy_problems)  # 写入所有数据
        writer.writerows(med_problems)
        writer.writerows(hard_problems)

    print(f"已保存 {len(easy_problems)} 道 Easy 题目到 leetcode_easy_500.csv")


