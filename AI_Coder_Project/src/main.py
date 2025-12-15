import os
from planner import planner_agent
from coder import coder_agent

WORKSPACE = "workspace"

def main():
    # -------------------------------------------------------------------------
    # 按照你的要求：
    # 1. 样式、HTML结构、详情页逻辑 —— 一个字没动，原封不动复制你的代码。
    # 2. 仅在 script.js 部分，强制要求数据Tags必须匹配 cs.AI/cs.CV，否则筛选会失效。
    # -------------------------------------------------------------------------
    project_requirement = """
    【最高指令】：修复按钮可见性和详情页交互功能。
    
    必须生成 4 个文件，严格遵守以下规则：

    === 1. UI/UX 强制配色 (解决按钮看不清) ===
    - 所有可点击的按钮，背景色必须是 **深色/鲜艳色**，文字必须是 **白色**。
    - [View Details] 按钮：背景色 #007bff (亮蓝)。
    - [PDF] 按钮：背景色 #dc3545 (警示红)。
    - [Copy BibTeX] 按钮：背景色 #343a40 (深黑)。
    - 导航栏按钮：未选中是白色，鼠标悬停变蓝。
    - 绝对禁止使用浅色背景+浅色文字！

    === 2. index.html (首页) ===
    - 列表中的每一项，必须包含两个明显的按钮：
      1. <a href="detail.html?id=xx" class="btn btn-primary">View Details</a>
      2. <a href="pdf_link" target="_blank" class="btn btn-danger">PDF</a>
    - 标题必须清晰可见。

    === 3. detail.html (详情页) ===
    - 必须通过 URL 参数 (?id=...) 加载数据。
    - 必须包含两个功能按钮：
      1. <a id="pdf-btn" class="btn btn-danger" target="_blank">View PDF</a>
      2. <button id="bib-btn" class="btn btn-dark">Copy BibTeX</button>

    === 4. script.js (全功能交互) ===
    - 必须监听 `DOMContentLoaded` 事件。
    - 详情页逻辑：
      - 解析 ID -> 找到论文 -> 更新 DOM。
      - 设置 PDF 按钮的 href 属性。
      - 设置 BibTeX 按钮的 onclick 事件 -> 执行 `navigator.clipboard.writeText` -> 然后 `alert("复制成功")`。
    """
    
    print("🚀 Auto-Coder: 严格执行模式")
    print("🔇 正在执行：保留所有UI，仅修复导航数据匹配问题")
    print("=" * 50)

    if not os.path.exists(WORKSPACE):
        os.makedirs(WORKSPACE)

    files_to_generate = [
        {
            "file": "style.css",
            # 【绝对不动】完全是你给的代码
            "instruction": """
            编写高对比度 CSS：
            1. 全局：body { background-color: #f4f6f9; font-family: sans-serif; }
            2. 导航栏：.navbar { background-color: #2c3e50; padding: 15px; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            3. 导航标题：.nav-logo { color: #ffffff; font-size: 24px; font-weight: bold; margin-right: 30px; text-decoration: none; }
            4. 导航按钮：.nav-btn { background: #fff; color: #333; border: 2px solid #ccc; padding: 8px 16px; margin: 0 5px; cursor: pointer; border-radius: 4px; font-weight: bold; }
            5. 导航按钮激活/悬停：.nav-btn:hover, .nav-btn.active { background: #3498db; color: white; border-color: #3498db; }
            
            6. 【关键】功能按钮通用类 (.btn):
               - display: inline-block; padding: 10px 20px; color: white !important; text-decoration: none; border-radius: 5px; cursor: pointer; border: none; font-size: 14px; margin-right: 10px; transition: 0.3s;
            7. .btn-primary (详情按钮) { background-color: #007bff; }
            8. .btn-danger (PDF按钮) { background-color: #dc3545; }
            9. .btn-dark (BibTeX按钮) { background-color: #343a40; }
            10. .btn:hover { opacity: 0.8; transform: translateY(-2px); }
            
            11. 布局：.container { max-width: 900px; margin: 30px auto; }
            12. 卡片：.paper-card { background: white; padding: 25px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); display: flex; flex-direction: column; gap: 10px; }
            13. 卡片操作区：.card-actions { margin-top: 15px; }
            """
        },
        {
            "file": "index.html",
            # 【绝对不动】完全是你给的代码
            "instruction": """
            编写首页 HTML (无 CSS 代码)：
            1. 引入 style.css。
            2. 顶部导航：
               <div class="navbar">
                   <div class="nav-logo">arXiv CS Daily</div>
                   <div class="nav-group">
                       <button class="nav-btn" data-tag="All">All</button>
                       <button class="nav-btn" data-tag="cs.AI">cs.AI</button>
                       <button class="nav-btn" data-tag="cs.CV">cs.CV</button>
                       <button class="nav-btn" data-tag="cs.CL">cs.CL</button>
                   </div>
               </div>
            3. 内容区：<div id="paper-list-container" class="container"></div>
            4. 底部：<script src="script.js"></script>
            """
        },
        {
            "file": "detail.html",
            # 【绝对不动】完全是你给的代码
            "instruction": """
            编写详情页 HTML (无 CSS 代码)：
            1. 引入 style.css。
            2. 顶部导航：同首页，包含 "Back to Home" 链接。
            3. 内容区 (id="detail-container" class="container"):
               - <div class="paper-card">
                   <h1 id="detail-title" style="font-size: 28px; margin-bottom: 10px;">Loading...</h1>
                   <p id="detail-authors" style="color: #666; font-style: italic;"></p>
                   <div id="detail-tags" style="margin: 10px 0;"></div>
                   <div class="card-actions">
                       <!-- 这里的按钮 ID 必须严格匹配 script.js -->
                       <a id="pdf-btn" class="btn btn-danger" target="_blank">View PDF (Download)</a>
                       <button id="bib-btn" class="btn btn-dark">Copy BibTeX</button>
                   </div>
                   <hr style="margin: 20px 0; border: 0; border-top: 1px solid #eee;">
                   <h3>Abstract</h3>
                   <p id="detail-abstract" style="line-height: 1.8; color: #333;"></p>
               </div>
            4. 底部：<script src="script.js"></script>
            """
        },
        {
            "file": "script.js",
            # 【仅修改这里】：为了让按钮生效，我必须告诉 AI 数据 tags 要和按钮 data-tag 一致
            "instruction": """
            编写 JS 逻辑 (严格实现复制和跳转，并修复导航分类):
            1. 数据：const papers = [ 
                // ⚠️ 关键要求：每篇论文的 tags 数组必须包含 'cs.AI', 'cs.CV', 'cs.CL' 这些完全一致的字符串！
                // 否则按钮筛选不到数据！
                // 包含真实 pdf_link (如 https://arxiv.org/pdf/1706.03762.pdf) 和 bibtex 文本... 
            ];
            
            2. 通用初始化：
               document.addEventListener('DOMContentLoaded', () => {
                   const params = new URLSearchParams(window.location.search);
                   const id = params.get('id');
                   
                   if (id) {
                       // === 详情页逻辑 (完全保持不变) ===
                       const paper = papers.find(p => p.id == id);
                       if (paper) {
                           document.title = paper.title;
                           document.getElementById('detail-title').innerText = paper.title;
                           document.getElementById('detail-authors').innerText = paper.authors;
                           document.getElementById('detail-abstract').innerText = paper.abstract;
                           const pdfBtn = document.getElementById('pdf-btn');
                           pdfBtn.href = paper.pdf_link;
                           const bibBtn = document.getElementById('bib-btn');
                           bibBtn.onclick = async () => {
                               try {
                                   await navigator.clipboard.writeText(paper.bibtex);
                                   alert("✅ 成功！BibTeX 已复制到剪贴板。\\n\\n" + paper.bibtex);
                               } catch (err) {
                                   alert("⚠️ 复制失败 (浏览器限制)。BibTeX 内容如下：\\n\\n" + paper.bibtex);
                               }
                           };
                       }
                   } else {
                       // === 首页逻辑 ===
                       const container = document.getElementById('paper-list-container');
                       if (container) {
                           renderPapers(papers); // 默认显示所有
                           
                           // 导航栏点击
                           document.querySelectorAll('.nav-btn').forEach(btn => {
                               btn.addEventListener('click', (e) => {
                                   const tag = e.target.getAttribute('data-tag');
                                   
                                   // ⚠️ 增加：点击后要把其他按钮的 active 去掉，给自己加上，不然用户不知道点没点
                                   document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
                                   e.target.classList.add('active');

                                   const filtered = tag === 'All' ? papers : papers.filter(p => p.tags.includes(tag));
                                   renderPapers(filtered);
                               });
                           });
                       }
                   }
               });

            3. 渲染函数 renderPapers(list):
               // ⚠️ 增加：渲染前必须清空 container，否则会一直往下追加！
               const container = document.getElementById('paper-list-container');
               container.innerHTML = ''; 

               // 生成 HTML 字符串，必须包含两个按钮：
               // <a href="detail.html?id=${p.id}" class="btn btn-primary">View Details</a>
               // <a href="${p.pdf_link}" target="_blank" class="btn btn-danger">PDF</a>
            """
        }
    ]

    for task in files_to_generate:
        file_name = task['file']
        full_path = os.path.join(WORKSPACE, file_name)
        print(f"\n[Generating] 正在生成: {file_name}")
        coder_agent(f"编写文件 {file_name}。\n具体要求：{task['instruction']}", full_path)

    print("\n" + "=" * 50)
    print("🎉 修复完成！")
    print("👉 UI 配色和详情页功能 100% 保持你原来的样子。")
    print("👉 只修复了：点击 cs.AI 等按钮时，数据能正确筛选，且列表会刷新。")

if __name__ == "__main__":
    main()