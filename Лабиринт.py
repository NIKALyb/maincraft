#подключение библиотек
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
#очищение
mc.setBlocks(0,64,0,50,100,30,0)
#телепортация
mc.player.setTilePos(0,80,0)
#пол
mc.setBlocks(0,63,0,50,63,30,4)
#стены
mc.setBlocks(0,63,0,50,66,30,4)
#лабиринт
mc.setBlocks(0,64,1,24,67,2,0)
mc.setBlocks(24,64,2,23,67,13,0)
mc.setBlocks(25,64,7,35,67,8,0)
mc.setBlocks(35,64,7,36,67,28,0)
mc.setBlocks(5,64,1,4,67,14,0)
mc.setBlocks(4,64,14,24,67,15,0)
mc.setBlocks(14,64,15,15,67,29,0)
mc.setBlocks(15,64,29,1,67,28,0)
mc.setBlocks(35,64,28,38,67,27,0)
mc.setBlocks(37,64,16,45,67,17,0)
mc.setBlocks(37,64,7,45,67,8,0)
mc.setBlocks(45,64,7,44,67,29,0)
#вход выход
mc.setBlocks(0,63,0,0,66,3,22)
mc.setBlocks(0,65,1,0,64,2,0)
mc.setBlocks(0,63,27,0,66,30,57)
mc.setBlocks(0,64,28,0,65,29,0)


