# FilenameProperty.isReadOnly Property

Parent Object: [FilenameProperty](FilenameProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FilenameProperty.h>

## Description

Indicates if this property is read-only. If True any attempted edits will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filenameProperty\_var" is a variable referencing a FilenameProperty object. |

"filenameProperty\_var" is a variable referencing a FilenameProperty object. ```` ``` #include <Core/Application/FilenameProperty.h>  // Get the value of the property. boolean propertyValue = filenameProperty_var->isReadOnly(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |