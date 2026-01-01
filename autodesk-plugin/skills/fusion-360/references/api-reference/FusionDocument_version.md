# FusionDocument.version Property

Parent Object: [FusionDocument](FusionDocument.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDocument.h>

## Description

Returns the Fusion version this document was last saved with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDocument\_var" is a variable referencing a FusionDocument object. |

"fusionDocument\_var" is a variable referencing a FusionDocument object. ```` ``` #include <Fusion/Fusion/FusionDocument.h>  // Get the value of the property. string propertyValue = fusionDocument_var->version(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |