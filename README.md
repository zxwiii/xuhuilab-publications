# 许晖课题组 (Hui Xu Lab) 学术成果全自动同步与发布系统

专为**许晖课题组网站 ([xuhuilab.com/paper.html](https://xuhuilab.com/paper.html))** 定制的现代化、免登录、国内 100% 稳定的学术成果自动化发布系统。

---

## 核心特性升级

1. **学术级严谨规范**：
   - 彻底删除原顶部的数字统计卡片与大色块横幅，恢复庄重端庄的经典学术标题栏；
   - 许晖老师姓名（`Hui Xu` / `许晖`）专属加粗显示，**严格不带星号 (*)**；
   - 顶级代表作**严格核实**：已自动收录 *Nature Energy*、*Advanced Materials (AM)*、*Advanced Energy Materials (AEM)*、*Angewandte Chemie*、*ACS Nano* 等顶级顶刊，彻底剔除早年的会议论文集 (*Advanced Materials Research*) 与非顶刊 (*Advanced Materials Interfaces*)；
   - 主题词去 AI 化：采用纯文本 **`CO2`**（无下标、无任何 Emoji 表情），严谨规范分类。
2. **年份智能归纳**：
   - 2026 ~ 2015 按年份逐级展示；
   - **2014年及以前的论文统一合并至“2014及以前 (≤2014)”**，按钮布局精简清爽。
3. **Crossref 权威作者补全**：
   - 自动调用全球学术出版官方 Crossref API 补齐所有论文的**完整作者姓名（拒绝缩写）**与规范期刊卷期页码，并持久化缓存至 `crossref_cache.json`。
4. **国内 100% 访问保障（Gitee 镜像）**：
   - GitHub 负责云端无障碍爬取学术 API；
   - 自动推送到国内 **Gitee（码云）**，国内高校、校园网与家庭宽带毫秒级直连，零被墙风险！

---

## 文件清单说明

```text
xuhuilab/
├── sync_orcid.py                 # ORCID + Crossref 双核全自动同步清洗脚本
├── selected_doi.txt              # 代表作 DOI 清单（已预置 Nature Energy/AM/AEM/Angew等顶刊）
├── esi_top_1_percent.txt         # ESI TOP 1% / 热点论文 DOI 清单（随时粘贴）
├── publications.json             # 生成的完整学术论文 JSON 数据库 (508 篇)
├── publications_data.js          # 生成的前端直引 JS 数据（国内 Gitee/CDN 直通）
├── orcid_raw_cache.json          # ORCID 原始数据缓存库
├── crossref_cache.json           # Crossref 权威作者全名缓存库
├── preview_publications.html     # 本地高颜值交互预览页面（双击直接查看）
├── 一键更新论文数据.bat           # Windows 本地一键秒级增量更新批处理
├── 凡科嵌入代码.html              # 凡科后台“插件代码”模块专属嵌入代码
└── .github/
    └── workflows/
        └── update_publications.yml  # GitHub Actions 定时自动更新 + 秒推 Gitee 工作流
```

---

## 3分钟部署指南

### 第一步：本地预览与确认
- 直接在本地双击打开 [`preview_publications.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/preview_publications.html)；
- 查看已清洗的 508 篇论文：作者全名、严谨代表作、去 AI 化的主题词、年份合并展示是否完美。

### 第二步：在 Gitee 与 GitHub 创建仓库
1. **在 Gitee（码云）新建公开仓库**：
   - 仓库名称填：`xuhuilab-publications`，设为**公开（Public）**；
2. **在 GitHub 新建公开仓库**：
   - 仓库名称同样填：`xuhuilab-publications`，设为**公开（Public）**；
3. **上传代码**：
   - 将本 `xuhuilab` 文件夹内的全部文件（包括 `.github` 隐藏文件夹）推送到您的 GitHub 仓库中；
4. **配置 GitHub 自动同步到 Gitee**（可选但推荐，只需配一次）：
   - 在 GitHub 仓库页点击 **Settings** -> **Secrets and variables** -> **Actions** -> **New repository secret**；
   - 添加 `GITEE_USER`（您的 Gitee 用户名）和 `GITEE_TOKEN`（在 Gitee 设置 -> 私人令牌 生成的 token）；
   - 配置好后，每次 GitHub Actions 定时运行完，就会**自动把最新数据推给 Gitee**！

### 第三步：在凡科建站后台嵌入
1. 用文本编辑器打开 [`凡科嵌入代码.html`](file:///e:/OneDrive%20-%20Jiangsu%20University/%E5%B7%A5%E4%BD%9C/5.%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%AE%A1%E7%90%86/%E7%BD%91%E7%AB%99/wxz/xuhuilab/凡科嵌入代码.html)；
2. 将第 8 行的 `YOUR_GITEE_USERNAME` 替换为您注册的 Gitee 用户名；
3. 登录凡科后台，进入 `paper.html` 页面；
4. 添加一个 **“插件代码”** 模块，将文件内的所有代码直接粘贴进去，保存并发布；
5. 大功告成！从此许老师网站将永远自动展示最新学术论文，国内秒开，免登录维护。
