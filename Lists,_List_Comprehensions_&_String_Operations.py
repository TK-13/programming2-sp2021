{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Lists, List Comprehensions & String Operations.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TK-13/programming2-sp2021/blob/main/Lists%2C_List_Comprehensions_%26_String_Operations.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yZC2W4N2Gk69"
      },
      "source": [
        "## Lists"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EpoUH0cWAWNE"
      },
      "source": [
        "[Python's documentation on Lists](https://docs.python.org/3/tutorial/datastructures.html)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0t_cLpbJEK9b"
      },
      "source": [
        "Let's make some lists! In Python, lists don't have to be homogenous."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pH0Cdwj-EK9b"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZCezzGTYENfH"
      },
      "source": [
        "**Slicing a list** with list indices"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "z58Vp7v-ENfI"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2aSNkX0qENwS"
      },
      "source": [
        "\n",
        "**Copying a list:** assigning a list to another variable does not make a copy of that list. Instead, use `[:]` or `.copy()`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "llUmAB33ENwS"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NJhT7y3sEOA_"
      },
      "source": [
        "**If in:** checking if an item is in a list"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1v5zrrSjEOBA"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YkR3pLymEN20"
      },
      "source": [
        "**List Functions**\n",
        "\n",
        "*   `len(s)`\n",
        "*   `min(iterable, *[, key, default])`\n",
        "*   `max(iterable, *[, key, default])`\n",
        "*   `sum(iterable, /, start=0)`\n",
        "*   `all(iterable)`\n",
        "*   `any(iterable)`\n",
        "*   `sorted(iterable, *, key=None, reverse=False)`\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Xq9j9ap2EN21"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8W1yTgoDEN8E"
      },
      "source": [
        "**List Methods**\n",
        "\n",
        "*   `list.append(x)`\n",
        "*   `list.extend(iterable)`\n",
        "*   `list.insert(i, x)`\n",
        "*   `list.remove(x)`\n",
        "*   `list.pop([i])`\n",
        "*   `list.clear()`\n",
        "*   `list.index(x[, start[, end]])`\n",
        "*   `list.count(x)`\n",
        "*   `list.sort(*, key=None, reverse=False)`\n",
        "*   `list.reverse()`\n",
        "*   `list.copy()`\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "unEu7UaGEN8F"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oqBOD5L8EOFv"
      },
      "source": [
        "**Destroy a list element** with `del`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hzF-LkW3EOFw"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "953w17JpEOKk"
      },
      "source": [
        "**List concatenation**: merging two lists into one"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zUGQPjoAEOKl"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eKTK4xKSEOOt"
      },
      "source": [
        "**Iterating through lists**\n",
        "*   For each loop\n",
        "*   Index variable loop\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tVyzTBhcEOOu"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ISWDpAEoEOTp"
      },
      "source": [
        "**2 Dimensional Lists**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s3q6k92UEOTq"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4HP693uAEOYT"
      },
      "source": [
        "# List Comprehensions\n",
        "\"List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_f4XvRDsEOdX"
      },
      "source": [
        "Let's create a list of squares of the numbers from 1 to 10."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Z5Msy6JcEOdZ"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "h0mvnG-rEOg5"
      },
      "source": [
        "Now, the same, but with a list comprehension."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QDu_BVB3EOg7"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WuhQxWCUEIb_"
      },
      "source": [
        "Let's create a list of all the possible die rools with two six sided die, and remove the ones that are duplicates"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XpeohKG2_tDp"
      },
      "source": [
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NTGPfARBKhNx"
      },
      "source": [
        "Now let's do it with a list comprehension"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mAf1WKnRKhWj"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IzYMqi7xKvvz"
      },
      "source": [
        "We could also try one on a 2d list??"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bAdTtWVIKvmQ"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GCWQSRVUK1Lc"
      },
      "source": [
        "# String Operations"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KOdi08e5LYW9"
      },
      "source": [
        "Strings can be operated on similarly to lists :)\n",
        "\n",
        "[Python's documentation](https://docs.python.org/3/library/stdtypes.html#str)\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DxNbeoqcK1bj"
      },
      "source": [
        "**String concatenation**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A4ok9GMAK1hB"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "S-6FjfMyLsuv"
      },
      "source": [
        "**Uppercase and lowercase**\n",
        "*   `.upper()`\n",
        "*   `.lower()`\n",
        "*   `.isupper()`\n",
        "*   `.islower()`\n",
        "*   `.capitalize()`\n",
        "*   `str.swapcase()`\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9Oa8bkQpLszr"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wrwdsxP3Ls8X"
      },
      "source": [
        "**Substrings**\n",
        "*   slicing\n",
        "*   check for substring\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "q5zrvFm0LtBn"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "joUNaqc-LtKU"
      },
      "source": [
        "**Looping through characters in a string**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Nw2LsCkILtQV"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NCI5VIUPMUeu"
      },
      "source": [
        "**Most of the list functions and methods work on strings too!!**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G6-7EWC6MUlw"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t6Zj_7l5b6QI"
      },
      "source": [
        "**Some more string functions:**\n",
        "*   `str.endswith(suffix[, start[, end]])`\n",
        "*   `str.join(iterable)`\n",
        "*   `str.replace(old, new[, count])`\n",
        "*   `str.split(sep=None, maxsplit=-1)`\n",
        "*   `str.startswith(prefix[, start[, end]])`\n",
        "*   `str.strip([chars])`\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o0HIGi1Hb6cq"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gOWMJZDzMUu8"
      },
      "source": [
        "**String formatting** with `.format()`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "y-qLUcORMU1F"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}