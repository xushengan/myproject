## django 实践指南
### day 1

在pycharm项目的虚拟环境下创建：
project：myproject
app：boards

不知道是公司的问题还是项目环境的问题，使用git同步项目要不就是全量，要不就是同步不成功
最后使用git bash手动建立账户，连接远程仓库remote，通过命令行push成功。

尝试git status 和 git diff功能

命令|功能
--|--
git add |增加文件到commit
git status|看哪个文件被改了，但不具体
git diff|具体看文件被改了哪里
git commit -m "test"|提交
git push | 推送到远程

### day 2
1、学习了在开始项目之前，使用 用例图 去表示用户和 系统应该提供的服务
2、根据用例图设计类，并画出类与类之间的关系
3、根据类图，再django设计模块，虽然这里没有用到sql语句，但是其实都差不多

### 额外关于foreignkey的了解
```
Model
ForeignKey.related_name
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')
```

ForeignKey.related_name
django会自动为模型提供一种反向关系，即在topic里面设置了user的外键，那么user也可以通过related_name来访问topic，比如，现在related_name='topics',则可以通过User.topics来访问topics,否则，默认通过模型名后加_set来访问，如User.topic_set
当related_name = '+'时，表示不需要反向关系

ForeignKey.related_query_name

	The name to use for the reverse filter name from the target model. Defaults to the value of related_name if it is set, otherwise it defaults to the name of the model:

简单来说，related_query_name是在topic需要筛选User时使用的名称如：

```
Topic.object.filter('related_query_name'=sth)
```

### day 3 
url命名空间没有说得太清楚，倒是学到了一些通过正则匹配然后赋值的技巧
base.html用了一下