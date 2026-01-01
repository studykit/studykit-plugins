# MultiLineTextDefinition.rectangleLines Property

Parent Object: [MultiLineTextDefinition](MultiLineTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MultiLineTextDefinition.h>

## Description

Returns the four sketch lines that define the boundary of the sketch text. By adding constraints to these lines you can associatively control the size, position and angle of the sketch text. If the MultiLineTextDefinition object is obtained from a SketchTextInput object, this property will return null because the text and it's associated lines have not been created yet.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiLineTextDefinition\_var" is a variable referencing a MultiLineTextDefinition object. |

"multiLineTextDefinition\_var" is a variable referencing a MultiLineTextDefinition object. ```` ``` #include <Fusion/Sketch/MultiLineTextDefinition.h>  // Get the value of the property. std::vector<Ptr<SketchLine>> propertyValue = multiLineTextDefinition_var->rectangleLines(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [SketchLine](SketchLine.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |