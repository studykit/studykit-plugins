# IntegerProperty.values Property

Parent Object: [IntegerProperty](IntegerProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/IntegerProperty.h>

## Description

Gets and sets the values associated with this property. HasMultipleValues property indicates if this property will be returning more than one value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerProperty\_var" is a variable referencing an IntegerProperty object.  ```` ``` # Get the value of the property. propertyValue = integerProperty_var.values  # Set the value of the property. integerProperty_var.values = propertyValue ``` ```` |

"integerProperty\_var" is a variable referencing an IntegerProperty object. ```` ``` #include <Core/Application/IntegerProperty.h>  // Get the value of the property. std::vector<integer> propertyValue = integerProperty_var->values();  // Set the value of the property, where value_var is an integer. bool returnValue = integerProperty_var->values(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |