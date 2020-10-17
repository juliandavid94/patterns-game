import pygame,random,math,copy

pygame.init()
colors_players = [(37,7,255),(35,183,253),(48,254,241),(19,79,251),(255,7,230),(255,7,23),(6,254,13)]
colors_cells = [(80,252,54),(36,244,255),(243,31,46),(4,39,243),(254,6,178),(255,211,7),(216,6,254),(145,255,7),(7,255,182),(255,6,86),(147,7,255)]
colors_viruses = [(66,254,71)]
screen_width, screen_height = (800,500)
surface = pygame.display.set_mode((screen_width,screen_height))
t_surface = pygame.Surface((95,25),pygame.SRCALPHA) #transparent rect for score
t_lb_surface = pygame.Surface((155,278),pygame.SRCALPHA) #transparent rect for leaderboard
t_surface.fill((50,50,50,80))
t_lb_surface.fill((50,50,50,80))
pygame.display.set_caption("AgarUs.io")
cell_list = list()
enemy_list = list()
clock = pygame.time.Clock()
try:
    font = pygame.font.Font("Ubuntu-B.ttf",20)
    big_font = pygame.font.Font("Ubuntu-B.ttf",24)
except:
    print("Font file not found: Ubuntu-B.ttf")
    font = pygame.font.SysFont('Ubuntu',20,True)
    big_font = pygame.font.SysFont('Ubuntu',24,True)

def drawText(message,pos,color=(255,255,255)):
        surface.blit(font.render(message,1,color),pos)

def getDistance(pos1,pos2):
    px,py = pos1
    p2x,p2y = pos2
    diffX = math.fabs(px-p2x)
    diffY = math.fabs(py-p2y)

    return ((diffX**2)+(diffY**2))**(0.5)

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = screen_width
        self.height = screen_height
        self.zoom = 0.5

    def centre(self,blobOrPos):
        if(isinstance(blobOrPos,Player)):
            p = blobOrPos
            self.x = (p.startX-(p.x*self.zoom))-p.startX+((screen_width/2))
            self.y = (p.startY-(p.y*self.zoom))-p.startY+((screen_height/2))
        elif(type(blobOrPos) == tuple):
            self.x,self.y = blobOrPos
class ImpostorDecorator:
  def __init__(self, player):
    self.player = player
    self.player.name = "IMPOSTOR"
  def getImpostor(self):
    return self.player
  def updateImpostor(self):
    self.player.update()
    self.killPlayers()
  def killPlayers (self):
    for i in enemy_list:
      if(getDistance((i.x,i.y),(self.player.x, self.player.y))<= self.player.mass/2):
        self.player.mass +=0.5
        enemy_list.remove(i)
class Player:
    def __init__(self,surface,name = ""):
        self.startX = None
        self.x = None
        self.startY = None
        self.y = None
        self.mass = 20
        self.surface = surface
        self.color = colors_players[random.randint(0,len(colors_players)-1)]
        self.name = name
        self.pieces = list()
        piece = Piece(surface,(self.x,self.y),self.color,self.mass,self.name)
        self.initialX = None
        self.initialY = None
    def buildCamera(self,cam_x, cam_y):
      self.startX = cam_x
      self.startY = cam_y
      return self
    def buildPosition(self,pos_x,pos_y):
      self.x = pos_x
      self.y = pos_y
      return self
    def buildRandomMovement(self, x, y):
      self.initialX = x
      self.initialY = y
      return self
    def setMovement(self, x, y):
      self.initialX = x
      self.initialY = y
    def update(self):
        self.move()
        self.collisionDetection()

    def collisionDetection(self):
        for cell in cell_list:
            if(getDistance((cell.x,cell.y),(self.x,self.y)) <= self.mass/2):
                self.mass+=0.5
                cell_list.remove(cell)
    def move(self):
        #print('Movimiento',pygame.mouse.get_pos())
        #print('self.initialY',self.initialY)
        #print('self.initialX',self.initialX)
        if(self.initialX is None and self.initialY is None):
          dX,dY = pygame.mouse.get_pos()
        else:
          dX,dY = (self.initialX, self.initialY)
        rotation = math.atan2(dY-(float(screen_height)/2),dX-(float(screen_width)/2))*180/math.pi
        speed = 5-1
        vx = speed * (90-math.fabs(rotation))/90
        vy = 0
        if(rotation < 0):
            vy = -speed + math.fabs(vx)
        else:
            vy = speed - math.fabs(vx)
        if vx > 0 and self.x < 2000:
          self.x += vx
        elif vx < 0 and self.x > 0:
          self.x += vx
        elif self.initialX is not None and self.initialY is not None:
          self.setMovement(random.randint(0,800),random.randint(0,500))
        if vy > 0 and self.y < 2000:
          self.y += vy
        elif vy < 0 and self.y > 0:
          #print('arriba')
          self.y += vy
        elif self.initialX is not None and self.initialY is not None:
          self.setMovement(random.randint(0,800),random.randint(0,500))
    def feed(self):
        pass

    def split(self):
        pass

    def draw(self,cam):
        col = self.color
        zoom = cam.zoom
        x = cam.x
        y = cam.y
        pygame.draw.circle(self.surface,(col[0]-int(col[0]/3),int(col[1]-col[1]/3),int(col[2]-col[2]/3)),(int(self.x*zoom+x),int(self.y*zoom+y)),int((self.mass/2+3)*zoom))
        pygame.draw.circle(self.surface,col,(int(self.x*cam.zoom+cam.x),int(self.y*cam.zoom+cam.y)),int(self.mass/2*zoom))
        if(len(self.name) > 0):
            fw, fh = font.size(self.name)
            drawText(self.name, (self.x*cam.zoom+cam.x-int(fw/2),self.y*cam.zoom+cam.y-int(fh/2)),(50,50,50))

