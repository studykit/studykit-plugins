# FilenameProperty.objectType Property

Parent Object: [FilenameProperty](FilenameProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FilenameProperty.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filenameProperty\_var" is a variable referencing a FilenameProperty object.  ```` ``` # Get the value of the property. propertyValue = filenameProperty_var.objectType ``` ```` |

"filenameProperty\_var" is a variable referencing a FilenameProperty object. ```` ``` #include <Core/Application/FilenameProperty.h>  // Get the value of the property. string propertyValue = filenameProperty_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |