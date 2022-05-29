import pygame


def get_mosaic(img: pygame.Surface):
    clip_images: list[[pygame.Surface], ...] = []

    rect_size = 5
    space = 30

    step = rect_size + space
    for y in range(1, img.get_height() + 1, step):
        clips = []
        for x in range(1, img.get_width() + 1, step):
            clips.append(clip(img, x, y, rect_size, rect_size))
        clip_images.append(clips)

    result_image = pygame.Surface((len(clip_images[0]) * rect_size, len(clip_images) * rect_size))

    x_offset = 0
    y_offset = 0
    for imgs in clip_images:
        for img in imgs:
            result_image.blit(img, (x_offset, y_offset))
            x_offset += rect_size
        x_offset = 0
        y_offset += rect_size
    return result_image


# by DAFLUFFYPOTATO
def clip(surf, x, y, w, h):
    handle_surf = surf.copy()
    clip_rect = pygame.Rect(x, y, w, h)
    handle_surf.set_clip(clip_rect)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


if __name__ == '__main__':
    origin_image = pygame.image.load("image.png")
    mosaic_image = get_mosaic(origin_image)
    pygame.image.save(mosaic_image, "result.png")
