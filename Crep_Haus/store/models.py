class Category(models.Model):
    image = models.ImageField(upload_to='uploads/product/', default='path/to/default/image.jpg')