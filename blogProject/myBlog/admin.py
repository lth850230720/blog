from django.contrib import admin

# Register your models here.
from .models import Author,Tag,Category,BlogBook

class AuthorAdmin(admin.ModelAdmin):
    def author_name(self):
        return self.author_name
    def isDelete(self):
        if self.isDelete:
            return "删除"
        else:
            return "未删除"
    def mainKey(self):
        return self.pk
    def author_date(self):
        return self.author_date
    mainKey.short_description = '主键'
    author_name.short_description='作者名'
    author_date.short_description='创建时间'
    isDelete.short_description='是否删除'
    list_display = [mainKey,author_name,author_date,isDelete]
    search_fields =['author_name']

class TagAdmin(admin.ModelAdmin):
    def tag_name(self):
        return self.tag_name
    def isDelete(self):
        if self.isDelete:
            return "删除"
        else:
            return "未删除"
    def mainKey(self):
        return self.pk
    mainKey.short_description = '主键'
    tag_name.short_description='标签名'
    isDelete.short_description='是否删除'
    list_display = [mainKey,tag_name,isDelete]
    search_fields =['tag_name']

class CategoryAdmin(admin.ModelAdmin):
    def category_name(self):
        return self.category_name
    def isDelete(self):
        if self.isDelete:
            return "删除"
        else:
            return "未删除"
    def mainKey(self):
        return self.pk
    mainKey.short_description = '主键'
    category_name.short_description='标签名'
    isDelete.short_description='是否删除'
    list_display = [mainKey,category_name,isDelete]
    search_fields =['category_name']

class BlogBookAdmin(admin.ModelAdmin):
    def blog_title(self):
        return self.blog_title
    def blog_body(self):
        return self.blog_body
    def created_time(self):
        return self.created_time
    def modified_time(self):
        return self.modified_time
    def category(self):
        return self.category
    def tag(self):
        return self.tags
    def isDelete(self):
        if self.isDelete:
            return "删除"
        else:
            return "未删除"
    def mainKey(self):
        return self.pk
    mainKey.short_description = '主键'
    blog_title.short_description='博客标题'
    blog_body.short_description='博客内容'
    isDelete.short_description='是否删除'
    tag.short_description='标签'
    category.short_description='分类'
    created_time.short_description='创建时间'
    modified_time.short_description='修改时间'
    list_display = [mainKey,blog_title,blog_body,tag,category,created_time,modified_time,isDelete]
    search_fields =['blog_title']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(BlogBook,BlogBookAdmin)