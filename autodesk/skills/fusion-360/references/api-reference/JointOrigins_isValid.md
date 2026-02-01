# JointOrigins.isValid Property

Parent Object: [JointOrigins](JointOrigins.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigins.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigins\_var" is a variable referencing a JointOrigins object. |

"jointOrigins\_var" is a variable referencing a JointOrigins object. ```` ``` #include <Fusion/Components/JointOrigins.h>  // Get the value of the property. boolean propertyValue = jointOrigins_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |