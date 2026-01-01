# SketchLine.isReference Property

Parent Object: [SketchLine](SketchLine.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLine.h>

## Description

Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLine\_var" is a variable referencing a SketchLine object. |

"sketchLine\_var" is a variable referencing a SketchLine object. ```` ``` #include <Fusion/Sketch/SketchLine.h>  // Get the value of the property. boolean propertyValue = sketchLine_var->isReference();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchLine_var->isReference(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |