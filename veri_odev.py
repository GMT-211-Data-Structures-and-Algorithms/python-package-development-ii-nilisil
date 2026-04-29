import math

class Point:
    """
    Mekansal bir noktayı temsil eden sınıf.
    """
    def __init__(self, x, y, name=""):
        """
        Nokta objesini başlatır.

        :param x: Noktanın X koordinatı.
        :type x: float
        :param y: Noktanın Y koordinatı.
        :type y: float
        :param name: Noktanın adı (isteğe bağlı).
        :type name: str
        """
        self.x = float(x)
        self.y = float(y)
        self.name = name.strip()

    @classmethod
    def from_file(cls, filepath):
        """
        Belirtilen formatlı bir metin dosyasından noktaları okur.

        :param filepath: Okunacak dosyanın yolu.
        :type filepath: str
        :return: Oluşturulan Point objelerinin listesi.
        :rtype: list
        """
        points = []
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = [line.strip() for line in file if line.strip()]
                
            if not lines or lines[0].lower() != 'point':
                raise ValueError("Geçersiz format: Dosya 'point' ile başlamalı.")
            
            num_points = int(lines[1])
            for i in range(2, 2 + num_points):
                if i < len(lines):
                    parts = lines[i].split(',')
                    if len(parts) >= 3:
                        points.append(cls(parts[0], parts[1], parts[2]))
            return points
        except FileNotFoundError:
            print(f"Hata: {filepath} bulunamadı.")
            return []

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, name='{self.name}')"


class Line:
    """
    Noktalardan oluşan bir çizgiyi temsil eden sınıf.
    """
    def __init__(self, name=""):
        """
        Çizgi objesini başlatır.

        :param name: Çizginin adı.
        :type name: str
        """
        self.name = name.strip()
        self.points = []

    def add_point(self, point):
        """
        Çizgiye yeni bir Point objesi ekler.

        :param point: Eklenecek nokta.
        :type point: Point
        """
        if isinstance(point, Point):
            self.points.append(point)
        else:
            raise TypeError("Sadece Point objeleri eklenebilir.")

    def calculate_length(self):
        """
        Çizginin toplam geometrik uzunluğunu hesaplar.

        :return: Çizginin toplam uzunluğu.
        :rtype: float
        """
        total_length = 0.0
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i+1]
            total_length += math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
        return total_length

    @classmethod
    def from_file(cls, filepath):
        """
        Dosyadan çizgi verilerini okur ve Line objeleri oluşturur.

        :param filepath: Okunacak dosyanın yolu.
        :type filepath: str
        :return: Oluşturulan Line objelerinin listesi.
        :rtype: list
        """
        lines_list = []
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                raw_lines = [line.strip() for line in file if line.strip()]
                
            if not raw_lines or raw_lines[0].lower() != 'line':
                raise ValueError("Geçersiz format: Dosya 'line' ile başlamalı.")
            
            current_line = None
            for i in range(2, len(raw_lines)):
                text = raw_lines[i]
                if ',' in text:
                    parts = text.split(',')
                    if len(parts) >= 2 and current_line is not None:
                        current_line.add_point(Point(parts[0], parts[1]))
                else:
                    current_line = cls(text)
                    lines_list.append(current_line)
            return lines_list
        except FileNotFoundError:
            print(f"Hata: {filepath} bulunamadı.")
            return []

    def __repr__(self):
        return f"Line(name='{self.name}', node_count={len(self.points)})"