# ExtentDefinition.isValid Property

Parent Object: [ExtentDefinition](ExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtentDefinition.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extentDefinition\_var" is a variable referencing an ExtentDefinition object. |

"extentDefinition\_var" is a variable referencing an ExtentDefinition object. ```` ``` #include <Fusion/Features/ExtentDefinition.h>  // Get the value of the property. boolean propertyValue = extentDefinition_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |