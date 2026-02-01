# ChordLengthFilletEdgeSetInput.entities Property

Parent Object: [ChordLengthFilletEdgeSetInput](ChordLengthFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChordLengthFilletEdgeSetInput.h>

## Description

Gets and sets the entities associated with this fillet edge set. For constant radius and chord length edge sets, this can be edges, faces, and features. For variable radius edges sets, this must be edges.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chordLengthFilletEdgeSetInput\_var" is a variable referencing a ChordLengthFilletEdgeSetInput object. |

"chordLengthFilletEdgeSetInput\_var" is a variable referencing a ChordLengthFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/ChordLengthFilletEdgeSetInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = chordLengthFilletEdgeSetInput_var->entities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = chordLengthFilletEdgeSetInput_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |