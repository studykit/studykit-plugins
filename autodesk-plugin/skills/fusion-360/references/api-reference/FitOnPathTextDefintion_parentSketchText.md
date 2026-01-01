# FitOnPathTextDefintion.parentSketchText Property

Parent Object: [FitOnPathTextDefintion](FitOnPathTextDefintion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/FitOnPathTextDefintion.h>

## Description

Returns the SketchText object this definition is associated with. This property will return null in the case the definition object was obtained from a SketchTextInput object because the SketchText object does not yet exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fitOnPathTextDefintion\_var" is a variable referencing a FitOnPathTextDefintion object. |

"fitOnPathTextDefintion\_var" is a variable referencing a FitOnPathTextDefintion object. ```` ``` #include <Fusion/Sketch/FitOnPathTextDefintion.h>  // Get the value of the property. Ptr<SketchText> propertyValue = fitOnPathTextDefintion_var->parentSketchText(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchText](SketchText.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |