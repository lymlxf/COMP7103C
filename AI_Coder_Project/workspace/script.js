// 论文数据
const papers = [
    {
        id: 1,
        title: "Attention Is All You Need",
        authors: "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin",
        abstract: "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.",
        pdf_link: "https://arxiv.org/pdf/1706.03762.pdf",
        bibtex: `@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, {\L}ukasz and Polosukhin, Illia},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}`,
        tags: ["cs.AI", "cs.CL", "cs.LG"]
    },
    {
        id: 2,
        title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        authors: "Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova",
        abstract: "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.",
        pdf_link: "https://arxiv.org/pdf/1810.04805.pdf",
        bibtex: `@article{devlin2018bert,
  title={Bert: Pre-training of deep bidirectional transformers for language understanding},
  author={Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  journal={arXiv preprint arXiv:1810.04805},
  year={2018}
}`,
        tags: ["cs.CL", "cs.AI"]
    },
    {
        id: 3,
        title: "ImageNet Classification with Deep Convolutional Neural Networks",
        authors: "Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton",
        abstract: "We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0% which is considerably better than the previous state-of-the-art. The neural network, which has 60 million parameters and 650,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and three fully-connected layers with a final 1000-way softmax.",
        pdf_link: "https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf",
        bibtex: `@article{krizhevsky2012imagenet,
  title={Imagenet classification with deep convolutional neural networks},
  author={Krizhevsky, Alex and Sutskever, Ilya and Hinton, Geoffrey E},
  journal={Advances in neural information processing systems},
  volume={25},
  pages={1097--1105},
  year={2012}
}`,
        tags: ["cs.CV", "cs.LG", "cs.AI"]
    },
    {
        id: 4,
        title: "Deep Residual Learning for Image Recognition",
        authors: "Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun",
        abstract: "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers—8× deeper than VGG nets but still having lower complexity.",
        pdf_link: "https://arxiv.org/pdf/1512.03385.pdf",
        bibtex: `@article{he2016deep,
  title={Deep residual learning for image recognition},
  author={He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian},
  journal={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={770--778},
  year={2016}
}`,
        tags: ["cs.CV", "cs.AI"]
    },
    {
        id: 5,
        title: "GPT-3: Language Models are Few-Shot Learners",
        authors: "Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei",
        abstract: "Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions—something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches.",
        pdf_link: "https://arxiv.org/pdf/2005.14165.pdf",
        bibtex: `@article{brown2020language,
  title={Language models are few-shot learners},
  author={Brown, Tom B and Mann, Benjamin and Ryder, Nick and Subbiah, Melanie and Kaplan, Jared and Dhariwal, Prafulla and Neelakantan, Arvind and Shyam, Pranav and Sastry, Girish and Askell, Amanda and others},
  journal={Advances in neural information processing systems},
  volume={33},
  pages={1877--1901},
  year={2020}
}`,
        tags: ["cs.CL", "cs.AI", "cs.LG"]
    }
];

// 渲染论文列表到首页容器
function renderPapers(list) {
    const container = document.getElementById('paper-list-container');
    if (!container) return;
    
    // 清空容器
    container.innerHTML = '';
    
    // 如果列表为空，显示提示
    if (list.length === 0) {
        container.innerHTML = '<div class="no-papers">No papers found for this category.</div>';
        return;
    }
    
    // 为每篇论文创建卡片
    list.forEach(paper => {
        const card = document.createElement('div');
        card.className = 'paper-card';
        
        // 限制摘要长度
        const shortAbstract = paper.abstract.length > 200 
            ? paper.abstract.substring(0, 200) + '...' 
            : paper.abstract;
        
        card.innerHTML = `
            <h3 class="paper-title">${paper.title}</h3>
            <p class="paper-authors"><strong>Authors:</strong> ${paper.authors}</p>
            <p class="paper-abstract"><strong>Abstract:</strong> ${shortAbstract}</p>
            <div class="paper-tags">
                ${paper.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
            </div>
            <div class="paper-actions">
                <a href="detail.html?id=${paper.id}" class="btn btn-primary">View Details</a>
                <a href="${paper.pdf_link}" target="_blank" class="btn btn-danger">PDF</a>
            </div>
        `;
        
        container.appendChild(card);
    });
}

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    
    if (id) {
        // === 详情页逻辑 ===
        const paper = papers.find(p => p.id == id);
        if (paper) {
            // 设置页面标题和内容
            document.title = paper.title;
            document.getElementById('detail-title').innerText = paper.title;
            document.getElementById('detail-authors').innerText = paper.authors;
            document.getElementById('detail-abstract').innerText = paper.abstract;
            
            // 设置PDF按钮链接
            const pdfBtn = document.getElementById('pdf-btn');
            pdfBtn.href = paper.pdf_link;
            
            // 设置BibTeX按钮点击事件
            const bibBtn = document.getElementById('bib-btn');
            bibBtn.onclick = async () => {
                try {
                    await navigator.clipboard.writeText(paper.bibtex);
                    alert("✅ 成功！BibTeX 已复制到剪贴板。\n\n" + paper.bibtex);
                } catch (err) {
                    alert("⚠️ 复制失败 (浏览器限制)。BibTeX 内容如下：\n\n" + paper.bibtex);
                }
            };
            
            // 显示标签
            const tagsContainer = document.getElementById('detail-tags');
            if (tagsContainer) {
                tagsContainer.innerHTML = paper.tags.map(tag => `<span class="tag">${tag}</span>`).join('');
            }
        } else {
            // 如果找不到论文，显示错误信息
            document.getElementById('detail-title').innerText = "Paper Not Found";
            document.getElementById('detail-authors').innerText = "";
            document.getElementById('detail-abstract').innerText = "The requested paper could not be found.";
        }
    } else {
        // === 首页逻辑 ===
        const container = document.getElementById('paper-list-container');
        if (container) {
            // 默认显示所有论文
            renderPapers(papers);
            
            // 为导航按钮添加点击事件
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const tag = e.target.getAttribute('data-tag');
                    
                    // 移除所有按钮的active类，为当前点击的按钮添加active类
                    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
                    e.target.classList.add('active');
                    
                    // 根据标签筛选论文
                    const filtered = tag === 'All' ? papers : papers.filter(p => p.tags.includes(tag));
                    renderPapers(filtered);
                });
            });
            
            // 默认激活"All"按钮
            const allBtn = document.querySelector('.nav-btn[data-tag="All"]');
            if (allBtn) {
                allBtn.classList.add('active');
            }
        }
    }
});