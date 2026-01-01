# UserParameter.value Property

Parent Object: [UserParameter](UserParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameter.h>

## Description

Gets and sets the real value (a double) of the parameter in database units. Setting this property will set/reset the expression value for this parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameter\_var" is a variable referencing a UserParameter object.  ```` ``` # Get the value of the property. propertyValue = userParameter_var.value  # Set the value of the property. userParameter_var.value = propertyValue ``` ```` |

"userParameter\_var" is a variable referencing a UserParameter object. ```` ``` #include <Fusion/Fusion/UserParameter.h>  // Get the value of the property. double propertyValue = userParameter_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = userParameter_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |