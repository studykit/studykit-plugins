# ChordLengthFilletEdgeSetInput.tangencyWeight Property

Parent Object: [ChordLengthFilletEdgeSetInput](ChordLengthFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChordLengthFilletEdgeSetInput.h>

## Description

Gets and sets the tangency weight for the given edge set. The tangency weight controls the influence of the continuity (G1 or G2) on the fillet. The ValueInput must be a real value between 0.1 and 2.0 inclusive, with no units. The default value is 1.0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chordLengthFilletEdgeSetInput\_var" is a variable referencing a ChordLengthFilletEdgeSetInput object. |

"chordLengthFilletEdgeSetInput\_var" is a variable referencing a ChordLengthFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/ChordLengthFilletEdgeSetInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = chordLengthFilletEdgeSetInput_var->tangencyWeight();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = chordLengthFilletEdgeSetInput_var->tangencyWeight(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |