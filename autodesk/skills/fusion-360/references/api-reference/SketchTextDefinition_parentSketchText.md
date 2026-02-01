# SketchTextDefinition.parentSketchText Property

Parent Object: [SketchTextDefinition](SketchTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextDefinition.h>

## Description

Returns the SketchText object this definition is associated with. This property will return null in the case the definition object was obtained from a SketchTextInput object because the SketchText object does not yet exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextDefinition\_var" is a variable referencing a SketchTextDefinition object. |

"sketchTextDefinition\_var" is a variable referencing a SketchTextDefinition object. ```` ``` #include <Fusion/Sketch/SketchTextDefinition.h>  // Get the value of the property. Ptr<SketchText> propertyValue = sketchTextDefinition_var->parentSketchText(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchText](SketchText.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |