# ChordLengthFilletEdgeSetInput.continuity Property

Parent Object: [ChordLengthFilletEdgeSetInput](ChordLengthFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChordLengthFilletEdgeSetInput.h>

## Description

Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType. The default is TangentSurfaceContinuityType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chordLengthFilletEdgeSetInput\_var" is a variable referencing a ChordLengthFilletEdgeSetInput object. |

"chordLengthFilletEdgeSetInput\_var" is a variable referencing a ChordLengthFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/ChordLengthFilletEdgeSetInput.h>  // Get the value of the property. SurfaceContinuityTypes propertyValue = chordLengthFilletEdgeSetInput_var->continuity();  // Set the value of the property, where value_var is a SurfaceContinuityTypes. bool returnValue = chordLengthFilletEdgeSetInput_var->continuity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceContinuityTypes](SurfaceContinuityTypes.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |