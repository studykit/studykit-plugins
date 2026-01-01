# Design.materials Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns the materials contained in this document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<Materials> propertyValue = design_var->materials(); ``` ```` |

## Property Value

This is a read only property whose value is a [Materials](Materials.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |