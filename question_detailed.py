import requests
import json
import csv
from tempfile import NamedTemporaryFile
import shutil


def fetch_question(title_slug: str):
    url = "https://leetcode.com/graphql"
    headers = {"Content-Type": "application/json"}
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        title
        difficulty
        content
        codeSnippets { lang code }
      }
    }
    """
    variables = {"titleSlug": title_slug}
    response = requests.post(
        url,
        json={"query": query, "variables": variables},
        headers=headers
    )
    data = response.json()
    if "data" in data and "question" in data["data"]:
        question_data = data["data"]["question"]
        python_snippets = [
            snippet for snippet in question_data.get("codeSnippets", [])
            if snippet.get("lang") == "Python3" or snippet.get("langSlug") == "python3"
        ]
        question_data["codeSnippets"] = python_snippets  # 只保留 Python3 代码
    return data


def catch_detailed():
    # 输入文件（原数据）
    input_csv = "leetcode_easy_1600.csv"
    # 输出文件（新数据）
    output_csv = "leetcode_with_details.csv"

    with open(input_csv, "r", encoding="utf-8") as infile, \
            open(output_csv, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.DictReader(infile)
        # 新字段：存储抓取的题目详情（JSON 格式）
        fieldnames = reader.fieldnames + ["details"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            slug = row["slug"]  # 假设 CSV 中有 "slug" 列
            print(f"Fetching data for slug: {slug}")

            # 调用 fetch_question 获取题目数据
            data = fetch_question(slug)

            # 将数据转为 JSON 字符串并添加到当前行
            row["details"] = json.dumps(data, ensure_ascii=False)

            # 写入新文件
            writer.writerow(row)

    print(f"数据已保存到 {output_csv}")


# 执行抓取
catch_detailed()