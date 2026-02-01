# ModelParameter.value Property

Parent Object: [ModelParameter](ModelParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameter.h>

## Description

Gets and sets the real value (a double) of the parameter in database units. Setting this property will set/reset the expression value for this parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameter\_var" is a variable referencing a ModelParameter object.  ```` ``` # Get the value of the property. propertyValue = modelParameter_var.value  # Set the value of the property. modelParameter_var.value = propertyValue ``` ```` |

"modelParameter\_var" is a variable referencing a ModelParameter object. ```` ``` #include <Fusion/Fusion/ModelParameter.h>  // Get the value of the property. double propertyValue = modelParameter_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = modelParameter_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |