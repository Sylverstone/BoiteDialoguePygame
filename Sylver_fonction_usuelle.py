import pygame

def draw_text_(text, font = "Comic Sans Ms", color = (0,0,0), x = 0, y = 0,reference_center_x = None,contener = None,size = 20,importer = False, center_multi_line_y = False, ombre = False,center_multi_line = False):
    """Fonction affichant un texte a l'écran

    Args:
        text (str): texte a image_userr
        font (str, optional): nom de la police a image_userr. Defaults to "Comic Sans Ms".
        color (tuple, optional): couleur du texte a image_userr. Defaults to (0,0,0).
        x (int, optional): position en x du texte a image_userr. Defaults to 0.
        y (int, optional): position en y du texte a image_userr. Defaults to 0.
        reference_center_x (pygame.Surface, optional): Surface sur laquelle le texte doit être centré en x. Defaults to None.
        contener (pygame.Surface, optional): Surface sur laquelle le texte doit être image_userr. Defaults to screen.
        size (int, optional): taille du texte a image_userr. Defaults to 20.
        importer (bool, optional): Variable indiquant si la varible n'est pas native a pygame ou non. Defaults to False.
        center_multi_line_y (bool, optional): Variable indiquant si le texte est centrer en y (pour les textes avec \\n). Defaults to False.
        ombre (bool, optional): Variable indiquant si le texte doit comporter une ombre. Defaults to False.
        center_multi_line (bool, optional): Variable indiquant si le texte est centrer en x (pour les textes avec \\n). Defaults to False.
    """
    
    text = str(text) #transformer le texte en str 
    all_text = text.split("\n")
    if not importer:
        font_ = pygame.font.SysFont(font, size)
    else:
        font_ = pygame.font.Font(font,size)
    #boucle pour image_userr tout les textes de all_text
    
    for enum,text in enumerate(all_text):
        if center_multi_line:
            if reference_center_x==None:
                x = contener.get_rect()[2]/2 - font_.size(text)[0]/2
            else:
                x = reference_center_x.get_rect()[2]/2 - font_.size(text)[0]/2
        if center_multi_line_y:
            y = contener.get_rect()[3]/2 - font_.size(text)[1] * len(all_text)/2
        if ombre:
            text_ = font_.render(str(text), True, (0,0,0))            
            contener.blit(text_, (x+1,y+(size+2)*enum))
        text_ = font_.render(str(text), True, color)
        contener.blit(text_, (x,y+(size + 2)*enum))
        
def font(font_name,size,importer = False):
    if not importer:
        return pygame.font.SysFont(font_name,size)
    return pygame.font.Font(font_name,size)

def make_line_n(text : str,font : pygame.font,size_max : int):
    """Fonction permettant de faire le coupage d'un texte par rapport a son contenaire,
    dans cette version de make_line, des \n sont ajouter au texte

    # Args:
        text (str): text que l'on choisi
        font (pygame.font): la police attribué a ce text
        size_max (int): la taille maximum a ne pas depasser

    # Returns:
        (list,int,float): Renvoie la liste de coupages des caractères, renvoie le nombre de ligne qu'occupe le texte, renvoie la hauteur qu'occupe le texte
    
    * Liste de coupages : liste comportant les indices où une nouvelle ligne commence pour le texte
    """
    line = 1
    start = 0
    i = 0
    while i < len(text):
        size = font.size(text[start:i])[0]
        if size + 20 > size_max:
            
            w = -1
            while text[start:i][w] != " " and abs(w) < len(text[start:i]):
                w -= 1
            if abs(w) == len(text[start:i]):
                #dans le cas ou il n'y a pas d'espace avant le mot
                w = -1
            i += w #i recule jusqua la position de l'espace, pour eviter de couper un mot
            start = i
            line+=1
            text = text[0:i] + "\n" + text[i:]
        elif text[start:i][-1:] == "\n":
            line += 1
            start = i
        i+=1            
    
    y = font.size(text)[1] + font.size(text)[1] * (line-1)
    return text,line,y


