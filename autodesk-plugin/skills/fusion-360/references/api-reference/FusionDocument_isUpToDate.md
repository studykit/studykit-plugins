# FusionDocument.isUpToDate Property

Parent Object: [FusionDocument](FusionDocument.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDocument.h>

## Description

Indicates if any external references in the assembly are out of date. This is the API equivalent to the "Out of Date" notification displayed in the Quick Access Toolbar.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDocument\_var" is a variable referencing a FusionDocument object. |

"fusionDocument\_var" is a variable referencing a FusionDocument object. ```` ``` #include <Fusion/Fusion/FusionDocument.h>  // Get the value of the property. boolean propertyValue = fusionDocument_var->isUpToDate(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |