# Author:      Jacob Moore
# Date:        7/15/22
# Description: This program...


class Solution(object):
    def floodFill(self, image, sr, sc, color, og=-1):
        """
        :param og:
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if og == -1:
            og = image[sr][sc]
        # If image being looked at is equal to color, return image as is
        if sr > len(image) - 1 or sc > len(image[0]) - 1 or sr < 0 or sc < 0 or image == [] or image[sr][sc] != og or \
                image[sr][sc] == color:
            return image
        image[sr][sc] = color
        # Up
        image = self.floodFill(image, sr - 1, sc, color, og)
        # Right
        image = self.floodFill(image, sr, sc + 1, color, og)
        # Down
        image = self.floodFill(image, sr + 1, sc, color, og)
        # Left
        image = self.floodFill(image, sr, sc - 1, color, og)
        # Last thing to be done is change current to color

        return image


def main():
    a = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    print(a.floodFill(image, sr, sc, color))
    # Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    color = 0
    print(a.floodFill(image, sr, sc, color))
    # Output: [[0, 0, 0], [0, 0, 0]]


if __name__ == "__main__":
    main()
