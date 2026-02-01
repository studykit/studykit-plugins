# FilenameProperty.hasMultipleValues Property

Parent Object: [FilenameProperty](FilenameProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FilenameProperty.h>

## Description

Gets the boolean flag that indicates if this property has multiple values or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filenameProperty\_var" is a variable referencing a FilenameProperty object. |

"filenameProperty\_var" is a variable referencing a FilenameProperty object. ```` ``` #include <Core/Application/FilenameProperty.h>  // Get the value of the property. boolean propertyValue = filenameProperty_var->hasMultipleValues(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |