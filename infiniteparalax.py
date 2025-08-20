
class InfiniteParalax():
    def is_offlimits(obj):
        if obj.rect.x < 0 - obj.rect.width//2:

            obj.rect.x = obj.limits[0]

        elif obj.rect.x > obj.limits[0]:

            obj.rect.x = 0 - obj.rect.width//2

        if obj.rect.y < 0 - obj.rect.height//2:

            obj.rect.y = obj.limits[1]

        elif obj.rect.y > obj.limits[1]:

            obj.rect.y = 0 - obj.rect.height//2
