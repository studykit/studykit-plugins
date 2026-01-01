# BooleanProperty.value Property

Parent Object: [BooleanProperty](BooleanProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/BooleanProperty.h>

## Description

Gets and sets the value of this property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"booleanProperty\_var" is a variable referencing a BooleanProperty object. |

"booleanProperty\_var" is a variable referencing a BooleanProperty object. ```` ``` #include <Core/Application/BooleanProperty.h>  // Get the value of the property. boolean propertyValue = booleanProperty_var->value();  // Set the value of the property, where value_var is a boolean. bool returnValue = booleanProperty_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |