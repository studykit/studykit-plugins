# More Reference Key Information

The following table details how the API determines primary and multiple matches for specific objects.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Category** | **Object** | **Cause of splits** | Expected behavior | |
| **Primary match** | **Multiple matches** |
| **Brep** | **Face** | Feature operations | BoundedFace algorithm will select that face which has maximum % of edges. | All other faces that share at least one edge with the original face. |
| Sketch splits | One of the resulting faces, Not deterministic | Not supported |
| Profile editing | One of the resulting faces, Not deterministic | Rest of the resulting faces, Not deterministic |
| Face merges & splits | Face with the earliest feature | Not supported |
| **Edge** | Feature operations | One of the resulting edges. Not deterministic | Rest of the split edges |
| Sketch splits | One of the resulting edges. Not deterministic | One of the resulting edges. Not deterministic |
| Face merges & splits | Edge with the earliest feature | Not supported |
| **Loop** | Feature operations | Match loop algorithm will select the primary match. | All other loops that share at least one edge with the original loop. |
| Sketch splits | One of the resulting loops, Not deterministic | Not supported |
| Face merges & splits | Loop with the earliest feature | Not supported |
| **Shell** | Feature operations | Match shell algorithm will select the primary match. | All other shells that share at least one face with the original shell. |
| Sketch splits | One of the resulting shells, Not deterministic | Not supported |
| Face merges & splits | Not supported | Not supported |
| **Sketch lines** | **Arcs** | Trim | One of the resulting arcs | Not supported |
| **Lines** | Trim | One of the resulting lines | Not supported |
| **Splines** | Trim | One of the resulting splines | Not supported |

## Exceptional Cases

**Profile Editing**

You can edit a profile for a feature to include additional
intersecting sketch entities so that a face or an edge gets split. In such a
case, one of
the resulting face/edge will the primary match. However the choice is not
deterministic. The other faces/edges will not be returned.

**Face Draft/ Face Splits**

In some special cases, new faces get generated when you add
face drafts or face splits. You could argue that these new faces are also
candidates for the purpose of multiple matches. However these new faces will
not be returned.
