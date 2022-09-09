# DOS5101_BestAction使用教程

## 安装Python环境（Windows）

1. 下载IDLE
    - Python官网：https://www.python.org/
    - ![image-20220909103247866](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909103247866.png)
    - 下载完成后，打开安装包`python-3.10.7-amd64.exe`，安装选项中**必须**勾选`Add Python 3.10 to PATH`。
    - ![image-20220909103435318](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909103435318.png)
2. 下载PyCharm
    - PyCharm官网：https://www.jetbrains.com/pycharm/
    - ![image-20220909103658938](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909103658938.png)
    - 选择Community版本下载
    - ![image-20220909103728880](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909103728880.png)
    - 下载完成后，打开安装包`pycharm-community-2022.2.1.exe`，选择`next`。
    - 选择安装目录，确保安装路径中**没有中文**。例如可以是`D:\InstallApp\...`，不能是`D:\安装\...`。
    - ![image-20220909104257914](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909104257914.png)
    - 勾选`PyCharm Community Edition`、`Add "Open Folder as Project"`、`.py`三个选项。
    - ![image-20220909104526989](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909104526989.png)
    - 选择`Install`，开始安装。



## 下载代码

1. 代码：https://github.com/xdai02/DOS5101_BestAction

2. 点击`Code`，选择`Download ZIP`。

    ![image-20220909105024017](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909105024017.png)

3. 将下载好的压缩包`DOS5101_BestAction-main.zip`解压，得到`DOS5101_BestAction`文件夹。

    ![image-20220909105345284](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909105345284.png)

> 其中：
>
> - `action_analyzer.py`为Python代码文件
> - `data.xlsx`为参考数据、规则等信息
> - `README.md`为简单的使用说明



## 打开/查看代码

1. 桌面上打开刚安装好的PyCharm（注意不是那个安装包），选择`Open`。

    ![image-20220909105919115](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909105919115.png)

2. 选择刚在解压出来的文件夹`DOS5101_BestAction-main`。

    ![image-20220909110008099](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909110008099.png)

    > 如跳出以下窗口，选择`Trust Project`。
    >
    > ![image-20220909110112021](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909110112021.png)

3. 在左侧`Project`栏中，选择Python代码文件`action_analyzer.py`，即可看到代码。

    ![image-20220909110353164](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909110353164.png)

    > 如字体太小，可在左上角`File`→`Settings`→`Editor`→`Font`→`Size`处修改字体，推荐改为`16`。
    >
    > ![image-20220909110649741](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909110649741.png)

4. 在`File`→`Settings`→`Project: DOS5101_BestAction-main`→`Python Interpreter`中，选择`Add Local Interpreter`。

    ![image-20220909112609545](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909112609545.png)

5. 选择`OK`

    ![image-20220909112650020](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909112650020.png)

6. 再选择`OK`

    ![image-20220909112714245](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909112714245.png)



## 代码运行

1. 代码最开始处用于设置目前的数据，包括两部分：已经发生的Actions、已经发生的Events。可在此处进行修改和添加。

    ![image-20220909111245724](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909111245724.png)

2. 在代码空白处，右键选择`Run 'action_analyzer'`。

    ![image-20220909112841703](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909112841703.png)

3. 查看运行结果

    ![image-20220909113915512](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909113915512.png)



## 想看更详细的分析结果？

- 这个程序默认只会显示下一轮的最佳组合，以及该最佳组合产生的数据（如上图运行结果所示）。
- 如果想看更加详细和全面的过程，也就是：
    - 所有可能的组合的详细数据，如Action 1+2+3的明细、Action 1+2+4的明细、Action 1+2+5的明细、....
    - 所有可能的组合从高到低排列，如收益最一的组合是什么，赚多少、收益第二的组合是什么，赚多少、...

- 如想查看所有可能的组合的详细明细，在代码最末尾（倒数几行的位置），将`verbose`设置为`True`即可。

    ![image-20220909114809621](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909114809621.png)

- 将`verbose`设置为`True`后，再右键运行程序。

    - 将会看到所有组合的明细（从1+2+3到14+15+16）。

    ![image-20220909115110782](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909115110782.png)

    - 在14+15+16的组合后面，还显示了这些全部组合从高到低的排名。如Rank 1即为最佳组合10+11+12，能使收益最大化为7478408.97。

        ![image-20220909115308388](C:\Users\25132\AppData\Roaming\Typora\typora-user-images\image-20220909115308388.png)
