# UserParameters.design Property

Parent Object: [UserParameters](UserParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameters.h>

## Description

Returns the design that owns the user parameters collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameters\_var" is a variable referencing a UserParameters object. |

"userParameters\_var" is a variable referencing a UserParameters object. ```` ``` #include <Fusion/Fusion/UserParameters.h>  // Get the value of the property. Ptr<Design> propertyValue = userParameters_var->design(); ``` ```` |

## Property Value

This is a read only property whose value is a [Design](Design.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |