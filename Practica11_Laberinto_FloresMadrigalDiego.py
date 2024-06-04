def count_paths(laberinto):
    m, n = len(laberinto), len(laberinto[0])

    # Si el punto inicial o el punto final son obstáculos, no hay rutas posibles
    if laberinto[0][0] == 1 or laberinto[m-1][n-1] == 1:
        return 0

    # Crear una tabla de dp con el mismo tamaño que el laberinto
    dp = [[0] * n for _ in range(m)]
    
    # Inicializar el punto de partida
    dp[0][0] = 1

    # Llenar la tabla dp
    for i in range(m):
        for j in range(n):
            if laberinto[i][j] == 1:
                dp[i][j] = 0  # No se puede pasar por obstáculos
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    # El valor en dp[m-1][n-1] es el número de rutas posibles al final del laberinto
    return dp[m-1][n-1]

# Ejemplo de uso
laberinto = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

print(count_paths(laberinto))  # Imprime las salias posibles 
