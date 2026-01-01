# FilenameProperty.value Property

Parent Object: [FilenameProperty](FilenameProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FilenameProperty.h>

## Description

Gets and sets the value of this property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filenameProperty\_var" is a variable referencing a FilenameProperty object. |

"filenameProperty\_var" is a variable referencing a FilenameProperty object. ```` ``` #include <Core/Application/FilenameProperty.h>  // Get the value of the property. string propertyValue = filenameProperty_var->value();  // Set the value of the property, where value_var is a string. bool returnValue = filenameProperty_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |