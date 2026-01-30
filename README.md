# 重新拉取步骤：
```
git add .
git commit -m "保存我当前进度，准备同步队友代码"
git pull origin main
```

|情况|结果|你需要做什么|
|---|---|---|
|最顺利|队友改了 A 文件，你改了 B 文件|无需操作。Git 会自动把 A 文件下载到你的文件夹里|
|自动合并|你们改了同一个文件，但不是同一行|输入:wq退出。会弹出Vim黑色界面（合并信息），直接退出即可|
|发生冲突|你们俩改了同一文件的同一行|手动解决。VS Code 会把冲突的地方标红，你需要选一个（或两个都留），然后重新 add 和 commit|

# The `mcmthesis` Class

This class is designed for the MCM/ICM.

This work is released under the [LaTeX Project Public
License](http://www.latex-project.org/lppl.txt), v1.3c or later.

## Installation

```plain
This work consists of the file mcmthesis.dtx,
                               figures/, and
                               code/,
and the derived files          mcmthesis.cls,
                               mcmthesis-demo.tex,
                               README,
                               LICENSE,
                               mcmthesis.pdf and
                               mcmthesis-demo.pdf.

To install this class, you should
    compile mcmthesis.dtx      with xetex mcmthesis.dtx,
    compile mcmthesis.dtx      with xelatex mcmthesis.dtx twice,
    compile mcmthesis-demo.tex with xelatex mcmthesis-demo.tex twice,
    rename README.tex and LICENSE.tex respectively to README and LICENSE,
    move mcmthesis.cls         to TEXMF/tex/latex/mcmthesis/,
    move mcmthesis.dtx         to TEXMF/source/latex/mcmthesis/,
    move other files           to TEXMF/doc/latex/mcmthesis/ and then
    run texhash.
```

## Authors

* [Zhaoli Wang][zhaoli]: 343083553@qq.com
* [Liam Huang][liam-ctan]: liamhuang0205+mcmthesis@gmail.com

## Project Page

If you are interested in the process of development you may observe

<https://github.com/Liam0205/mcmthesis>

[zhaoli]: http://www.latexstudio.net/
[liam-ctan]: http://www.ctan.org/author/huang-l
