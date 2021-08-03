import pygame
import os

upgrade_menu_image = pygame.image.load(os.path.join("images","upgrade_menu.png"))
upgrade = pygame.image.load(os.path.join("images", "upgrade.png"))
sell = pygame.image.load(os.path.join("images", "sell.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        self.upgrade_menu = pygame.transform.scale(upgrade_menu_image, (200, 200))
        self.upgrade = pygame.transform.scale(upgrade, (60, 40))
        self.sell = pygame.transform.scale(sell , (40, 40))
        self.rect = self.upgrade_menu.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y= y
        self.__buttons =[Button(upgrade,"upgrade",x-31, y-91),Button(sell,"sell",x-20, y+55)] # (Q2) Add buttons here
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.upgrade_menu, self.rect)
        # draw button
        win.blit(self.upgrade, (self.x-31,self.y-91 ))
        win.blit(self.sell, (self.x-20 ,self.y+55))
        # (Q2) Draw buttons here
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name

        self.button_sell_rect = pygame.Rect(x, y, 40, 40)
        self.button_upgrade_rect = pygame.Rect(x, y, 60, 40)
    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return self.button_upgrade_rect.collidepoint(x, y)
        return self.button_sell_rect.collidepoint(x, y)
        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name
        pass






