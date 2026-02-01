# SketchTextInput.definition Property

Parent Object: [SketchTextInput](SketchTextInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

Returns the SketchTextDefinition object associated with this input. When the SketchTextInput is first created this property will return null. Once one of the "set" methods have been called, this will return the SketchTextDefinition of the appropriate type and can be used to make any additional changes to the text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. |

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. ```` ``` #include <Fusion/Sketch/SketchTextInput.h>  // Get the value of the property. Ptr<SketchTextDefinition> propertyValue = sketchTextInput_var->definition(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchTextDefinition](SketchTextDefinition.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |