import pygame


def get_figure(width):
	figures_pos = [
		[(-1, 0), (-2, 0), (0, 0), (1, 0)], # palka
		[(0, -1), (-1, -1), (-1, 0), (0, 0)], # square
		[(-1, 0), (-1, 1), (0, 0), (0, -1)],
		[(0, 0), (-1, 0), (0, 1), (-1, -1)],
		[(0, 0), (0, -1), (0, 1), (-1, -1)], # L left
		[(-1, 0), (0, -1), (-1, 1), (-1, -1)], # L rigth
		[(0, 0), (0, -1), (0, 1), (-1, 0)]
	]

	figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
	return figures
