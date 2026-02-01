# FloatProperty.values Property

Parent Object: [FloatProperty](FloatProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FloatProperty.h>

## Description

Gets and sets the values associated with this property. HasMultipleValues property indicates if this property will be returning more than one value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatProperty\_var" is a variable referencing a FloatProperty object.  ```` ``` # Get the value of the property. propertyValue = floatProperty_var.values  # Set the value of the property. floatProperty_var.values = propertyValue ``` ```` |

"floatProperty\_var" is a variable referencing a FloatProperty object. ```` ``` #include <Core/Application/FloatProperty.h>  // Get the value of the property. std::vector<double> propertyValue = floatProperty_var->values();  // Set the value of the property, where value_var is a double. bool returnValue = floatProperty_var->values(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |