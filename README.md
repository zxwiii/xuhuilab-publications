# 许晖课题组 (Hui Xu Lab) 学术成果与影响力官方自动化系统

专为**许晖课题组官方网站 ([xuhuilab.com/paper.html](https://xuhuilab.com/paper.html))** 打造的现代化、权威级学术成果自动化发布系统。数据直通 **Clarivate Web of Science (科睿唯安官方核心合集数据库)**，彻底摆脱第三方不规范数据，实现学术指标与被引频次的官方权威认证。

---

## 🌟 核心架构与学术特性

### 1. 架构解耦：双模块独立发布
* **模块一：【学术影响力与学者头衔大看板】**
  - **核心指标**：展示官方权威的 **35,458+ 次 Web of Science 核心合集总被引**、**H 指数 101**、**500 篇论文总收录**。
  - **顶级学者头衔**：权威收录并直达官方认证页面：
    - 2019–2023 科睿唯安全球高被引科学家 (*Clarivate Highly Cited Researcher*)
    - 2021–2025 爱思唯尔中国高被引学者 (*Elsevier Highly Cited Chinese Researcher*)
    - 2022–2026 全球前 2% 顶尖科学家 (*World's Top 2% Scientists · 年度与终身双榜单*)
  - **独立数据包**：`impact_data.js`（仅 1KB，极速秒显，支持高频日常更新）。

* **模块二：【学术成果与多维筛选系统】**
  - **全量权威成果**：收录 500 篇论文，卷期页码深度融合 Crossref 补全，确保完全规范。
  - **实时被引动态更新**：每篇论文均标有官方实时被引次数（如 `被引 115 次`），被引数据动态更新，绝不写死固化。
  - **按被引频次动态排序**：支持 `[ 🕒 最新发表 ]` 与 `[ 🔥 按被引频次 ]` 实时一键排序切换，绝对固定编号（#500 至 #1）始终锁定。
  - **通讯/第一作者精准认证**：收录官方认证的 249 篇通讯作者成果与 28 篇第一作者成果（去重后共 275 篇），支持文章一作兼通讯双重身份识别。
  - **代表作精准收敛（29 篇）**：严格限定 10 本世界顶尖期刊（*Nat. Energy, Nat. Commun., Adv. Mater., Adv. Energy Mater., Angew. Chem., ACS Nano, CES, AIChE J., ACS Catal., AFM*）+ 自定义代表作清单，不多不少，精准对齐 29 篇。
  - **交互功能完备**：卡片所有小徽章（顶刊、主题、高被引、代表作、通讯作者）点击直接联动筛选；恢复 `[ ↗ 直达 DOI ]` 与 `[ 📋 复制引用 ]`（点击自动复制标准学术引用到剪贴板）。
  - **杜绝横向滚动条**：全作用域高优先级 CSS 深度隔离，彻底消除凡科建站容器在各分辨率下的横向拖动条。

---

## 📂 项目文件清单

```text
xuhuilab/
├── sync_wos.py                 # Web of Science 官方 API 数据同步与数据清洗引擎
├── xh.txt                      # 官方认证通讯作者标题特征库 (249 篇，高容错匹配)
├── selected_doi.txt            # 代表作 DOI 补充清单 (与顶刊规则共同保证 29 篇)
├── esi_top_1_percent.txt       # ESI Top 1% / 热点论文 DOI 清单 (27 篇，终身勋章锁定)
├── wos_fixed_metadata.json     # 固化元数据缓存 (主题、卷页、作者锁定，确保运行极速)
├── crossref_cache.json         # Crossref 权威卷期页码缓存库 (补齐早期 WoS 缺失卷页)
├── impact_data.js              # 模块一：学术影响力独立数据脚本 (国内 Gitee 优先直通)
├── impact_metrics.json         # 模块一：学术影响力纯数据 JSON
├── publications_data.js        # 模块二：论文成果与筛选独立数据脚本 (Gitee/本地双保险)
├── publications.json           # 模块二：500 篇论文全量 JSON 数据库
├── 凡科_模块1_学术影响力.html    # 模块一凡科后台专属代码 (复制粘贴即可使用)
├── 凡科_模块2_成果与筛选.html    # 模块二凡科后台专属代码 (复制粘贴即可使用)
├── preview_all.html            # 本地双模块全景联动预览页 (双击直接在浏览器查看)
├── 一键更新论文数据.bat         # Windows 本地一键秒级自动同步与预览工具
└── .github/
    └── workflows/
        └── sync_wos.yml        # GitHub Actions 定时半月自动同步 + 镜像推送 Gitee 工作流
```

---

## 🚀 部署与日常维护指南

### 步骤一：本地全景预览
1. 直接在本地双击打开 [`preview_all.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/preview_all.html)；
2. 检查顶部的三大宏观指标（35,458 次被引、H-101）以及三大学者荣誉外链；
3. 检查下方的 500 篇成果列表：按被引排序、代表作（29篇）、通讯/第一作者（275篇）、复制引用、标签点击联动是否完全顺畅。

---

### 步骤二：部署到凡科建站后台（paper.html）
在凡科建站后台 `paper.html` 成果页面：
1. **添加模块一**：在页面最上方添加一个“插件代码”模块，将 [`凡科_模块1_学术影响力.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/凡科_模块1_学术影响力.html) 内的全部代码粘贴进去并保存；
2. **添加模块二**：在模块一下方添加第二个“插件代码”模块，将 [`凡科_模块2_成果与筛选.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/凡科_模块2_成果与筛选.html) 内的代码粘贴进去并保存；
3. **上传数据文件**：将本地的 `impact_data.js` 和 `publications_data.js` 两个文件上传至凡科根目录（或提交到 Gitee 仓库）。

---

### 步骤三：GitHub 与 Gitee 云端自动同步配置

1. **将工作区文件推送到 GitHub 仓库**：
   - 将 `xuhuilab` 文件夹内的文件提交并推送到您的 GitHub 仓库 `zxwiii/xuhuilab-publications`（`main` 分支）；
2. **设置 GitHub 密钥 (Secrets)**：
   - 在 GitHub 仓库 -> **Settings** -> **Secrets and variables** -> **Actions** -> **New repository secret**；
   - 添加 `WOS_API_KEY`：值为您的 Clarivate API Key (`a5650a3cf00489bdd8d41011a3eca36de7c668de`)；
   - 添加 `GITEE_USER`（Gitee 用户名）与 `GITEE_TOKEN`（Gitee 个人令牌）；
3. **半月自动化定时同步**：
   - GitHub Actions 工作流会在每月的 1 号和 15 号凌晨自动启动，拉取最新 WoS 引文和新论文，并自动将数据镜像推送到 Gitee；
   - 前端代码会**优先读取 Gitee 仓库的最新数据，若受阻在 2.5 秒内自动无缝降级至凡科本地兜底**，确保无论何时何地访问均秒级顺畅！

---

### 步骤四：后续新文章与通讯作者增补方法
* **新论文录入**：程序每半月自动查询 ResearcherID (`ADN-0578-2022`)，只要文章见刊录入 WoS，程序会自动捕获并分配最新终生编号。
* **新增通讯作者**：如果后续有 2026 年新见刊的通讯作者文章，只需打开 `xh.txt`，把新文章的英文标题追加粘贴在文件末尾即可（程序内置了去重与标点高容错清洗，完全不用担心重复或格式错乱）。
