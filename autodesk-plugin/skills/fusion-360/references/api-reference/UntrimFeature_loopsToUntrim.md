# UntrimFeature.loopsToUntrim Property

Parent Object: [UntrimFeature](UntrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeature.h>

## Description

Gets the loop objects to untrim. Returns null/None in the case where faces are specified instead of loops

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeature\_var" is a variable referencing a UntrimFeature object. |

"untrimFeature\_var" is a variable referencing a UntrimFeature object. ```` ``` #include <Fusion/Features/UntrimFeature.h>  // Get the value of the property. std::vector<Ptr<BRepLoop>> propertyValue = untrimFeature_var->loopsToUntrim(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [BRepLoop](BRepLoop.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |