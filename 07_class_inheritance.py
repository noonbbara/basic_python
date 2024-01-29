print("챕터01 - <상속>")

# 일반 유닛
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed

  def move(self, location):
    print("[지상 유닛 이동]")
    print("{0} : {1} 방향으로 이동합니다 [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit): # 어택유닛은 유닛을 상속받아서 만들어짐
  def __init__(self, name, hp, speed, damage):
    Unit.__init__(self, name, hp, speed)
    self.damage=damage

  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
    self.hp -= damage
    print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴되었습니다".format(self.name))
    
firebat1 = AttackUnit("파이어뱃", 50, 5, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
print()

print("챕터02 - <다중상속>")

# 날 수 있는 기능을 가진 클래스
class Flyable:
  def __init__(self, flyingSpeed):
    self.flyingSpeed = flyingSpeed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]".format(name, location, self.flyingSpeed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__ (self, name, hp, damage, flyingSpeed):
    AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
    Flyable.__init__(self, flyingSpeed)

  def move(self, location):
    print("[공중 유닛 이동]")
    self.fly(self.name, location)

# 발키리 : 공중 공격 유닛
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
print()

print("챕터03 - <메소드 오버라이딩>")

# 벌쳐 : 지상 유닛, 속도가 빠름
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀 크루저 : 공중 유닛, 탱 딜 다됨
battlecruiser = FlyableAttackUnit("배틀 크루저", 500, 25, 3)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")
print()

print("챕터04 - <pass>")
print("챕터05 - <super>")
# 건물
class BuildingUnit(Unit):
  def __init__(self, name , hp, location):
    # Unit.__init__(self, name, hp, 0) 으로도 사용가능 하지만 super를 사용할 수 도 있음
    super().__init__(name, hp, 0) # super는 괄호를 쓰고 self를 사용하지 않음
    # super는 다중 상속에서는 권장하지 않음
    self.location = location

# 서플라이 디폿 : 건물, 건물 1개마다 8개의 유닛
supplyDepot = BuildingUnit("서플라이 디폿", 500, "7시")
# pass는 아무것도 안하고 일단 넘어간다는 의미
# 게임 오버와 같은 상황에서 사용할 수 있다
print()

print("챕터06 - <퀴즈>")
class House:
  def __init__(self, location, house_type, deal_type, price, completion_year):
    self.location = location
    self.house_type = house_type
    self.deal_type = deal_type
    self.price = price
    self.completion_year = completion_year

  def show_detail(self):
    print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다".format(len(houses)))
for house in houses:
  house.show_detail()