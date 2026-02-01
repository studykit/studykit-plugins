# ModelParameter.expression Property

Parent Object: [ModelParameter](ModelParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameter.h>

## Description

Gets and sets the expression used to calculate the value of the parameter. This is the equivalent of the "Expression" column in the Parameters dialog. Numeric parameters can be defined by a simple expression like "6.25", which will be interpreted based on whatever the default units are for the document. For example, if the units are set to millimeters, the value will be 6.25 mm; if the units are inches, it will be 6.25 inches. The expression can also contain the units so "6.25 in" will always be evaluated as inches regardless of the document units.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameter\_var" is a variable referencing a ModelParameter object.  ```` ``` # Get the value of the property. propertyValue = modelParameter_var.expression  # Set the value of the property. modelParameter_var.expression = propertyValue ``` ```` |

"modelParameter\_var" is a variable referencing a ModelParameter object. ```` ``` #include <Fusion/Fusion/ModelParameter.h>  // Get the value of the property. string propertyValue = modelParameter_var->expression();  // Set the value of the property, where value_var is a string. bool returnValue = modelParameter_var->expression(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |