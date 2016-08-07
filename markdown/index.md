# Markdown—学习手册
  > 2016-08-06 by Gol bj.

** 此文转载自[Te_Lee](http://www.jianshu.com/p/1e402922ee32)， 只用于个人学习使用。**

### 导语：
> Markdown是一种轻量级的「标记语言」，它的优点很多，目前也被越来越多的写作爱好者，撰稿者广泛使用。看到这里请不要被「标记」、「语言」所迷惑，Markdown 的语法十分简单。常用的标记符号也不超过十个，这种相对于更为复杂的 HTML 标记语言来说，Markdown 可谓是十分轻量的，学习成本也不需要太多，且一旦熟悉这种语法规则，会有一劳永逸的效果。

![Ulysses for Mac](http://ww3.sinaimg.cn/large/6aee7dbbjw1eqft66xcg3j21kw12mdub.jpg)

<center>[Ulysses for Mac](http://www.ulyssesapp.com/)</center>


### 一，认识 Markdown
在刚才的导语里提到，Markdown 是一种用来写作的轻量级 ***「标记语言」***，它用简洁的语法代替排版，而不像一般我们用的字处理软件 Word 或 Pages 有大量的排版、字体设置。它使我们专心于码字，用「标记」语法，来代替常见的排版格式。例如此文从内容到格式，甚至插图，键盘就可以通通搞定了。目前来看，支持 Markdown 语法的编辑器有很多，包括很多网站（例如简书）也支持了 Markdown 的文字录入。Markdown 从写作到完成，导出格式随心所欲，你可以导出 HTML 格式的文件用来网站发布，也可以十分方便的导出 PDF 格式，这种格式写出的简历更能得到 HR 的好感。甚至可以利用 CloudApp 这种云服务工具直接上传至网页用来分享你的文章，全球最大的轻博客平台 Tumblr，也支持 Mou 这类 Markdown 工具的直接上传。

#### Markdown 官方文档
>这里可以看到官方的 Markdown 语法规则文档，当然，** 后文我也会用自己的方式阐述这些语法的具体用法 **。

> * [创始人 John Gruber 的 Markdown 语法说明](http://ww3.sinaimg.cn/large/6aee7dbbjw1eqft66xcg3j21kw12mdub.jpg)
* [Markdown 中文版语法说明](http://ww3.sinaimg.cn/large/6aee7dbbjw1eqft66xcg3j21kw12mdub.jpg)

#### 使用 Markdown 的优点
> * 专注你的文字内容而不是排版样式，安心写作。
* 轻松的导出 HTML、PDF 和本身的 .md 文件。
* 纯文本内容，兼容所有的文本编辑器与字处理软件。
* 随时修改你的文章版本，不必像字处理软件生成若干文件版本导致混乱。
* 可读、直观、学习成本低。

#### 使用 Markdown 的误区
> We believe that writing is about content, about what you want to say – not about fancy formatting. 
我们坚信写作写的是内容，所思所想，而不是花样格式。
— Ulysses for Mac

* Markdown 旨在简洁、高效，也由于 Markdown 的易读易写，人们用不同的编程语言实现了多个版本的解析器和生成器，这就导致了目前不同的 Markdown 工具集成了不同的功能（基础功能大致相同），例如流程图与时序图，复杂表格与复杂公式的呈现，虽然功能的丰富并没有什么本质的缺点，但终归有些背离初衷，何况在编写的过程中很费神，不如使用专业的工具撰写来的更有效率，所以如果你需实现复杂功能，专业的图形界面工具会更加方便。当然，如果你对折腾这些不同客户端对 Markdown 的定制所带来高阶功能感到愉悦的话，那也是无可厚非的。

![image2](http://ww2.sinaimg.cn/large/6aee7dbbgw1eq320claw3j21kw0kjdpc.jpg)

<center>[flowchart.js on Github（使用 Markdown 绘制流程图）](http://#)</center>


#### 我该用什么工具？

在 Mac OS X 上，我强烈建议你用 [Mou](http://25.io/mou/) 这款免费且十分好用的 Markdown 编辑器


### 二，Markdown 语法的简要规则
#### 标题
![标题](http://ww1.sinaimg.cn/large/6aee7dbbgw1effeaclhiyj20eh09cwez.jpg)

标题是每篇文章都需要也是最常用的格式，在 Markdown 中，如果一段文字被定义为标题，只要在这段文字前加 # 号即可。

\# 一级标题  
\#\# 二级标题  
\#\#\# 三级标题  

以此类推，总共六级标题，建议在井号后加一个空格，这是最标准的 Markdown 语法。

####列表
 熟悉 HTML 的同学肯定知道有序列表与无序列表的区别，在 Markdown 下，列表的显示只需要在文字前加上 - 或 * 即可变为无序列表，有序列表则直接在文字前加1. 2. 3. 符号要和文字之间加上一个字符的空格。

![列表](http://ww4.sinaimg.cn/large/6aee7dbbgw1effew5aftij20d80bz3yw.jpg)

#### 引用
如果你需要引用一小段别处的句子，那么就要用引用的格式。
> 引用别人的话

只需要在文本前加入 > 这种尖括号（大于号）即可

#### 图片与链接

插入链接与插入图片的语法很像，区别在一个 !号

图片为：\!\[\]\(\)\{ImgCap\}\{/ImgCap\}

链接为：\[\]\(\)

#### 粗体与斜体

Markdown 的粗体和斜体也非常简单，用两个 * 包含一段文本就是粗体的语法，用一个 * 包含一段文本就是斜体的语法。

例如：**这里是粗体** 这里是斜体

#### 表格
表格是我觉得 Markdown 比较累人的地方，例子如下：

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

#### 代码框 
如果你是个程序猿，需要在文章里优雅的引用代码框，在 Markdown下实现也非常简单，只需要用两个 ` 把中间的代码包裹起来 

#### 分割线

分割线的语法只需要三个 * 号，例如

---

### 三，相关推荐:

#### 相关文章阅读：

* [Markdown-入门指南](http://www.jianshu.com/p/1e402922ee32)
* [Markdown写作浅谈](http://www.yangzhiping.com/tech/r-markdown-knitr.html)
* [Markdown 语法基础中文版](http://wowubuntu.com/markdown/)

#### 工具：

* Mou
* Sublime Text 插件：MarkdownEditing 
   MarkdownEditing是一个Sublime Text的Markdown插件。提供了一种合适的Markdown着色方案(light 与 dark)，包含强大的语法高亮，和实用的Markdown编辑功能。支持3种风格：Standard Markdown, GitHub flavored Markdown, MultiMarkdown。

* Sublime Text 插件：Markdown Preview


