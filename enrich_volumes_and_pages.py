"""
批量补全许晖课题组历史论文的卷号 (volume)、期号 (issue)、页码 (page) 与文章号 (article-number)
数据源：Crossref 官方 API (多线程并发加速，持久化缓存)
"""

import os
import json
import time
import urllib.request
import concurrent.futures

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PUBS_FILE = os.path.join(SCRIPT_DIR, "publications.json")
ARCHIVE_FILE = os.path.join(SCRIPT_DIR, "archive_publications_2025.json")
DATA_JS_FILE = os.path.join(SCRIPT_DIR, "publications_data.js")
CACHE_FILE = os.path.join(SCRIPT_DIR, "crossref_bib_cache.json")

def clean_doi(d):
    if not d:
        return ""
    d = d.strip()
    for prefix in ["https://doi.org/", "http://doi.org/", "doi:"]:
        if d.lower().startswith(prefix):
            d = d[len(prefix):]
    return d.strip().lower()

def fetch_bib_for_doi(doi):
    doi_clean = clean_doi(doi)
    if not doi_clean:
        return doi, None, None, None
    url = f"https://api.crossref.org/works/{doi_clean}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "xuhuilab-enrich/1.0 (mailto:admin@xuhuilab.com; contact: Jiangsu University)",
            "Accept": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read().decode("utf-8"))
            msg = data.get("message", {})
            vol = str(msg.get("volume") or "").strip()
            iss = str(msg.get("issue") or "").strip()
            pg = str(msg.get("page") or "").strip()
            art_num = str(msg.get("article-number") or "").strip()
            # 若无传统页码但有电子文章编号，使用电子文章编号作为页码
            final_page = pg if pg else art_num
            return doi_clean, vol, iss, final_page
    except Exception:
        return doi_clean, "", "", ""

def main():
    print("=" * 60)
    print("🚀 开始批量提取 508 篇论文的卷号、期号与页码数据...")
    print("=" * 60)

    # 1. 加载已有缓存
    cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cache = json.load(f)
            print(f"[Cache] 已载入文献卷期缓存: {len(cache)} 条")
        except Exception:
            cache = {}

    # 2. 读取当前 publications.json
    with open(PUBS_FILE, "r", encoding="utf-8") as f:
        pubs = json.load(f)

    # 3. 找出所有需要查询的 DOI
    all_dois = []
    for p in pubs:
        d = clean_doi(p.get("doi", ""))
        if d:
            all_dois.append(d)
    
    unique_dois = list(dict.fromkeys(all_dois))
    to_fetch = [d for d in unique_dois if d not in cache or (not cache[d].get("volume") and not cache[d].get("page"))]
    print(f"[Crossref] 总 DOI 篇数: {len(unique_dois)}，需从 Crossref 补齐卷期: {len(to_fetch)} 篇")

    if to_fetch:
        print("[Crossref] 正在启动 12 线程并发查询...")
        t0 = time.time()
        success_cnt = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
            futures = {executor.submit(fetch_bib_for_doi, d): d for d in to_fetch}
            for fut in concurrent.futures.as_completed(futures):
                doi_clean, vol, iss, pg = fut.result()
                cache[doi_clean] = {
                    "volume": vol,
                    "issue": iss,
                    "page": pg
                }
                if vol or pg:
                    success_cnt += 1
                if len(cache) % 50 == 0:
                    print(f"  已处理 {len(cache)} / {len(unique_dois)} 篇...")
        print(f"[Crossref] 批量获取完成！耗时: {time.time()-t0:.1f} 秒，成功匹配卷期: {success_cnt} 篇")

        # 写入缓存文件
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)

    # 4. 回填至 publications.json
    enriched_count = 0
    for p in pubs:
        d = clean_doi(p.get("doi", ""))
        if d in cache:
            c = cache[d]
            p["volume"] = c.get("volume", "")
            p["issue"] = c.get("issue", "")
            p["page"] = c.get("page", "")
            if p["volume"] or p["page"]:
                enriched_count += 1
        else:
            p["volume"] = ""
            p["issue"] = ""
            p["page"] = ""

    print(f"[Enrich] 成功为 {enriched_count} / {len(pubs)} 篇论文注入卷号与页码！")

    # 5. 更新 publications.json
    with open(PUBS_FILE, "w", encoding="utf-8") as f:
        json.dump(pubs, f, ensure_ascii=False, indent=2)
    print(f"[Save] 已保存最新 {PUBS_FILE}")

    # 6. 更新 archive_publications_2025.json（固定永久归档）
    archive_pubs = [p for p in pubs if p.get("year", 0) <= 2025]
    with open(ARCHIVE_FILE, "w", encoding="utf-8") as f:
        json.dump(archive_pubs, f, ensure_ascii=False, indent=2)
    print(f"[Save] 已同步更新历史永久归档: {ARCHIVE_FILE} ({len(archive_pubs)} 篇)")

    # 7. 更新 publications_data.js
    stats = {}
    years_stat = {}
    topics_stat = {}
    for p in pubs:
        y = str(p.get("year", ""))
        yg = p.get("year_group", y)
        years_stat[yg] = years_stat.get(yg, 0) + 1
        for t in p.get("topics", []):
            tid = t.get("id")
            topics_stat[tid] = topics_stat.get(tid, 0) + 1

    stats = {
        "total": len(pubs),
        "selected": sum(1 for p in pubs if p.get("is_selected")),
        "esi": sum(1 for p in pubs if p.get("is_esi")),
        "years": years_stat,
        "topics": topics_stat
    }

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    js_content = f"""/**
 * 许晖课题组 (Hui Xu Lab) 学术成果数据库
 * 更新时间: {timestamp}
 * 收录总篇数: {len(pubs)}
 */
window.XUHUILAB_STATS = {json.dumps(stats, ensure_ascii=False, indent=2)};

window.XUHUILAB_PUBLICATIONS = {json.dumps(pubs, ensure_ascii=False, indent=2)};
"""
    with open(DATA_JS_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"[Save] 已重新生成 {DATA_JS_FILE}")

    # 打印前 3 篇展示样例
    print("\n[Preview Sample]:")
    for p in pubs[:3]:
        vol_str = f", {p['volume']}" if p.get('volume') else ""
        iss_str = f"({p['issue']})" if p.get('issue') else ""
        pg_str = f": {p['page']}" if p.get('page') else ""
        print(f"#{p['index']} {p['title'][:40]}... -> {p['journal']}, {p['year']}{vol_str}{iss_str}{pg_str}")

if __name__ == "__main__":
    main()
