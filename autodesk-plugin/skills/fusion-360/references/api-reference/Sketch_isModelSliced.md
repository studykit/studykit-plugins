# Sketch.isModelSliced Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Gets and sets whether the model is sliced along the sketch plane when this sketch is active. This provides access to the "Slice" setting in the "SKETCH PALETTE".

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. boolean propertyValue = sketch_var->isModelSliced();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketch_var->isModelSliced(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |