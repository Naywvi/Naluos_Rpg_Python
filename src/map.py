from dataclasses import dataclass
from src.player import NPC

import pygame, pytmx, pyscroll

@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str

@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    trees: list[pygame.Rect]
    roofs: list[pygame.Rect]
    layer_reset: list[pygame.Rect]
    layer_change: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[NPC]
    
class MapManager:
    def __init__(self, screen, player) -> None:
        self.maps = dict()
        self.music = pygame.mixer.music
        self.music2 = pygame.mixer.music
        self.player = player
        self.screen = screen
        self.current_map = "spawn_house"
        self.collar = False
        self.weapon = False
        self.ring = False
        self.quest1 = False
        self.quest2 = False
        
        self.register_map("holled", portals=[
            Portal(from_world="holled", origin_point="exit_holled", target_world="snow_map", teleport_point="exit_holled")
        ], npcs=[
            NPC("ghost_holled", nb_points=1, dialog=["?????????? *-1HP*[F] >", "*Pas d'arme pour se défendre* [F] >"])
        ])
        self.register_map("house_snow", portals=[
            Portal(from_world="house_snow", origin_point="exit_house_snow", target_world="snow_map", teleport_point="exit_house_snow")
        ], npcs=[
            NPC("black_guy", nb_points=2, dialog=["Salut mon fwèwe ! [F] >","Ca a la pêche ? [F] >", "Le fowegeron cherche son mawteau, va le vuaw [F] >"]),
            NPC("black_woman", nb_points=2, dialog=["*Tsshhhpppp* [F] >", "Gé féw lé ménage là ! [F] >", "*giffle* GE FEW LE MENAGE ! *-1HP* [F] >"])
            ])
        self.register_map("peche", portals=[
            Portal(from_world="peche", origin_point="exit_peche", target_world="snow_map", teleport_point="exit_peche")
        ], npcs=[
            NPC("fisher_man",nb_points=1, dialog=[
                "Salut toi ! [F] >",
                "Ah c'est toi le chef de la ville de Naluosa ! [F] >",
                "Oh si tu savais, la pêche ici a changé [F] >",
                "A l'ancienne, le temps était tout le temps ensoleillé ... [F] >",
                "Quand j'étais jeune, mes enfants étaient épanouis[F] >",
                "D'ailleurs ils sont partis d'ici ... [F] >",
                "Ca fait longtemps que je ne les ai pas vu *triste* !",
                "Bah tiens, ça me fait penser à une chose ! [F] >",
                "J'ai caché dans un buisson une bague en diamant ! [F]",
                "Ah oui je m'en souviens, va voir en bas, près du bateau ! [F] >"
                ])
        ])
        self.register_map("boat", portals=[
            Portal(from_world="boat", origin_point="exit_boat", target_world="snow_map", teleport_point="exit_boat")
        ], npcs=[
            NPC("ring", nb_points=1, dialog=["*item trouvé !* [F] >"])
        ])
        self.register_map("caravane", portals=[
            Portal(from_world="caravane", origin_point="exit_caravane", target_world="snow_map", teleport_point="exit_caravane")
        ], npcs=[
            NPC("roumaine", nb_points=1, dialog=[])
        ])
        self.register_map("grange", portals=[
            Portal(from_world="grange", origin_point="exit_grange", target_world="snow_map", teleport_point="exit_grange")
        ])
        self.register_map("forge", portals=[
            Portal(from_world="forge", origin_point="exit_forge", target_world="snow_map", teleport_point="exit_forge")
        ], npcs=[
            NPC("forgeron", nb_points=4, dialog=["Bonjour monsieur *grogne* ! [F] >", "Est-ce que t'as trouvé mon marteau ? [F] >", "Ah dommage ... Si tu le trouves, préviens-moi... [F] >"])
        ])
        self.register_map("snow_map", portals=[
            Portal(from_world="snow_map", origin_point="exit_snow_map", target_world="world", teleport_point="exit_snow_map"),
            Portal(from_world="snow_map", origin_point="enter_holled", target_world="holled", teleport_point="enter_holled"),
            Portal(from_world="snow_map", origin_point="enter_boat", target_world="boat", teleport_point="enter_boat"),
            Portal(from_world="snow_map", origin_point="enter_caravane", target_world="caravane", teleport_point="enter_caravane"),
            Portal(from_world="snow_map", origin_point="enter_grange", target_world="grange", teleport_point="enter_grange"),
            Portal(from_world="snow_map", origin_point="enter_forge", target_world="forge", teleport_point="enter_forge"),
            Portal(from_world="snow_map", origin_point="enter_peche", target_world="peche", teleport_point="enter_peche"),
            Portal(from_world="snow_map", origin_point="enter_house_snow", target_world="house_snow", teleport_point="enter_house_snow")
        ], npcs=[
            NPC("snow_guy", nb_points=1, dialog=[
                "Bienvenue à toi ! [F] >", 
                "Ici il fait froid depuis quelques temps. [F] >", 
                "Beaucoup d'habitants sont donc partis. [F] >",
                "Ils ont surement dus emmenagés de l'autre côté... [F] >",
                "Les visiteurs se font rare !",
                "En ce moment il y a quelques vols ![F] >",
                "Fait attention à tes affaires ! [F] >"
                ]),
        ])
        self.register_map("donjon", portals=[
            Portal(from_world="donjon", origin_point="exit_donjon_small", target_world="world", teleport_point="exit_donjon_small"),
            Portal(from_world="donjon", origin_point="exit_donjon_small2", target_world="world", teleport_point="exit_donjon_small2")
        ])
        self.register_map("spawn_house", portals=[
            Portal(from_world="spawn_house", origin_point="exit_spawn_house", target_world="world", teleport_point="exit_spawn_house")
        ])
        self.register_map("house_one", portals=[
            Portal(from_world="house_one", origin_point="exit_house_one", target_world="world", teleport_point="exit_house_one")
        ], npcs=[
            NPC("pink_girl", nb_points=7, dialog=["Me dérange pas s'il te plait ! [F] >", "Je cherche mon collier... [F] >", "Tu pourrais demander aux autres ? [F] >", "Reviens me voir si tu l'as trouvé ! [F] >"])
        ])
        self.register_map("house_two", portals=[
            Portal(from_world="house_two", origin_point="exit_house_two", target_world="world", teleport_point="exit_house_two")
        ], npcs=[
            NPC("barmans", nb_points=2, dialog=["Et beh, le mari de Paula ! [F] >","J'crois c'est Mohamed, il a cassé son ramadan, [F] >","Hier soir il était ici, 5 pintes de bières, [F] >", "Je peux te dire, il était bien déchiré ! [F] >"]),
            NPC("green_guy", nb_points=6, dialog=["Laisse-moi tranquille connard ! [F] >","*frappe* LAISSE-MOI TRANQUILLE J'AI DIT *-1HP !* [F] >","Que des casse-couilles ici ! [F] >"])
        ])
        self.register_map("house_tree", portals=[
            Portal(from_world="house_tree", origin_point="exit_house_tree", target_world="world", teleport_point="exit_house_tree")
        ], npcs=[
            NPC("defaults", nb_points=1, dialog=["Toi aussi tu l'entends... ? [F] >", "Ils sont là... [F] >","Tu le vois toi aussi ...? [F] >","Il est à côté de toi... [F] >"])    
        ])
        self.register_map("screamer", portals=[
            Portal(from_world="screamer", origin_point="exit_screamer", target_world="world", teleport_point="exit_screamer")
        ], npcs=[
            NPC("julia_girl", nb_points=6, dialog=["... [F] >", "... [F] >", "LAISSE-MOI TRANQUILLE !!! [F] >", "... [F] >", "MOHAMMED... [F] >","CE CHIENN !!! [F] >","IL A PASSE SA NUIT AVEC... [F] >", "CETTE PUTAIN DE 'GRATTE LA CHATTE' [F] >", "C'EST FINI ! PLUS JAMAIS DE CE CRETIN ! [F] >"])
        ])
        self.register_map("world", portals=[
           Portal(from_world="world", origin_point="enter_donjon_small", target_world="donjon", teleport_point="enter_donjon_small"),
            Portal(from_world="world", origin_point="enter_donjon_small2", target_world="donjon", teleport_point="enter_donjon_small2"),
            Portal(from_world="world", origin_point="enter_spawn_house", target_world="spawn_house", teleport_point="enter_spawn_house"),
            Portal(from_world="world", origin_point="enter_house_one", target_world="house_one", teleport_point="enter_house_one"),
            Portal(from_world="world", origin_point="enter_house_two", target_world="house_two", teleport_point="enter_house_two"),
            Portal(from_world="world", origin_point="enter_house_tree", target_world="house_tree", teleport_point="enter_house_tree"),
            Portal(from_world="world", origin_point="enter_screamer", target_world="screamer", teleport_point="enter_screamer"),
            Portal(from_world="world", origin_point="enter_snow_map", target_world="snow_map", teleport_point="enter_snow_map")
        ], npcs=[
            NPC("villager_welcome", nb_points=2, dialog=[
                "Chef, enfin tu es réveillé ! [F] >", 
                "Aujourd'hui, Laura a perdu son chien dans la forêt ! [F] >", 
                "Luc et Paul ont aussi perdu quelques objets... [F] >",
                "J'ai entendu au village qu'il y aurait des 'montres' dans la mine. [F] >",
                "Sûrement des histoires d'enfant ... [F] >",
                "Ah oui ! Très étrange le marie à Julia n'est pas rentré hier [F] >",
                "Il a sûrement dû s'endormir saoule près d'un arbre ... [F] >",
                "Ce n'est pas la première fois qu'il nous fait ce coup. [F] >",
                ]),
            NPC("green_girl", nb_points=1, dialog=[
                "Bonjour chef, ! [F] >", 
                "Cette nuit des bruits étranges ont survenu ! [F] >",
                "Ils provenaient de la fôret. [F] >",
                "Je ne sais pas quoi en penser... [F] >"
                ]),
            NPC("naked_girl", nb_points=9, dialog=[
                "Coucou toi ! [F] >","C'était bien hier avec Mohammed ! [F] >", "Ah oui, tiens le collier de ... Je sais pas ! [F] >", "*item récupéré* [F] >", "Tu voudrais pas te joindre à moi ? [F] >", "*se gratte la chatte* [F] >", "Grrrr [F] >"
                ]),
            NPC("invisible", nb_points=1, dialog=["Vers la ville de Sinaloa... [F] >"]),
            NPC("neige", nb_points=1, dialog=["... [F] >"]),
            NPC("hat_girl", nb_points=4, dialog=["Bonjour chef du village ! *rougie* [F] >", "Les habitants commencent à se faire rare ici... [F] >", "Comment se fait-il que les habitants partent ? Ou... [F] >", "Dispar... ? [F]","Enfin bref... Bonne journée ! [F] >"]),
            NPC("luc", nb_points=4, dialog=["[Luc] J'ai perdu mon Sac *stresse*! [F] >", "Je ne sais plus quoi faire ! [F] >"]),
            NPC("paul", nb_points=4, dialog=["[Paul] J'ai perdu ma bague *stresse*! [F] >","S'il-te-plaît, retrouve-la ! [F] >"])
        ])
        
        self.teleport_player("spawn_player_world")
        self.teleport_npcs()
        
    def check_npc_collisions(self, dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC:
                
                if sprite.name == "villager_welcome":
                    if sprite.interactions == 0:
                        sprite.dialog
                    else:  
                        sprite.dialog = ["Y'a une meuf à poil dans la fôret ! [F] >"]
                    sprite.interactions += 1
                    
                if sprite.name == "naked_girl":
                    if sprite.interactions == 0:
                        sprite.dialog
                        if not self.player.inventory.has_already("Collier"): self.player.inventory.add("Collier")
                        sprite.nb_points = 1
                    elif sprite.interactions == 1:
                        sprite.dialog = ["Ah c'est bon ? [F] >", "Tu t'es décidé coquin ? [F] >", "*se gratte la chatte* [F] >"]
                    sprite.interactions += 1
                
                if sprite.name == "pink_girl":
                    if self.player.inventory.has_already("Collier") and self.collar == False: 
                        sprite.dialog = ["Ah yes ! [F] >", "Merci beaucoup [F] >", "C'est mon collier porte bohneur [F] >","Je l'aurais bien offert à Julia mais elle pleure dans la tante [F] >", "Elle ne veut pas qu'on l'a dérange [F] >", "Tiens comme cadeau aussi pour avoir trouver mon collier ! [F] >", "Je sais que c'est rien mais c'est déjâ ça... ! *item récupéré* [F] >"]
                        self.player.inventory.add("Billet d'argent")
                        self.player.inventory.remove("Collier")
                        self.collar = True
                    elif self.player.inventory.has_already("Collier") and self.collar == True:
                        sprite.dialog = ["J'adore cette musique, tu l'aimes pas toi ? [F] >"]
                    elif self.collar == True:
                        sprite.dialog = ["Ah ça fait longtemps ! [F] >", "Julia est toujours entrain de pleurer la pauvre ! [F] >"]
                    sprite.interactions += 1
                
                if sprite.name == "roumaine":
                    if sprite.interactions == 0:
                        sprite.dialog = ["Rah ouééééé... [F] >","La putain de ses morts ! [F] >","Il fait trop froid, ma bière s'est congelée quoi !", "*gloups* *gloups* [F] >","Et t'es qui toi ?! [F] >", "T'es beau gosse toi ! [F] >","Attends ... ?! C'est ... [F] >","C'est pas toi le voleur la putain de tes morts ! [F] >","T'es venu chiné quelque chose ?! [F] >", "Et aussi *gloups* ! [F] >", "J'ai un marteau à vendre [F] >", "Si t'as un p'tit billet j'te le passe [F] >"]
                    else:
                        if self.player.inventory.has_already("Billet d'argent"):
                            sprite.dialog = ["Vas-y tiens, maintenant barre-toi ! *item récupéré* [F] >"]
                            self.player.inventory.add("Marteau")
                            self.player.inventory.remove("Billet d'argent")
                        else:
                            sprite.dialog = ["C'est bon t'as le billet ? [F] >", "Oh sur mes morts tu l'auras pas si t'as pas de billets ! [F] >", "Je veux juste m'acheter des cloppes ! [F] >"]
                    sprite.interactions += 1
                    
                if sprite.name == "black_woman":
                    if sprite.interactions == 0:
                        self.player.hp -= 1
                    else:
                        sprite.dialog = ["DÉGAGE GÉ TÉW DIT ! [F] >"]
                    sprite.interactions += 1
                    
                if sprite.name == "forgeron":
                    if self.player.inventory.has_already("Marteau"): 
                        sprite.dialog = ["Merci monsieur ! [F] >", "Rohhh je la cherchais partout ! [F] >" ,"Tenez comme cadeau *item récupéré* [F] >"]
                        self.player.inventory.add("Epée en fer")
                        self.player.inventory.remove("Marteau")
                    elif self.player.inventory.has_already("Epée en fer"):
                        sprite.dialog = ["Bon c'est bon ... [F] >", "Faudrait me laisser travailler maintenant ... ! [F] >"]
                
                if sprite.name == "green_girl":
                    if sprite.interactions != 0:
                        sprite.dialog = ["En vérité, sa me fait peur tout ça ! [F] >"]
                    sprite.interactions += 1
                
                if sprite.name == "barmans":
                    if sprite.interactions != 0:
                        sprite.dialog = ["Oh putain ! [F] >", "Je sais pas ce qu'il fait depuis tout à l'heure l'autre gars ... [F] >","Il fait flippé un peu. [F] >"]
                    sprite.interactions += 1
                
                if sprite.name == "green_guy":
                    if sprite.interactions == 0:
                        self.player.hp -= 1
                    else:
                        sprite.dialog = ["Mais dégage je t'ai dit, merde ! [F] >", "T'en veux encore plus ?! [F] >"]
                    sprite.interactions += 1
                
                if sprite.name == "ghost_holled":
                    if self.player.inventory.has_already("Epée en fer"):
                        sprite.dialog = ["Tu veux te battre ?! [F] >", "... *Coup d'Epée* [F] >", "Aïeee !!! [F] >", "Ok, tu as gagné, tiens, c'est ça que tu voulais ? [F] >", "Laisse-moi tranquille maintenant *items récupérés* [F] >","Surtout n'en parle à personne ! [F] >"]
                        if not self.player.inventory.has_already("Sac à dos"): self.player.inventory.add("Sac à dos")
                        else: sprite.dialog = ["Laisse-moi tranquille et n'en parle à personne ! [F] >"]
                    else:
                        self.player.hp -= 1
                
                if sprite.name == "fisher_man":
                    if sprite.interactions != 0:
                        if self.player.inventory.has_already("Bague en diamant"): sprite.dialog = ["Tu l'as trouvé ! [F] >", "Tu peux la garder ! [F] >"]
                        else: sprite.dialog = ["Alors trouvé ? [F] >", "Non ? [F] >","Cherche bien, dans un buisson en bas du bateau ! [F] >"]
                    sprite.interactions += 1
                
                if sprite.name == "ring":
                    if self.ring == False:
                        self.ring = True
                        self.player.inventory.add("Bague en diamant")
                    if sprite.interactions != 0:
                        sprite.dialog = ["*Tu l'as déjâ récupéré* [F] >"]
                    sprite.interactions += 1
                    
                if sprite.name == "luc":
                    if self.player.inventory.has_already("Bague en diamant") and self.quest1 == False:
                        sprite.dialog = ["OHHH TU L'AS TROUVE ! [F] >", "Merci beaucoup, je t'en dois une ! [F] >"]
                        self.player.inventory.remove("Bague en diamant")
                        self.quest1 = True
                    elif self.quest1 == True:
                        sprite.dialog = ["Je t'en devrai toujours une ! [F] >"]
                
                if sprite.name == "paul":
                    if self.player.inventory.has_already("Sac à dos") and self.quest2 == False :
                       sprite.dialog = ["Mon... *larme* [F] >", "Merci beaucouuuup ! [F] >"]
                       self.quest2 = True
                       sprite.nb_points = 1
                    elif self.quest2 == True:
                        sprite.dialog = ["*content* [F] >"]
                        
                dialog_box.execute(sprite.dialog)

    def welcome_message(self, dialog_box):
        dialog_box.execute([
            "Bienvenue à toi dans Naluos Aventure ! [H] >", 
            "Ce message est juste destiné à le lire, ne fais rien ! [H] >",
            "Pour bouger utilise les fléches du clavier ! [H] >", 
            "Il est possible de communiquer avec les PNJ ! [H] >",
            "Il te suffit d'appuyer sur [ESPACE] devant eux ! [H] >",
            "Surtout ne pas spam la barre [ESPACE] ! [H]",
            "Il faut aussi continuer les conversations avec [F] ! [H]",
            "Petite chose, il faut que le PNJ ne bouge plus pour lui parler ! [H] >",
            "Pour cela, mets-toi devant lui / en bas ! [H] >",
            "Pour ouvrir ton inventaire, appuie sur [E] ! [H] >",
            "Ton nombre de vie est affiché en bas à gauche ! [H] >",
            "Pour revoir ce message si besoin d'aide, ré-appuie sur [H] ! [H] >"])
    
    def delete_message(self, dialog_box):
        dialog_box.execute([])
    
    def inventory_message(self, dialog_box):
        dialog_box.execute([self.player.inventory.get_text()])
    
    def register_map(self, name, portals=[], npcs=[]):
        tmx_data = pytmx.util_pygame.load_pygame(f"./assets/map/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 5
        
        #map affichage des layers
        group = pyscroll.PyscrollGroup(map_layer, default_layer=0)
        group.add(self.player)
        
        for npc in npcs:
            group.add(npc)
        
        #gestion musique
        self.change_music(self.current_map)
        
        #gestion collision
        walls = []
        trees = []
        roofs = []
        layer_change = []
        layer_reset = []
        
        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "arbre":
                trees.append(pygame.Rect(obj.x, obj.y, obj.width,obj.height))
            if obj.type == "toit":
                roofs.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "change":
                layer_change.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "reset":
                layer_reset.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                
        self.maps[name] = Map(name, walls, trees, layer_change, layer_reset, roofs, group, tmx_data, portals, npcs)

    def change_music(self, name):
        self.music.unload()
        self.music.load(f"./assets/music/{name}.mp3")
        self.music.set_volume(0.05)
        self.music.play(loops=-1)
    
    def get_map(self): return self.maps[self.current_map]
    
    def get_group(self): return self.get_map().group
    
    def get_walls(self): return self.get_map().walls
    
    def get_roofs(self): return self.get_map().roofs
    
    def get_trees(self): return self.get_map().trees

    def get_layer_change(self): return self.get_map().layer_change
    
    def get_layer_reset(self): return self.get_map().layer_reset
    
    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)
    
    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs
            
            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()
                
    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)
    
    def check_collision(self):
        
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect =  pygame.Rect(point.x, point.y, point.width, point.height)
                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.change_music(self.current_map)
                    self.teleport_player(copy_portal.teleport_point)
        
        for sprite in self.get_group().sprites():
            
            if type(sprite) is NPC:
                if sprite.feet.colliderect(self.player.rect):
                    sprite.walk_speed = 0
                else:
                    
                    sprite.walk_speed = 1
                    
            
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()                                          #collision
            elif sprite.feet.collidelist(self.get_trees()) > -1:
                self.get_group().change_layer(self.player,14)               #layer pour arbre
            elif sprite.feet.collidelist(self.get_roofs()) > -1:
                self.get_group().change_layer(self.player,13)               #layer pour toit
            elif sprite.feet.collidelist(self.get_layer_change()) > -1:
                self.get_group().change_layer(self.player,0)               #layer change
            elif sprite.feet.collidelist(self.get_layer_reset()) > -1:
                self.get_group().change_layer(self.player,1)               #layer reset
                
            else: self.get_group().change_layer(self.player,0)             #par défaut
            
    
    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def update(self):
        self.get_group().update()
        self.check_collision()
        for npc in self.get_map().npcs:
            npc.move()