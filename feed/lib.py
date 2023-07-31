def aggregrate_tailored_posts(request):
    follow_relationships = request.user.following.all()
    posts = request.user.post_set.all()
    for relationship in follow_relationships:
        posts = posts.union(relationship.following.post_set.all())
    return posts.order_by('-date')