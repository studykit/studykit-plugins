# ChordLengthFilletEdgeSetInput.chordLength Property

Parent Object: [ChordLengthFilletEdgeSetInput](ChordLengthFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChordLengthFilletEdgeSetInput.h>

## Description

Gets and sets a ValueInput object that defines the chord length of the fillet. If the ValueInput uses a real value then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current document units for length.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chordLengthFilletEdgeSetInput\_var" is a variable referencing a ChordLengthFilletEdgeSetInput object. |

"chordLengthFilletEdgeSetInput\_var" is a variable referencing a ChordLengthFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/ChordLengthFilletEdgeSetInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = chordLengthFilletEdgeSetInput_var->chordLength();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = chordLengthFilletEdgeSetInput_var->chordLength(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |