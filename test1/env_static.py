import numpy as numpy
import pyglet

class ArmEnv(object):
    viewer = None # 首先没有viewer（为了减少运算，没有用到可视化的时候，完全不调用Viewer类）
    
    def __init__(self):
        pass
        
    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        if self.viewer is None: # 如果调用了render，而且没有viewer，就生成一个
            self.viewer = Viewer()
        self.viewer.render() # 使用Viewer中的render功能


class Viewer(pyglet.window.Window):
    bar_thc = 5

    def __init__(self): # 画出手臂等
        # 创建窗口的继承
        # vsync 如果是 True, 按屏幕频率刷新, 反之不按那个频率
        super(Viewer, self).__init__(width=400, height=400, resizable=False, caption='Arm', vsync=False)
        
        # 窗口背景颜色
        pyglet.gl.glClearColor(0, 0, 0, 1)

        # 将手臂的作图信息放入这个 batch
        self.batch = pyglet.graphics.Batch()    # display whole batch at once
        
         # 添加蓝点
        self.point = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,    # 4 corners
            ('v2f', [80, 80,                # location
                     80, 100,
                     100, 100,
                     100, 80]),
            ('c3B', (255, 0, 0) * 4))    # color

        # 添加一条手臂
        self.arm1 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [250, 250,                # location
                     250, 300,
                     260, 300,
                     260, 250]),
            ('c3B', (255, 235, 205) * 4,))    # color
        self.arm2 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [100, 150,              # location
                     100, 160,
                     200, 160,
                     200, 150]), ('c3B', (255, 235, 205) * 4,))
    
    def render(self): # 刷新并呈现在屏幕上
        self._update_arm()
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()

    def on_draw(self): # 刷新手臂等位置
        self.clear() #清屏
        self.batch.draw() #画上batch里面的内容

    def _update_arm(self): # 更新手臂的位置信息
        pass


if __name__ == '__main__':
    env = ArmEnv()
    while True:
        env.render()