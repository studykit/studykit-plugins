# ModelParameter.createdBy Property

Parent Object: [ModelParameter](ModelParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameter.h>

## Description

Returns the object that created this parameter. For example, a feature, a sketch dimension, or a construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameter\_var" is a variable referencing a ModelParameter object. |

"modelParameter\_var" is a variable referencing a ModelParameter object. ```` ``` #include <Fusion/Fusion/ModelParameter.h>  // Get the value of the property. Ptr<Base> propertyValue = modelParameter_var->createdBy(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |