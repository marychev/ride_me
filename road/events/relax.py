from .go import GoEventRoad


class RelaxEventRoad(GoEventRoad):

    def start(self, acceleration):
        if self.bike.has_collision_rock():
            self.bike.collision_rock()
            return False
        else:
            self.bike.acceleration = acceleration

            if self.bike.speed - acceleration <= 0:
                self.bike.speed = 0
                self.rock.set_x()
                self.finish.set_x()
                return False
            else:
                self.bike.speed -= acceleration
                self.set_distances()
                return True
