# BaseFeature.constructionPlanes Property

Parent Object: [BaseFeature](BaseFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeature.h>

## Description

Returns an array of the construction planes associated with this base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeature\_var" is a variable referencing a BaseFeature object. |

"baseFeature\_var" is a variable referencing a BaseFeature object. ```` ``` #include <Fusion/Features/BaseFeature.h>  // Get the value of the property. std::vector<Ptr<ConstructionPlane>> propertyValue = baseFeature_var->constructionPlanes(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [ConstructionPlane](ConstructionPlane.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |