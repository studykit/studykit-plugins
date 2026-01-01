# Attribute.value Property

Parent Object: [Attribute](Attribute.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attribute.h>

## Description

Gets and sets the value of this attribute.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attribute\_var" is a variable referencing an Attribute object.  ```` ``` # Get the value of the property. propertyValue = attribute_var.value  # Set the value of the property. attribute_var.value = propertyValue ``` ```` |

"attribute\_var" is a variable referencing an Attribute object. ```` ``` #include <Core/Application/Attribute.h>  // Get the value of the property. string propertyValue = attribute_var->value();  // Set the value of the property, where value_var is a string. bool returnValue = attribute_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |