# -*- coding: utf-8 -*-
"""
Created on Sat Apr 2 14:05:10 2011

@author: Eric Burnett (ericburnett@gmail.com)
Released under the LGPL (or most other licenses on demand) - contact me if you
need appropriate headers stuck on.
"""

import pytest
from .life import Node, World, UsageError


def test_no_node_constructor():
    with pytest.raises(UsageError):
        Node(1, 1, 1, 1, 1)


def test_basic():
    box = Node.CanonicalNode(1, 1, 1, 1, 1)
    exp = box.Expand()
    exp2 = exp._Forward()
    expexp = exp.Expand()
    expexp2 = expexp._Forward()
    assert expexp2 == box.Expand()
    expexp3 = expexp2._Forward()
    assert expexp3 == box
    assert expexp3.Canonical() == box.Canonical()


def test_fill_node():
    box = Node.CanonicalNode(1, 1, 1, 1, 1)
    box2 = World.FillNode(((5, 5), (5, 6), (6, 5), (6, 6)))
    assert box.Expand() == box2

    blink = Node.CanonicalNode(
        2,
        Node.Zero(1),
        Node.Zero(1),
        Node.CanonicalNode(1, 1, 1, 0, 0),
        Node.CanonicalNode(1, 1, 0, 0, 0),
    )
    blink2 = World.FillNode(((0, 0), (1, 0), (2, 0)))
    assert blink == blink2


def test_inner_bounds():
    bounds = (1, 4, 3, 6)
    assert World._InnerBounds(bounds, 0) == (1, 2, 5, 6)
    assert World._InnerBounds(bounds, 1) == (3, 4, 5, 6)
    assert World._InnerBounds(bounds, 2) == (1, 2, 3, 4)
    assert World._InnerBounds(bounds, 3) == (3, 4, 3, 4)


def test_blinker():
    b = Node.CanonicalNode(
        2,
        Node.CanonicalNode(1, 0, 0, 1, 1),
        Node.CanonicalNode(1, 0, 0, 1, 0),
        Node.Zero(1),
        Node.Zero(1),
    )
    b_1 = b.ForwardN(1)
    b_2 = b.ForwardN(2)
    assert b.IsCanonical()
    assert b_1.IsCanonical()
    assert b_2.IsCanonical()
    b_1f = b_1.ForwardN(1)
    assert b_1f.IsCanonical()
    assert b_1f == b_2
    assert b != b_1
    assert b_1 != b_2
    assert b == b_2
    b_lots = b.ForwardN(2**32 + 1)
    assert b_lots == b_1


def test_performance():
    initial_state = [
        (-2, -2),
        (-2, -1),
        (-2, 2),
        (-1, -2),
        (-1, 1),
        (0, -2),
        (0, 1),
        (0, 2),
        (1, 0),
        (2, -2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]
    n = World.FillNode(initial_state)
    n.ForwardN(1000000)

