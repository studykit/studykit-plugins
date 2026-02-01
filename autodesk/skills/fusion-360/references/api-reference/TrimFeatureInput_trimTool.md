# TrimFeatureInput.trimTool Property

Parent Object: [TrimFeatureInput](TrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatureInput.h>

## Description

Gets and sets the entity (a patch body, B-Rep face, construction plane or sketch curve) that intersects the trim tool

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatureInput\_var" is a variable referencing a TrimFeatureInput object. |

"trimFeatureInput\_var" is a variable referencing a TrimFeatureInput object. ```` ``` #include <Fusion/Features/TrimFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = trimFeatureInput_var->trimTool();  // Set the value of the property, where value_var is a Base. bool returnValue = trimFeatureInput_var->trimTool(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |