# FusionDocument.parent Property

Parent Object: [FusionDocument](FusionDocument.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDocument.h>

## Description

Returns the parent Application object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDocument\_var" is a variable referencing a FusionDocument object. |

"fusionDocument\_var" is a variable referencing a FusionDocument object. ```` ``` #include <Fusion/Fusion/FusionDocument.h>  // Get the value of the property. Ptr<Application> propertyValue = fusionDocument_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Application](Application.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |