from django.db import models

# Create your models here.

#作者
class Author(models.Model):
    author_name    = models.CharField(max_length=20)
    author_date    = models.DateTimeField()
    isDelete = models.BooleanField()
    def __str__(self):
        return "%s"%(self.author_name)
    class Meta:
        verbose_name_plural='作者'


#类型
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    isDelete = models.BooleanField()
    def __str__(self):
        return "%s"%(self.category_name)
    class Meta:
        verbose_name_plural='分类'
#标签
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    isDelete = models.BooleanField()
    def __str__(self):
        return "%s"%(self.tag_name)
    class Meta:
        verbose_name_plural='标签'
        #verbose_name='标签'

#文章
class BlogBook(models.Model):
    blog_title=models.CharField(max_length=100)
    blog_body=models.TextField()
    #评论
    # blog_comment=
    #创建时间
    created_time = models.DateTimeField()
    #修改时间
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    isDelete = models.BooleanField()
    def __str__(self):
        return "%s"%(self.blog_title)
    class Meta:
        verbose_name_plural='博客'

