# 许晖课题组 (Hui Xu Lab) 学术成果与影响力官方自动化系统

专为**许晖课题组官方网站 ([xuhuilab.com/paper.html](https://xuhuilab.com/paper.html))** 打造的现代化、权威级学术成果自动化发布系统。数据直通 **Clarivate Web of Science (科睿唯安官方核心合集数据库)**，彻底摆脱第三方不规范数据，实现学术指标与被引频次的官方权威认证。

---

## 🌟 核心架构与学术特性

### 1. 架构解耦：双模块独立或全合一发布
* **模块一：【学术影响力与学者头衔大看板】**
  - **核心指标**：展示官方权威的 **35,475+ 次 Web of Science 核心合集总被引**、**H 指数 101**、**504 篇论文总收录**。
  - **顶级学者头衔**：权威收录并直达官方认证页面：
    - 2019–2023 科睿唯安全球高被引科学家 (*Clarivate Highly Cited Researcher*)
    - 2021–2025 爱思唯尔中国高被引学者 (*Elsevier Highly Cited Chinese Researcher*)
    - 2022–2026 全球前 2% 顶尖科学家 (*World's Top 2% Scientists · 年度与终身双榜单*)
  - **动态纯净加载**：HTML 标签内无任何硬编码写死旧数字（初始为 `--`），100% 从云端动态注入。

* **模块二：【学术成果与多维筛选系统】**
  - **全量权威成果**：收录 504 篇论文，卷期页码深度融合 Crossref 补全，确保完全规范。
  - **实时被引动态更新**：每篇论文均标有官方实时被引次数（如 `被引 115 次`），被引数据动态更新，绝不写死固化。
  - **按被引频次动态排序**：支持 `[ 🕒 最新发表 ]` 与 `[ 🔥 按被引频次 ]` 实时一键排序切换，绝对固定编号（#504 至 #1）始终锁定。
  - **通讯/第一作者精准认证**：收录官方认证的通讯作者成果与第一作者成果（去重后共 275 篇），支持文章一作兼通讯双重身份识别。
  - **代表作精准收敛（29 篇）**：严格限定 10 本世界顶尖期刊（*Nat. Energy, Nat. Commun., Adv. Mater., Adv. Energy Mater., Angew. Chem., ACS Nano, CES, AIChE J., ACS Catal., AFM*）+ 自定义代表作清单，不多不少，精准对齐 29 篇（`Nat. Energy` 居首位排列）。
  - **交互功能完备**：卡片所有小徽章（顶刊、主题、高被引、代表作、通讯作者）点击直接联动筛选；提供 `[ ↗ 直达 DOI ]` 与 `[ 📋 复制引用 ]`（点击自动复制标准学术引用到剪贴板）。
  - **杜绝横向滚动条**：全作用域高优先级 CSS 深度隔离，彻底消除凡科建站容器在各分辨率下的横向拖动条。

* **单模块合一版：【凡科_全合一单代码_完美版.html】**
  - 完美整合模块一与模块二，仅需在凡科网后台添加一个插件代码模块即可一次性嵌入全部功能，统一 1200px 版心居中。

---

## ⚡ 全网极速 0 缓存云端分发技术（彻底根治 CDN 滞后与 7 天强缓存）

本系统采用行业前沿的 **Commit SHA 瞬时哈希版本号 + Fastly 全球多节点 CDN** 架构：
1. **彻底根治 7 天本地强缓存**：前端启动时先花费 ~100ms 探查 GitHub 最新 Commit SHA（如 `@2d4385ffcc`），直接拼接请求全球唯一的绝对版本文件（`fastly.jsdelivr.net/...@2d4385ffcc/impact_data.js`），**缓存命中率直接归零，任何新同步成果全网秒级呈现**！
2. **多源并发容灾保护**：若 Commit SHA 探测受阻，自动无缝平滑回退至 `@main` 分支加速源及 Gitee 官方国内跨域 API，确保 100% 永不白屏。
3. **严格中国北京时间日历**：自动化同步脚本与 GitHub Actions 强制绑定 `TZ: Asia/Shanghai` 并结合 `timezone(timedelta(hours=8))`，杜绝虚拟机零时区导致日期倒退。

---

## 📂 项目文件清单

```text
xuhuilab/
├── sync_wos.py                 # Web of Science 官方 API 数据同步与数据清洗引擎 (防截断保护+北京时区)
├── corresponding_titles.txt    # 官方认证通讯作者标题特征库 (标准命名，原 xh.txt，249 篇高容错匹配)
├── xh.txt                      # 兼容软链接/同源文件
├── selected_doi.txt            # 代表作 DOI 补充清单 (与顶刊规则共同保证 29 篇)
├── esi_top_1_percent.txt       # ESI Top 1% / 热点论文 DOI 清单 (27 篇，终身勋章锁定)
├── wos_fixed_metadata.json     # 固化元数据缓存 (主题、卷页、作者锁定，确保运行极速)
├── crossref_cache.json         # Crossref 权威卷期页码缓存库 (补齐早期 WoS 缺失卷页)
├── impact_data.js              # 模块一：学术影响力独立数据脚本 (全网 Fastly CDN 瞬时版本加载)
├── impact_metrics.json         # 模块一：学术影响力纯数据 JSON
├── publications_data.js        # 模块二：论文成果与筛选独立数据脚本 (504 篇成果集)
├── publications.json           # 模块二：504 篇论文全量 JSON 数据库
├── 凡科_全合一单代码_完美版.html  # 推荐：双模块二合一凡科专属单代码 (复制粘贴一个模块搞定)
├── 凡科_模块1_学术影响力.html    # 模块一凡科后台专属代码 (独立部署时使用)
├── 凡科_模块2_成果与筛选.html    # 模块二凡科后台专属代码 (独立部署时使用)
├── preview_all.html            # 本地双模块全景联动预览页 (双击直接在浏览器查看)
├── 一键更新论文数据.bat         # Windows 本地一键秒级自动同步与预览工具
├── skills/                     # 本项目专用 Skill 副本
│   └── academic-website-builder/ # 通用学术主页构建 Skill (已同步至全局 ~/.gemini/config/skills)
└── .github/
    └── workflows/
        └── update_publications.yml # GitHub Actions 定时自动同步 + Purge CDN 缓存 + 镜像推送 Gitee
```

---

## 🚀 部署与日常维护指南

### 步骤一：本地全景预览
1. 直接在本地双击打开 [`preview_all.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/preview_all.html)；
2. 检查顶部的三大宏观指标（35,475 次被引、H-101、504篇）以及三大学者荣誉外链；
3. 检查下方的成果列表：默认选中代表作（29篇，`Nat. Energy` 居首）、通讯/第一作者（275篇）、按被引排序、复制引用等交互是否顺畅。

---

### 步骤二：部署到凡科建站后台（paper.html）
在凡科建站后台 `paper.html` 成果页面：
* **方式 A（强烈推荐：全合一单代码）**：
  在页面中添加一个“插件代码”模块，将 [`凡科_全合一单代码_完美版.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/凡科_全合一单代码_完美版.html) 的全部代码粘贴进去并保存发布。
* **方式 B（双模块独立嵌入）**：
  分别添加两个插件代码模块，上方放 [`凡科_模块1_学术影响力.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/凡科_模块1_学术影响力.html)，下方放 [`凡科_模块2_成果与筛选.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/凡科_模块2_成果与筛选.html)。

> 💡 **无需在凡科或目标主机上传任何本地 .js 文件**！所有文章和指标均通过云端 Fastly CDN 瞬时版本号自动秒开加载。

---

### 步骤三：GitHub 与 Gitee 云端自动同步配置

1. **将工作区文件推送到 GitHub 仓库**：
   - 将 `xuhuilab` 文件夹内的文件提交并推送到 GitHub 仓库 `zxwiii/xuhuilab-publications`（`main` 分支）；
2. **设置 GitHub 密钥 (Secrets)**：
   - 在 GitHub 仓库 -> **Settings** -> **Secrets and variables** -> **Actions**；
   - 确保 `WOS_API_KEY` 已配置（支持双 Key 逗号隔开故障转移）；
   - 确保 `GITEE_USER` 与 `GITEE_TOKEN` 已配置；
3. **自动化定时同步**：
   - GitHub Actions 工作流定时自动启动，执行 WoS 官方抓取；
   - 同步完成后自动向 Gitee 镜像推送（`master` 与 `main` 双分支）；
   - 末尾自动调用 jsDelivr 全球 Purge 接口刷新边缘节点；
   - 无论何时打开网页，前端都会自动获取最新 Commit SHA，实现 0 秒延迟呈现最新成果！

---

### 步骤四：后续新文章与通讯作者增补方法
* **新论文录入**：程序自动查询 ResearcherID (`ADN-0578-2022`)，只要文章见刊录入 WoS，程序会自动捕获并分配最新终生编号。内置实时完整性防截断锁，绝不因 API 限流覆盖残缺数据。
* **新增通讯作者**：如果后续有新见刊的通讯作者文章，只需打开 `xh.txt`（或 `corresponding_titles.txt`），把新文章的英文标题追加在文件末尾即可。
