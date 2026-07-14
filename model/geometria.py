import math


class Geometria:

    @staticmethod
    def distancia(x1, y1, x2, y2, px, py) :
        # Vetor direção do segmento (AB)
        dx = x2 - x1
        dy = y2 - y1
        
        # Comprimento do segmento ao quadrado
        ab_len_sq = dx**2 + dy**2
        
        # Caso o segmento seja apenas um ponto (A e B são iguais)
        if ab_len_sq == 0:
            return math.sqrt((px - x1)**2 + (py - y1)**2)
        
        # Vetor do ponto A ao ponto P (AP)
        ap_x = px - x1
        ap_y = py - y1
        
        # Produto escalar de AP e AB dividido pelo comprimento ao quadrado (fator t)
        t = (ap_x * dx + ap_y * dy) / ab_len_sq
        
        # Limita t entre 0 e 1 para garantir que a projeção fique dentro do segmento
        t = max(0.0, min(1.0, t))
        
        # Coordenadas do ponto mais próximo no segmento
        ponto_proximo_x = x1 + t * dx
        ponto_proximo_y = y1 + t * dy 
        
        return math.sqrt((px - ponto_proximo_x)**2 + (py - ponto_proximo_y)**2)
    
    @staticmethod
    def tres_pontos_alinhados(p1, p2, p3):
        """Verifica se 3 pontos 2d estão alinhados em uma linha reta, cada ponto deve ser uma tupla ou lista de (x,y)"""
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        
        # Calculate the cross product of vectors (p2-p1) and (p3-p2)
        # Formula: (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
        cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
        
        # Use a small tolerance for floating-point numbers
        return abs(cross_product) < 1e-12