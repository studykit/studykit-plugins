# PatternElement.faces Property

Parent Object: [PatternElement](PatternElement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElement.h>

## Description

Gets the faces generated as a result of this particular element.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElement\_var" is a variable referencing a PatternElement object. |

"patternElement\_var" is a variable referencing a PatternElement object. ```` ``` #include <Fusion/Features/PatternElement.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = patternElement_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |