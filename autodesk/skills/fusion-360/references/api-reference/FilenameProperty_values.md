# FilenameProperty.values Property

Parent Object: [FilenameProperty](FilenameProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FilenameProperty.h>

## Description

Gets and sets the values associated with this property. HasMultipleValues property indicates if this property will be returning more than one value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filenameProperty\_var" is a variable referencing a FilenameProperty object. |

"filenameProperty\_var" is a variable referencing a FilenameProperty object. ```` ``` #include <Core/Application/FilenameProperty.h>  // Get the value of the property. std::vector<string> propertyValue = filenameProperty_var->values();  // Set the value of the property, where value_var is a string. bool returnValue = filenameProperty_var->values(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |