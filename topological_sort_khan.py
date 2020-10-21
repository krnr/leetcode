#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typing as t
from collections import defaultdict


def order(*, elements: t.Set[str], constraints: t.Dict[str, t.Set[str]]):
    return khans_algo(vertices=elements, edges=constraints)


def khans_algo(*, vertices: t.Set[str], edges: t.Dict[str, t.Set[str]]):
    """Use Khan's algorithm to implement topological sort of a graph.

    vertices: {"A", "B", "C"}
    edges: {"A": {"B", "C"}, "B": {"C"}}
    """
    el_in = defaultdict(set)
    el_out = defaultdict(set)

    def link(tail, head):
        el_out[tail].add(head)
        el_in[head].add(tail)
        print("after link:")
        print("in: ", el_in)
        print("out: ", el_out)

    def unlink(tail, head):
        el_out[tail].remove(head)
        el_in[head].remove(tail)

    indegree = lambda v: len(el_in[v])
    outdegree = lambda v: len(el_out[v])

    source = lambda v: indegree(v) == 0

    for tail in edges:
        for head in edges[tail]:
            link(tail, head)
        print("tail: ", tail)

    result = []
    S = set(filter(source, vertices))

    while len(S) > 0:
        print("S:", S)
        vertx = S.pop()
        result.append(vertx)
        print("result:", result)
        for head in tuple(el_out[vertx]):
            print("unlink head:", head)
            unlink(vertx, head)
            if source(head):
                S.add(head)

    # if no cycles:
    no_cycles = all(indegree(v) == 0 and outdegree(v) == 0 for v in vertices)
    if no_cycles:
        print("=" * 20)
        return result
    raise CyclomaticGraphException


class CyclomaticGraphException(Exception): pass

tasks = {"A", "B", "C", "D", "E"}
constraints = {
  "E": {"A"},
  "D": {"B", "C", "E"},
  "B": {"C"}
}

if __name__ == "__main__":
    print(order(elements=tasks, constraints=constraints))
