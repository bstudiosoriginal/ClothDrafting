class InputParameters:

    def __init__(self) -> None:
        self._Kg = 175
        self._Ow = 105
        self._Tw = 82
        self._Gw = 99
        self._Hs = 8.5
        self._Rh = 25
        self._T = 44
        self._G = 8
        self._L = 79
        self._Bt = 18
        self._Rb = 23
        self._Ad = 17
        self._Bb = 25
        self._Bau = 23
        

    @property
    def Kg(self):
        """
        height
        """
        return self._Kg
    
    @property
    def Kh(self):
        """
        height
        """
        return self._Kg
    
    @property
    def Ow(self):
        """
        chest
        """
        return self._Ow
    
    @property
    def Bu(self):
        """
        chest
        """
        return self._Ow
    
    @property
    def Tw(self):
        """
        waist
        """
        return self._Tw
    
    @property
    def Tu(self):
        """
        waist
        """
        return self._Tw
    
    @property
    def Gw(self):
        """
        Hip or seat girth
        """
        return self._Gw
    
    @property
    def Hu(self):
        """
        Hip or seat girth
        """
        return self._Gw
    
    @property
    def Hs(self):
        """
        Back neck
        """
        return self._Hs
    
    @property
    def Rh(self):
        """
        Depth of scye at back
        """
        return self._Rh
    
    @property
    def T(self):
        """
        Waist lenght
        """
        return self._T
    
    @property
    def G(self):
        """
        Depth of hip/seat
        """
        return self._G
    
    @property
    def L(self):
        """
        Length of coat
        """
        return self._L
    
    @property
    def Bt(self):
        """
        Depth of chest or front depth of scye
        """
        return self._Bt
    
    @property
    def Rb(self):
        """
        Width of back
        """
        return self._Rb
    
    @property
    def Ad(self):
        """
        Armscye width or diameter
        """
        return self._Ad
    
    @property
    def Bb(self):
        """
        Width of chest/bust
        """
        return self._Bb
    
    @property
    def B(self):
        """
        Width of chest/bust
        """
        return self._Bb
    
    @property
    def Bau(self):
        """
       Front width of waist
        """
        return self._Bau
    
    @property
    def Lv(self):
        """
        Front width of waist
        """
        return self._Bau
    
    @property
    def U(self):
        """
        Front width of waist
        """
        return self._Bau
    

class BackPanel():

    def __init__(self, params: InputParameters) -> None:
        self.params = params
        # select an initial point W
        self.W = [5, 90]
        self.plot_points = []

    def create(self):
        pass

    def _start_line_1(self):
        # drawing a line from point W
        self.plot_points.append(self.W)

        # mark the positon of the points from here
        Rh_point = self.W[1] - self.params.Rh