class Piece:
    def __init__(self,surface,pos,color,mass,name,transition=False):
        self.x,self.y = pos
        self.mass = mass
        self.splitting = transition
        self.surface = surface
        self.name = name

    def draw(self):
        pass

    def update(self):
        if(self.splitting):
            pass

class Cell:
    def __init__(self,surface):
        self.x = random.randint(20,1980)
        self.y = random.randint(20,1980)
        self.mass = 7
        self.surface = surface
        self.color = colors_cells[random.randint(0,len(colors_cells)-1)]
    def setPosition (self,pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
    def setSurface (self,surface):
        self.surface = surface
    def setColor (self):
        self.color = colors_cells[random.randint(0,len(colors_cells)-1)]
    def change_color(self):
        self.color = colors_cells[random.randint(0,len(colors_cells)-1)]
    def draw(self,cam):
        pygame.draw.circle(self.surface,self.color,(int((self.x*cam.zoom+cam.x)),int(self.y*cam.zoom+cam.y)),int(self.mass*cam.zoom))

class Protoype:
    def __init__(self):
        self.number = 100
        self.cell_p = None
    def setNumber(self,number_in):
        self.number = number_in
    def setCell(self, cell):
        self.cell_p = cell
    def spawn_cells(self):
        for i in range(self.number):
            if self.cell_p is None:
                self.cell_p = Cell(surface)
                cell_list.append(self.cell_p)
                self.putClon(self.cell_p)
            else:
              self.putClon(self.getClon())
              
    def putClon(self, cell):
      cell_list.append(cell)
    def getClon(self):
      prueba = copy.copy(self.cell_p)
      prueba.setPosition(random.randint(20,1980),random.randint(20,1980))
      prueba.change_color()
      return prueba
                
            

def draw_grid():
    for i in range(0,2001,25):
        pygame.draw.line(surface,(230,240,240),(0+camera.x,i*camera.zoom+camera.y),(2001*camera.zoom+camera.x,i*camera.zoom+camera.y),3)
        pygame.draw.line(surface,(230,240,240),(i*camera.zoom+camera.x,0+camera.y),(i*camera.zoom+camera.x,2001*camera.zoom+camera.y),3)

camera = Camera()
player_position = random.randint(100,400)
blob = Player(surface,"ElMugre").buildCamera( player_position, player_position).buildPosition(player_position,player_position)
enemy = Player(surface,"Melascula").buildPosition(random.randint(100,400),random.randint(100,400)).buildRandomMovement(random.randint(0,800), random.randint(0,500))
enemy_list.append(enemy);
impostor= None
cellProto = Protoype()
cellProto.spawn_cells()

def draw_HUD():
    w,h = font.size("Score: "+str(int(blob.mass*2))+" ")
    surface.blit(pygame.transform.scale(t_surface,(w,h)),(8,screen_height-30))
    surface.blit(t_lb_surface,(screen_width-160,15))
    drawText("Score: " + str(int(blob.mass*2)),(10,screen_height-30))
    surface.blit(big_font.render("Leaderboard",0,(255,255,255)),(screen_width-157,20))
    drawText("1. G #1",(screen_width-157,20+25))
    drawText("2. G #2",(screen_width-157,20+25*2))
    drawText("3. ISIS",(screen_width-157,20+25*3))
    drawText("4. ur mom",(screen_width-157,20+25*4))
    drawText("5. w = pro team",(screen_width-157,20+25*5))
    drawText("6. jumbo",(screen_width-157,20+25*6))
    drawText("7. [voz]plz team",(screen_width-157,20+25*7))
    drawText("8. G #3",(screen_width-157,20+25*8))
    drawText("9. doge",(screen_width-157,20+25*9))
    if(blob.mass <= 500):
        drawText("10. G #4",(screen_width-157,20+25*10))
    else:
        drawText("10. Viliami",(screen_width-157,20+25*10),(210,0,0))

while(True):
    clock.tick(70)
    cellProto.setNumber(1)
    cellProto.spawn_cells()
    for e in pygame.event.get():
        if(e.type == pygame.KEYDOWN):
            if(e.key == pygame.K_c):
              enemy_two = Player(surface,"Zeldris_"+str(len(enemy_list))).buildPosition(random.randint(0,800),random.randint(0,500)).buildRandomMovement(random.randint(0,800), random.randint(0,500))
              enemy_list.append(enemy_two)
            if(e.key == pygame.K_i):
              impostor = ImpostorDecorator(enemy_list[random.randint(0,len(enemy_list)-1)])
            if(e.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if(e.key == pygame.K_SPACE):
                blob.split()
            if(e.key == pygame.K_w):
                blob.feed()
        if(e.type == pygame.QUIT):
            pygame.quit()
            quit()
    blob.update()
    if impostor is not None:
      impostor.updateImpostor()
    for k in enemy_list:
      k.update();
    
    camera.zoom = 1/(blob.mass)+0.3
    camera.centre(blob)
    surface.fill((242,251,255))
    #surface.fill((0,0,0))
    draw_grid()
    for c in cell_list:
        c.draw(camera)
    blob.draw(camera)
    if impostor is not None:
      impostor.getImpostor().draw(camera)
    for k in enemy_list:
      k.draw(camera);
    draw_HUD()
    pygame.display.flip()
