# SketchEntity.isReference Property

Parent Object: [SketchEntity](SketchEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntity.h>

## Description

Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEntity\_var" is a variable referencing a SketchEntity object. |

"sketchEntity\_var" is a variable referencing a SketchEntity object. ```` ``` #include <Fusion/Sketch/SketchEntity.h>  // Get the value of the property. boolean propertyValue = sketchEntity_var->isReference();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchEntity_var->isReference(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |