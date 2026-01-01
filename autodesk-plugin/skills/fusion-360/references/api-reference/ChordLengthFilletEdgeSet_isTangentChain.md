# ChordLengthFilletEdgeSet.isTangentChain Property

Parent Object: [ChordLengthFilletEdgeSet](ChordLengthFilletEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChordLengthFilletEdgeSet.h>

## Description

Gets and sets the Tangent chain for fillet. This enables tangent chain option for fillet.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chordLengthFilletEdgeSet\_var" is a variable referencing a ChordLengthFilletEdgeSet object. |

"chordLengthFilletEdgeSet\_var" is a variable referencing a ChordLengthFilletEdgeSet object. ```` ``` #include <Fusion/Features/ChordLengthFilletEdgeSet.h>  // Get the value of the property. boolean propertyValue = chordLengthFilletEdgeSet_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = chordLengthFilletEdgeSet_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |