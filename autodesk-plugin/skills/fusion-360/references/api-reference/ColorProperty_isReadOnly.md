# ColorProperty.isReadOnly Property

Parent Object: [ColorProperty](ColorProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ColorProperty.h>

## Description

Indicates if this property is read-only. If True any attempted edits will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"colorProperty\_var" is a variable referencing a ColorProperty object. |

"colorProperty\_var" is a variable referencing a ColorProperty object. ```` ``` #include <Core/Application/ColorProperty.h>  // Get the value of the property. boolean propertyValue = colorProperty_var->isReadOnly(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |